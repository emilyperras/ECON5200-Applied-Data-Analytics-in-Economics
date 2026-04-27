## Lab 6: The Architecture of Bias

### Objective
Investigate how bias arises from the **Data Generating Process (DGP)** and sampling decisions, and how these issues distort machine learning results before modeling even begins.

### Tech Stack
- Python  
- pandas, numpy  
- scipy (Chi-Square testing)  
- scikit-learn  

---

### Methodology

#### 1. Sampling Error via Simple Random Sampling
I manually simulated **Simple Random Sampling** on the Titanic dataset to demonstrate how randomness alone can introduce high variance. Even with correct methodology, small or imbalanced samples produced unstable estimates, highlighting the limits of naive random sampling.

#### 2. Eliminating Covariate Shift with Stratified Sampling
I implemented **Stratified Sampling** using `sklearn` to preserve class distributions (e.g., survival rates). This reduced covariate shift between training and test sets, improving the reliability and generalizability of downstream models.

#### 3. SRM Forensic Audit (Chi-Square Test)
I performed a **Sample Ratio Mismatch (SRM)** check on an A/B test using a Chi-Square test. This detects whether observed group splits deviate significantly from expected allocations (e.g., 50/50), which can reveal engineering issues such as broken randomization or load balancing errors.

---

### Key Insight
Most modeling failures are not caused by algorithms—they originate from **biased data pipelines**. Understanding and correcting the DGP is often more impactful than tuning models.

---

### Theoretical Question

**Why does analyzing only successful Unicorn startups (e.g., from TechCrunch) lead to survivorship bias?**

This creates **survivorship bias** because the dataset only includes companies that succeeded and were visible, while excluding the much larger set of startups that failed or were never covered. As a result, any patterns observed (e.g., growth strategies, funding levels) are misleading because they ignore the full population.

**What ghost data is needed for a Heckman Correction?**

To correct this bias, you need **ghost data** on the *selection process*, including:

- Startups that failed or shut down  
- Startups that never reached Unicorn status  
- Startups not covered by TechCrunch (i.e., not selected into the sample)  
- Variables influencing selection (e.g., media exposure, investor networks, geography)

This allows you to model:
1. **Selection Equation** — who gets observed  
2. **Outcome Equation** — who succeeds  

Without this missing data, estimates remain biased because the sample is not representative of the true population.

---

### Takeaway
Bias is structural. If the data is flawed, the model will be too—no matter how sophisticated the algorithm.
