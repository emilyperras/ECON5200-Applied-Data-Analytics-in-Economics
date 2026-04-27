## Audit 02: Deconstructing Statistical Lies
**ECON 5200 — Module 2: Probability, Robustness & Sampling**  
**Role:** Data Quality Auditor at Pareto Ventures  

### Overview
Three portfolio companies claimed "perfect" metrics. This audit dissects each claim using forensic statistics, revealing how averages can mask catastrophic risk, near-useless detectors, biased experiments, and phantom returns.

---

### Finding 1: Latency Skew — The Mean Is a Lie
**Company:** NebulaCloud | **Claim:** Mean latency = 35ms  
**Method:** DGP simulation (980 normal + 20 spike requests) → MAD vs SD comparison  
**Finding:**  
- The **Standard Deviation** was inflated ~100× beyond the MAD because just 20 spike requests (2% of traffic) contributed enormous squared deviations.  
- The **Median Absolute Deviation (MAD)** remained stable, revealing that 50% of real traffic deviates by only ~8ms from the true center.  
- **Verdict:** NebulaCloud's "stable server" claim is statistically false. Their P99 latency reaches 5,000ms — a catastrophic user experience hidden inside a tidy mean.

---

### Finding 2: False Positives — When Accuracy Becomes Useless
**Company:** IntegrityAI | **Claim:** 98% accurate plagiarism detector  
**Method:** Manual Bayes' Theorem across three base-rate scenarios  
**Finding:**  
| Context | Base Rate | P(Cheater \| Flagged) |
|---|---|---|
| Bootcamp | 50% | ~98% |
| Econ Class | 5% | ~72% |
| Honors Seminar | 0.1% | ~4.7% |
- In an Honors Seminar, **~95% of flagged students are innocent** despite the 98% accuracy claim.  
- **Verdict:** Detector accuracy is meaningless without knowing the population base rate. IntegrityAI's product is dangerous in low-prevalence environments.

---

### Finding 3: Sample Ratio Mismatch — The Experiment Was Broken
**Company:** FinFlash | **Claim:** Successful A/B test, 50/50 split  
**Method:** Manual Chi-Square Goodness of Fit test  
**Finding:**  
- Observed: Control = 50,250 | Treatment = 49,750 (difference: 500 users)  
- χ² statistic = **5.00 > 3.84** (critical value, α = 0.05)  
- **Verdict:** The experiment is **INVALID**. A statistically significant imbalance means the randomization was compromised — likely a client-side crash in the treatment arm. Any reported lift cannot be attributed to the product change.

---

### Finding 4: Survivorship Bias — The Memecoin Graveyard
**Context:** Crypto token analysis (e.g., Pump.fun)  
**Method:** Pareto-distributed simulation of 10,000 token launches  
**Finding:**  
- Mean market cap across all 10,000 tokens: ~$2,000  
- Mean market cap for Top 1% survivors: ~$200,000+  
- Bias multiplier: **~100×**  
- **Verdict:** Any report that analyzes only listed/surviving tokens overstates typical returns by two orders of magnitude. The graveyard of failed tokens is the real data.

---

### Key Takeaways
| Technique | When the Mean Lies | Correct Tool |
|---|---|---|
| Robustness | Skewed distributions, outliers | Median, MAD |
| Probability | Rare events, high-accuracy detectors | Bayes' Theorem |
| Experimental Validity | A/B test imbalance | Chi-Square (SRM check) |
| Selection Bias | Survivorship in financial data | Full population analysis |

> *"In a Pareto World, the mean is a vanity metric. The auditor's job is to find the statistical lie hidden in the average."*
