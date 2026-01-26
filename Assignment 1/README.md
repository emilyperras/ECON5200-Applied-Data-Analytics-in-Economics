# The Cost of Living Crisis: A Data-Driven Analysis

## The Problem
The official Consumer Price Index (CPI) suggests inflation is cooling, but many students feel their cost of living is still rising quickly. This happens because CPI is designed to measure inflation for an “average consumer,” but students have a very different spending profile—especially due to housing and tuition.

## Methodology
Using Python in Google Colab, I built a **Student Pricing Index (Student SPI)** to better reflect real student budget pressures. I collected CPI proxy series from the Federal Reserve Economic Data (**FRED**) API using `fredapi`, then normalized all series to a common baseline of **2016 = 100** to ensure comparability across categories with different base years. I constructed the Student SPI using a weighted basket methodology (Laspeyres-style approach), with heavier emphasis on tuition and rent relative to the official CPI structure.

## Key Findings
My analysis reveals a **[2]% divergence** between the Student SPI and the Official CPI since 2016, between the Student SPI and the Official CPI since 2016, showing that student costs tracked closely to national inflation in this model.

## Tools & Skills Demonstrated
- Python (`pandas`, `matplotlib`)
- API data collection (FRED / `fredapi`)
- Index construction & normalization (2016 = 100)
- Weighted basket inflation modeling (Student SPI)
- Data visualization and interpretation
