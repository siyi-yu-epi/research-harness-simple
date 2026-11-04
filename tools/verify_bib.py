#!/usr/bin/env python3
"""Check that every entry in a BibTeX file is a real, correctly cited work.

Entries with a DOI are looked up by DOI (OpenAlex, then doi.org). Others are
searched by title (Crossref, then OpenAlex). An entry is VERIFIED when the title
matches and the year and first author agree. Web pages, datasets and reports
without a DOI are checked by URL and listed as URL OK, for a manual look.

OpenAlex gives keyless requests a small daily budget shared by everyone on the
same network. Set OPENALEX_API_KEY (free from openalex.org) to use your own.
When OpenAlex is unavailable, entries it would have settled are UNCHECKED.

Usage:  python verify_bib.py refs.bib > refs.check.md
Exit code: 0 if every entry is VERIFIED or URL OK, 1 otherwise. Standard library only.
"""
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher

USER_AGENT = "research-harness-simple/0.1 (verify_bib.py)"
OPENALEX = "https://api.openalex.org/works"
CROSSREF = "https://api.crossref.org/works"
TITLE_OK = 0.9
NON_SCHOLARLY = {"misc", "online", "techreport", "report", "manual", "electronic", "dataset", "software"}
PASSING = {"VERIFIED", "URL OK"}
OPENALEX_REFUSED = [False]  # set when OpenAlex declines a lookup for the current entry

ENTRY_RE = re.compile(r"@\s*(\w+)\s*\{")
FIELD_RE = re.compile(r"([A-Za-z][\w-]*)\s*=\s*")
BARE_RE = re.compile(r"[^,\s}]+")


# --- BibTeX parsing --------------------------------------------------------

def _balanced(text, i):
    """Return (content of the brace group that opens at text[i], index after it)."""
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
    raise ValueError(f"unbalanced braces starting at character {i}")


def _fields(body):
    fields, i = {}, 0
    while m := FIELD_RE.search(body, i):
        name, j = m.group(1).lower(), m.end()
        if body[j:j + 1] == "{":
            value, i = _balanced(body, j)
        elif body[j:j + 1] == '"':  # a quote inside braces, e.g. {\"u}, doesn't end the value
            k, depth = j + 1, 0
            while k < len(body) and (body[k] != '"' or depth):
                depth += {"{": 1, "}": -1}.get(body[k], 0)
                k += 1
            value, i = body[j + 1:k], k + 1
        else:
            bare = BARE_RE.match(body, j)
            value, i = (bare.group(0), bare.end()) if bare else ("", j + 1)
        fields[name] = " ".join(value.split())
    return fields


def parse_bib(text):
    """Return [(key, entry_type, fields)], skipping @comment, @string and @preamble."""
    entries, pos = [], 0
    while m := ENTRY_RE.search(text, pos):
        body, pos = _balanced(text, m.end() - 1)
        entry_type = m.group(1).lower()
        if entry_type not in ("comment", "string", "preamble"):
            key, _, rest = body.partition(",")
            entries.append((key.strip(), entry_type, _fields(rest)))
    return entries


# --- Matching ----------------------------------------------------------------

def norm(s):
    """Lowercase ASCII words only, with LaTeX commands and accents removed."""
    s = re.sub(r"\\[a-zA-Z]+|\\.|[{}]", "", s or "")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s.lower()).split())


def title_score(a, b):
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0.0
    short, long_ = sorted((a, b), key=len)
    if long_.startswith(short) and len(short.split()) >= 4:  # subtitle missing on one side
        return 1.0
    return SequenceMatcher(None, a, b).ratio()


def first_author_family(authors):
    first = re.split(r"\s+and\s+", authors or "", maxsplit=1)[0].strip()
    if first.startswith("{") and first.endswith("}"):  # corporate author, e.g. {World Bank}
        return norm(first)
    family = first.split(",")[0] if "," in first else (first.split() or [""])[-1]
    return norm(family)


def quality(record, title, year, family):
    """(title matches, year agrees, first author appears, title score) for a found record."""
    score = title_score(title, record["title"])
    year_ok = not (year and record["year"]) or abs(year - record["year"]) <= 1
    names = " ".join(norm(a) for a in record["authors"])
    author_ok = not (family and record["authors"]) or bool(re.search(rf"\b{re.escape(family)}\b", names))
    return score >= TITLE_OK, year_ok, author_ok, score


def clean_doi(s):
    return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", (s or "").strip(), flags=re.I)


def _year(y):
    return int(y) if str(y).isdigit() else None


# --- Lookups -----------------------------------------------------------------

def get_json(url, accept="application/json"):
    """GET a JSON document; None on 404. Retries brief rate limits and server errors."""
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": accept})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            retry_after = e.headers.get("Retry-After") or ""
            wait = int(retry_after) if retry_after.isdigit() else 2 ** attempt
            if e.code not in (429, 500, 502, 503, 504) or attempt == 3 or wait > 30:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
            wait = 2 ** attempt
        finally:
            time.sleep(0.15)  # stay well under the APIs' rate limits
        time.sleep(wait)


def openalex(url):
    """OpenAlex JSON, or None if the work isn't there or OpenAlex declines (budget used up)."""
    if key := os.environ.get("OPENALEX_API_KEY"):
        url += ("&" if "?" in url else "?") + "api_key=" + urllib.parse.quote(key)
    try:
        return get_json(url)
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 429):
            OPENALEX_REFUSED[0] = True
            return None
        raise


