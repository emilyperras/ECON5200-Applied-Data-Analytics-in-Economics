# Descriptive Statistics & Anomaly Detection  
## Computational Laboratory: Robustness in a Skewed World

**Lab 4 — Applied Data Analytics in Economics**

---

## Objective: The Tech Economist Mindset

Traditional statistics teaches analysts to trust the **average**.  
In modern data-driven markets, however, the average often becomes a **vanity metric** distorted by extreme observations.

This lab reframes statistical analysis through the lens of a **Tech Economist**, treating data as a marketplace system where anomalies carry economic meaning rather than noise.

Using the **California Housing Dataset** — a proxy for real-world PropTech platforms such as Zillow or Airbnb — the project investigates how skewed distributions and structural constraints (e.g., price caps) challenge classical statistical assumptions.

The analytical progression moves from:

**Manual Statistical Forensics → Algorithmic Anomaly Detection**

---

## Dataset Context: A Skewed Marketplace

The California Housing dataset contains socioeconomic and housing characteristics across districts. A key feature is the **Median House Value ceiling** at \$500k, creating a real-world phenomenon known as a **ceiling effect**.

This artificial cap mirrors constraints frequently observed in platform economies where reporting limits distort distributions and bias averages.

Primary variables analyzed include:

- Median Income (`MedInc`)
- House Age (`HouseAge`)
- Average Rooms (`AveRooms`)
- Average Bedrooms (`AveBedrms`)
- Population
- Median House Value (`MedHouseVal`)

---

## Technical Approach

### Phase 1 — Data Inspection

- Ingested and explored housing market data.
- Visualized distributional skew and confirmed the ceiling effect.
- Demonstrated how capped outcomes distort summary statistics.

---

### Phase 2 — Manual Statistical Forensics (Foundations First)

Before automation, anomaly detection was performed manually using **robust statistics**.

**Methodology:**
- Calculated Quartiles (Q1, Q3)
- Computed Interquartile Range (IQR)
- Implemented the **Tukey Fence (1.5 × IQR rule)**
- Flagged univariate outliers in median income

**Insight:**  
The exercise highlights the fragility of the mean relative to the robustness of the median when distributions contain heavy tails.

Visualization via boxplots illustrated how extreme values pull central tendency metrics — the “Elon Musk Effect” in income distributions.

---

### Phase 3 — Algorithmic Anomaly Detection

Manual rules detect only **univariate anomalies**. Real markets exhibit anomalies across relationships between variables.

To detect multivariate irregularities, an **Isolation Forest** model was implemented:

- Unsupervised anomaly detection
- Ensemble-based isolation of rare observations
- Contamination parameter set to 5% (expected anomaly share)
- Feature space included income, housing characteristics, and population metrics

The algorithm identified observations that were **few and structurally different**, rather than merely extreme in one dimension.

---

### Phase 4 — Human vs. Machine Comparison

A visual comparison evaluated differences between:

- Human-defined statistical outliers (IQR)
- Machine-detected anomalies (Isolation Forest)

Key finding:

> Machine learning detects *relationship anomalies* — cases where variables interact unusually — that traditional statistical rules cannot identify.

---

## Robustness Report: Tech Economist Analysis

After separating the dataset into **core market observations** and **anomalous districts**, a comparative forensic analysis was conducted.

### Analytical Tasks

- Split dataset into normal and anomalous groups
- Compared:
  - Mean vs Median income and housing values
  - Standard Deviation vs Median Absolute Deviation (MAD)
- Measured the **Inequality Wedge**:
  
