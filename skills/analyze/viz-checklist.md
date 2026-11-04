# Figures and tables checklist

A working checklist for `rh:analyst`. The figure principles paraphrase, in our own words, Kieran Healy, *Data Visualization: A Practical Introduction* (Princeton University Press, 2018; free to read at socviz.co). The table rules follow common reporting practice at top journals. The book's examples use R's ggplot2; in Python, plotnine follows the same grammar, and matplotlib or seaborn work as well.

## Figures
- Start from the comparison the reader needs to make. Put the things being compared side by side on a common scale: position along a shared axis is read more accurately than length, angle, area or color.
- Show the data, not only summaries, where you can: points (jittered if they overlap), distributions, ranges. Avoid bars with error bars for continuous outcomes.
- Use small multiples (one panel per group, with shared axes) rather than piling many series into one panel.
- Order categories by a meaningful value, not alphabetically.
- Label lines and points directly where you can, rather than relying on a legend. Axis titles say what the variable is, in plain words, with its units.
- Use color to carry a variable, not for decoration: a sequential palette for ordered values, a diverging palette around a meaningful midpoint, a qualitative palette for categories. Use colorblind-safe palettes, and don't make color the only cue.
- Leave out chart junk: 3-D effects, heavy gridlines, background shading, dual y-axes. Bar charts start at zero.
- Show uncertainty with confidence intervals or bands. Report regression results as coefficient plots: point estimates with intervals, sorted meaningfully, with a reference line at zero. With interactions or nonlinear terms, plot predicted values or marginal effects across a meaningful range instead of raw coefficients.
- Use maps only when location is the point. Choropleth maps show rates, not counts.
- Each figure stands on its own, with a caption saying what's shown, the data source, the sample and N.
- Save each figure as PDF (vector, for the paper) and PNG (for review), with consistent fonts that are legible at print size.

## Tables
- **Descriptive statistics** (usually Table 1): N, mean, standard deviation, minimum and maximum (and the median for skewed variables) for the dependent, independent and control variables; split by group when there's a treatment and a control; a correlation matrix if the venue expects one.
- **Regression tables**: one column per specification, building from simple to full. Coefficients with standard errors in parentheses, saying which kind of standard error and the level of clustering; significance shown the way the venue does it (stars, exact p-values or confidence intervals); N and R² (or the model's equivalent); rows marking which fixed effects and controls each column includes; the dependent variable named at the top.
- A note under every table: the sample, the estimation method, the standard errors, the significance legend, and where the variables are defined.
- Code generates every table, as Markdown and CSV (e.g. with `pyfixest`'s `etable`, or `statsmodels` and `linearmodels` with a table writer). Never type numbers by hand.
