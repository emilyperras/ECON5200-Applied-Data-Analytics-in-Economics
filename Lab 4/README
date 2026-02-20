# Hypothesis Testing & Causal Evidence Architecture  
**The Epistemology of Falsification: Hypothesis Testing on the Lalonde Dataset**

---

## Objective

This project operationalizes the scientific method within an empirical data science workflow by shifting the analytical focus from **estimation** to **falsification**. Rather than optimizing models to fit observed outcomes, the analysis evaluates competing causal narratives by attempting to reject incorrect explanations through statistical testing.

Using the Lalonde (1986) job training dataset, the project frames causal inference as a process of **structured skepticism** — testing whether observed treatment effects withstand rigorous attempts at refutation. The objective is not simply to measure outcomes, but to determine whether the data provides sufficient evidence to invalidate the Null Hypothesis under multiple statistical assumptions.

---

## Technical Approach

The analysis implements a dual-framework hypothesis testing architecture designed for robustness under real-world data conditions:

- **Parametric Testing (Signal-to-Noise Estimation)**
  - Applied Welch’s T-Test using SciPy to estimate the Average Treatment Effect (ATE) of job training participation.
  - Treated hypothesis testing as a signal-detection problem, quantifying whether observed earnings differences exceeded sampling noise.
  - Accounted for unequal variances between treatment and control groups.

- **Non-Parametric Validation**
  - Conducted a permutation test with 10,000 resamples to validate results without relying on normality assumptions.
  - Constructed an empirical null distribution to evaluate robustness against skewed earnings data.

- **Statistical Discipline**
  - Controlled for **Type I error risk** through formal hypothesis testing procedures.
  - Cross-validated conclusions across parametric and distribution-free methods to reduce model-dependent inference.

---

## Key Findings

The analysis identified a statistically significant increase in real earnings of approximately **$1,795** for participants in the job training program.

Across both parametric and non-parametric frameworks, results consistently rejected the Null Hypothesis — demonstrating causal evidence through **proof by statistical contradiction**, rather than model fitting alone.

---

## Business Insight

In an algorithmic economy increasingly driven by large datasets and automated decision systems, rigorous hypothesis testing functions as a critical **safety valve** against false discovery.

Without falsification frameworks, organizations risk:
- data grubbing,
- overfitting narratives to noise,
- and deploying models built on spurious correlations.

Robust hypothesis testing enforces epistemic discipline by requiring claims to survive adversarial statistical scrutiny. This transforms analytics from descriptive pattern recognition into **decision-grade causal evidence**, enabling organizations to deploy data products with greater reliability, interpretability, and governance confidence.

---

## Tools & Concepts

- Python (analysis scripts pre-built)
- SciPy statistical testing framework
- Welch’s T-Test
- Non-parametric permutation testing
- Average Treatment Effect (ATE)
- Hypothesis testing & falsification methodology
- Type I error control
- Causal inference fundamentals

---