def from_openalex(w):
    return {
        "title": w.get("title") or w.get("display_name") or "",
        "year": _year(w.get("publication_year")),
        "authors": [(a.get("author") or {}).get("display_name") or "" for a in w.get("authorships") or []],
        "id": (w.get("doi") or w.get("id") or "").replace("https://", ""),
    }


def from_csl(m):
    """Crossref search results and doi.org (CSL JSON) records share this shape."""
    title = m.get("title") or ""
    date = (m.get("issued") or m.get("published") or {}).get("date-parts") or [[None]]
    return {
        "title": (title[0] if title else "") if isinstance(title, list) else title,
        "year": _year(date[0][0]),
        "authors": [a.get("literal") or a.get("name") or f"{a.get('given', '')} {a.get('family', '')}".strip()
                    for a in m.get("author") or []],
        "id": "doi.org/" + (m.get("DOI") or ""),
    }


def by_doi(doi):
    work = openalex(f"{OPENALEX}/doi:{urllib.parse.quote(doi)}")
    if work:
        return from_openalex(work)
    csl = get_json(f"https://doi.org/{urllib.parse.quote(doi)}", accept="application/vnd.citationstyles.csl+json")
    return from_csl(csl) if csl else None


def by_title(title, year, family):
    """Best match from Crossref; OpenAlex is searched too unless Crossref gives a full match."""
    rank = lambda record: quality(record, title, year, family)
    query = urllib.parse.quote(f"{title} {family}".strip())
    data = get_json(f"{CROSSREF}?query.bibliographic={query}&rows=10") or {}
    candidates = [from_csl(m) for m in (data.get("message") or {}).get("items", [])]
    best = max(candidates, key=rank, default=None)
    if best is None or not all(rank(best)[:3]):
        data = openalex(f"{OPENALEX}?filter=title.search:{urllib.parse.quote(norm(title))}&per-page=10") or {}
        candidates += [from_openalex(w) for w in data.get("results", [])]
        best = max(candidates, key=rank, default=None)
    return best


def url_works(url):
    try:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request, timeout=30) as r:
            return r.status < 400
    except Exception:
        return False


# --- Checking ----------------------------------------------------------------

def check(entry_type, f):
    """Return (status, matched record id, notes) for one entry's fields."""
    OPENALEX_REFUSED[0] = False
    doi, title, url = clean_doi(f.get("doi")), f.get("title", ""), f.get("url")
    found = re.search(r"\d{4}", f.get("year") or f.get("date") or "")
    year, family = (int(found.group()) if found else None), first_author_family(f.get("author"))

    if not doi and url and entry_type in NON_SCHOLARLY and url_works(url):
        return "URL OK", url, "not a scholarly record: the URL works, check it by hand"

    problems = []
    record = by_doi(doi) if doi else None
    if doi and record is None:
        problems.append("DOI does not resolve")
    if record is None and title:
        record = by_title(title, year, family)
        full_match = record is not None and all(quality(record, title, year, family)[:3])
        if not full_match and OPENALEX_REFUSED[0] and not doi:
            closest = f'; closest so far: "{record["title"]}" ({record["year"]})' if record else ""
            return "UNCHECKED", "", ("no full match in Crossref, and OpenAlex declined the lookup (daily budget "
                                     "used up): set OPENALEX_API_KEY or retry after midnight UTC" + closest)
        if record is not None and not quality(record, title, year, family)[0]:
            problems.append(f'closest: "{record["title"]}"')
            record = None
    if record is None:
        return "NOT FOUND", "", "; ".join(problems)

    title_ok, year_ok, author_ok, _ = quality(record, title, year, family)
    if not title_ok:
        problems.append(f'DOI points to "{record["title"]}"')
    if not year_ok:
        problems.append(f"year {year} vs {record['year']}")
    if not author_ok:
        problems.append(f"first author '{family}' not among {', '.join(record['authors'][:3])}")
    return ("MISMATCH" if problems else "VERIFIED"), record["id"], "; ".join(problems)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.stdout.reconfigure(encoding="utf-8")
    path = sys.argv[1]
    with open(path, encoding="utf-8-sig") as fh:
        entries = parse_bib(fh.read())

    rows, seen, counts = [], set(), {}
    for key, entry_type, fields in entries:
        if key in seen:
            result = ("DUPLICATE", "", "key used more than once")
        else:
            seen.add(key)
            try:
                result = check(entry_type, fields)
            except Exception as e:  # network trouble: report it and keep going
                result = ("ERROR", "", f"lookup failed: {e}")
        counts[result[0]] = counts.get(result[0], 0) + 1
        rows.append((key, *result))

    print(f"# Reference check: {path}\n")
    print(f"{len(rows)} entries: " + ", ".join(f"{n} {s}" for s, n in sorted(counts.items())) + "\n")
    print("| Key | Status | Matched record | Notes |\n|---|---|---|---|")
    for key, status, record_id, notes in rows:
        print(f"| {key} | {status} | {record_id} | {' '.join(notes.split()).replace('|', '/')} |")
    sys.exit(0 if set(counts) <= PASSING else 1)


if __name__ == "__main__":
    main()
