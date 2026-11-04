#!/usr/bin/env python3
"""Render a Markdown file to a standalone HTML page, and optionally to Word, with pandoc.

Usage:  python render.py FILE.md [--bib refs.bib] [--docx]

Writes FILE.html next to FILE.md, with images and styles embedded so the page
works on its own, and FILE.docx with --docx. With --bib, [@key] citations are
resolved from that BibTeX file and a reference list is added; a key missing from
the file is an error. Needs pandoc on PATH, or `pip install pypandoc_binary`.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

STYLE = Path(__file__).with_name("style.css")


def pandoc():
    if exe := shutil.which("pandoc"):
        return exe
    try:
        import pypandoc
        return pypandoc.get_pandoc_path()
    except (ImportError, OSError):
        sys.exit("pandoc not found: install it (Windows: winget install JohnMacFarlane.Pandoc) "
                 "or run `pip install pypandoc_binary`")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", type=Path, help="Markdown file")
    parser.add_argument("--bib", type=Path, help="BibTeX file for [@key] citations")
    parser.add_argument("--docx", action="store_true", help="also write a Word file")
    args = parser.parse_args()

    src = args.source.resolve()
    lines = src.read_text(encoding="utf-8").splitlines()
    title = next((line[2:].strip() for line in lines if line.startswith("# ")), src.stem)
    command = [pandoc(), src.name, "--from", "markdown"]
    if args.bib:
        command += ["--citeproc", "--bibliography", str(args.bib.resolve())]
    targets = {src.with_suffix(".html"): ["--standalone", "--embed-resources", "--css", str(STYLE),
                                          "--metadata", f"pagetitle={title}"]}
    if args.docx:
        targets[src.with_suffix(".docx")] = []

    missing = set()
    for out, options in targets.items():
        run = subprocess.run(command + options + ["--output", str(out)], cwd=src.parent,
                             capture_output=True, text=True, encoding="utf-8", errors="replace")
        sys.stderr.write(run.stderr)
        if run.returncode:
            sys.exit(f"pandoc failed on {src.name}")
        missing |= set(re.findall(r"[Cc]itation (\S+) not found", run.stderr))
        print(out)
    if missing:
        sys.exit(f"citation keys not in {args.bib.name}: {', '.join(sorted(missing))}")


if __name__ == "__main__":
    main()
