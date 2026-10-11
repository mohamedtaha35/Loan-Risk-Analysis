# Loan Risk Analysis Project

An end-to-end data analytics project examining borrower profiles and loan application data to evaluate default risk, identify key risk indicators, and provide data-driven lending recommendations.

---

## Project Overview
This project merges loan application data with borrower profiles to build a unified fact table (`Fact_table_clean.csv`). Exploratory data analysis, custom risk-bucket transformations, and data visualizations were performed using Python (Pandas and Matplotlib) and Excel to answer core credit risk questions and establish risk mitigation thresholds[cite: 3, 4, 5].

---

## Key Business Questions & Findings

1. **Default Rate by Credit Score Range**
   * **Overall Default Rate:** 24.29%[cite: 4]
   * **Highest Risk Bracket:** The **520–599** credit score bucket exhibits the highest default rate at **49.14%**[cite: 4]. Default rates progressively decrease as credit scores improve, dropping to 11.69% for borrowers with a credit score of 750+[cite: 2].

2. **DTI Ratio & Risk Thresholds**
   * **Relationship:** The correlation between DTI and default status is modest (~0.20)[cite: 4]. 
   * **Recommendation:** It is recommended to establish a strict cutoff for loan approvals at the **High (51–75%)** DTI bucket, where default rates elevate significantly[cite: 4].

3. **Loan Purpose Risk Analysis**
   * **Highest Risk Purpose:** **Investment & Growth** loans carry the highest risk with a default rate of **25.41%**[cite: 4].
   * **Loan Amount Impact:** Average loan amounts do not differ significantly between defaulted and non-defaulted loans (a difference of only $557.80), indicating loan size alone is not the primary driver of default[cite: 4].

4. **Employment Status & Tenure**
   * **Impact:** Employment status and years employed show limited direct linear correlation with default risk[cite: 4]. However, borrowers with less than 2 years of employment experience a higher default propensity (~28.77%) compared to their more established counterparts[cite: 4].

---

## Strategic Recommendations
* **Credit Score Cutoff:** Enforce a minimum credit score threshold of **600** for standard loan approvals[cite: 4].
* **DTI Cap:** Limit maximum allowable DTI ratios to **50%** to mitigate exposure to critical debt burdens[cite: 4].
* **Portfolio Risk Management:** Apply stricter underwriting criteria and enhanced monitoring for high-risk segments, specifically the **520–599 credit bracket**, **High DTI ranges (>51%)**, and **Investment & Growth** loan purposes[cite: 4].

---

## Project Structure & Files
* `loan_applications.csv`: Raw loan application records.
* `borrower_profiles.csv`: Borrower demographic and background profiles.
* `Exploring phase.py`: Python script handling data ingestion, cleaning, table merging, metric feature engineering, and correlation heatmap generation.
* `Fact_table_clean.csv`: The finalized, processed dataset combining application and borrower data.
* `Project Q and A.docx`: Detailed business documentation answering core credit risk queries and outlining underwriting recommendations[cite: 4].
* `Project_Dashboard.png`: Visual dashboard highlighting credit score buckets, DTI scatter distributions, and loan purpose risk comparisons[cite: 5].

---

## Technologies Used
* **Python**: Pandas, NumPy, Matplotlib
* **Excel**: Data formatting, formulas, and visual dashboard creation
* **Data Visualization**: Custom correlation heatmaps, bar charts, and scatter plots