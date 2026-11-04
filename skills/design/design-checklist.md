# Research design checklist

A working checklist for `rh:designer`. It paraphrases, in our own words, the elements of a research plan set out in John W. Creswell and J. David Creswell, *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches* (SAGE), and adds standard practice for common empirical designs in the social sciences. Use the parts that fit the study.

## Framing (all approaches)
- **Approach.** Quantitative, qualitative or mixed methods, and why it fits the question. Name the worldview behind it (postpositivist, constructivist, transformative, pragmatic) only if the venue expects that.
- **Problem.** What the problem is and who it affects; what studies have done about it; what they leave out; and why closing that gap matters, and to which audiences.
- **Purpose statement.** One or two sentences: the study's intent, the design, the variables or central phenomenon, the participants or units, and the setting.
- **Questions or hypotheses.**
  - Quantitative: relate named variables, and state hypotheses tied to the theory (directional where the theory supports a direction).
  - Qualitative: one open central question ("how" or "what") and a few sub-questions, which may evolve.
  - Mixed: a quantitative question, a qualitative one, and a question about what combining them adds.
- **Theory.**
  - Quantitative: the theory as an explanation tested deductively, with its source, its propositions, and how they produce the hypotheses.
  - Qualitative: theory as a lens from the start, or as the outcome (as in grounded theory).
  - Mixed: a theory or framework that shapes the whole design.

## Quantitative designs
**Surveys**
- The design (cross-sectional or longitudinal), the mode, and why a survey fits.
- The population, sampling frame and sampling method (random, stratified, convenience), and its limits.
- The sample size, from a power analysis: expected effect size, alpha, power.
- Recruitment, compensation, attention checks, and pre-specified exclusion rules.
- The instrument: each scale with its source and its reliability and validity evidence; any adaptations; a pilot test.
- A variables table: research question → variable → survey items.
- Analysis: response rate and non-response bias; descriptives; the test for each hypothesis; missing data; effect sizes and confidence intervals, not only p-values.

**Experiments**
- The participants, and how they're assigned (random assignment, or a quasi-experiment and why).
- The design (between- or within-subjects, factorial), the conditions, the manipulation and the manipulation check.
- The procedure, step by step, and the power analysis.
- Threats to internal validity (history, maturation, selection, attrition, testing, instrumentation, diffusion of treatment, demand effects) and to external validity (other people, settings and times), and how each is handled.

**Observational and secondary data** (standard practice in economics, management and information systems)
- The data source, access, coverage, unit of analysis and time window, and the sample construction steps with the count after each.
- A variables table: the dependent, independent and control variables, and any proxies, each with its definition and source.
- The identification strategy, argued for this setting:
  - **Difference-in-differences**: treatment and control groups; when treatment starts; with staggered adoption, estimators robust to heterogeneous effects (e.g. Callaway and Sant'Anna; Sun and Abraham); an event-study test of pre-trends; why parallel trends is plausible; anticipation; spillovers.
  - **Instrumental variables**: the instrument; relevance (the first stage, and weak-instrument diagnostics); the case for the exclusion restriction.
  - **Regression discontinuity**: the running variable and cutoff; a test for manipulation at the cutoff; the bandwidth choice; covariate balance at the cutoff.
  - **Panel fixed effects**: which fixed effects, and what variation is left to identify the effect.
  - **Matching or weighting**: the covariates, balance diagnostics and overlap.
- The main specification as an equation, the standard errors and the level of clustering.
- Robustness (alternative measures, samples, specifications and estimators; placebo tests), mechanisms (tests of the proposed channel) and heterogeneity (pre-specified subgroups, and why each).

**Machine learning and computational work**
- The data source, the labels and how they were made; training, validation and test splits (split by time where leakage is a risk).
- The algorithms, baselines, tuning procedure and evaluation metrics; interpretability.
- How model outputs feed the substantive analysis, and how measurement error in machine-generated variables is handled.

## Qualitative designs
- The design (narrative, phenomenology, grounded theory, ethnography, case study) and why it fits.
- The researcher's role and reflexivity: background, relationship to the site and participants, and how that may shape interpretation.
- Purposeful sampling of sites and participants: the strategy, the numbers and the rationale (e.g. saturation), and how access is gained.
- Data collection (interviews, observation, documents, audiovisual material), each with its protocol and how it's recorded.
- Analysis: the steps from raw data to codes, themes and interpretation; the codebook; any software; and the procedures specific to the design.
- Validity: several strategies, such as triangulation, member checking, rich description, clarifying the researcher's bias, presenting discrepant evidence, prolonged engagement, peer debriefing and an external audit. Reliability: checking transcripts, guarding against drift in the codebook, intercoder agreement.
- What kind of generalization is claimed: analytic or theoretical generalization, or transferability.

## Mixed methods
- The core design: convergent; explanatory sequential (quantitative, then qualitative); or exploratory sequential (qualitative, then quantitative, often to build an instrument). Or a complex design (an experiment, case study, evaluation or participatory study) built on one of these.
- Why mix, and the priority and timing of each strand.
- Where and how the strands are integrated (merging, connecting, building, embedding), a joint display of the results, and what happens if they disagree.
- Validity threats specific to the design, such as how participants for a follow-up phase are selected.

## Ethics and logistics
- IRB review: the likely category (exempt, expedited or full) and how long it takes; informed consent; risks and benefits; privacy and data security (de-identification, storage); compensation; any deception, and the debriefing.
- Data-use agreements for restricted data, and licenses for open data.
- A timeline with milestones; the costs (panel fees, data licenses); and the main risks to the plan, with a fallback for each.
