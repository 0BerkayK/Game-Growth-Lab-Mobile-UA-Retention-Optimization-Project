# Game Growth Lab 🚀

## Overview

**Game Growth Lab** is a comprehensive project designed to simulate and optimize mobile game user acquisition and retention strategies through data-driven performance marketing analysis.

This project covers the full growth marketing funnel—from campaign planning, LTV modeling, campaign performance evaluation, marketing sync with game updates, to retention strategies and industry trend responses.

---

## Project Structure

---

```bash
game_growth_lab/
│
├── data/
│ ├── user_acquisition.csv
│ ├── installs.csv
│ ├── sessions.csv
│ ├── purchases.csv
│ ├── retention.csv
│ └── game_updates.csv
│
├── notebooks/
│ ├── 01_campaign_planning.ipynb
│ ├── 02_ltv_prediction_model.ipynb
│ ├── 03_performance_analysis.ipynb
│ ├── 04_marketing_update_sync.ipynb
│ ├── 05_retention_strategy.ipynb
│ └── 06_trend_response_summary.ipynb
│
├── dashboards/
│ └── growth_kpi_dashboard.pbix
│
├── scripts/
│ └── generate_data.py
│
├── README.md
└── requirements.txt

```


---

## Features & Objectives

### 1. Campaign Planning & Optimization
- Simulate multi-platform ad campaigns (TikTok, Meta, Google UAC).
- Analyze KPIs such as CPI, CTR, CVR.
- Conduct A/B creative testing.
- Identify the most efficient channels and creatives.

### 2. LTV Prediction Model
- Predict 30-day LTV using early user behavior (sessions, retention, early purchases).
- Utilize XGBoost regression for modeling.
- Evaluate with MAE and RMSE metrics.
- Generate segment-based LTV curves and CSV reports.

### 3. Campaign Performance Analysis & Growth Optimization
- Calculate ROAS.
- Compare channel performances.
- Analyze funnel drop-off rates.
- Recommend budget reallocations.
- Visualize KPIs via dashboards.

### 4. Marketing & Game Update Synchronization
- Assess impact of game updates on user behavior.
- Compare D1/D7 retention pre- and post-update.
- Analyze creative success tied to update features.

### 5. User Acquisition & Retention Strategies
- Perform cohort analysis.
- Simulate bonus/onboarding effects.
- Conduct push notification A/B tests.
- Develop segment-specific action plans.

### 6. Industry Trends & Action Plan
- Monitor trends like playable ads and rewarded videos.
- Simulate creative tests aligned with trends.
- Provide actionable recommendations based on data.

---

## Data Description

- `user_acquisition.csv`: Ad campaign performance metrics by platform and creative.
- `installs.csv`: User install dates.
- `sessions.csv`: User session activity.
- `purchases.csv`: Purchase records.
- `retention.csv`: Retention metrics (D1, D7, D30).
- `game_updates.csv`: Dates and content summaries of game updates.

---

## How to Use

1. Clone the repository.
2. Install dependencies from `requirements.txt`.
3. Run `scripts/generate_data.py` to generate simulated datasets.
4. Open and run notebooks in the `notebooks/` folder step-by-step:
   - Start with `01_campaign_planning.ipynb` for campaign simulations.
   - Follow through to `06_trend_response_summary.ipynb`.
5. Explore and customize the dashboard in `dashboards/growth_kpi_dashboard.pbix`.

---

## Technologies & Tools

- Python (Pandas, NumPy, Scikit-learn, XGBoost)
- Jupyter Notebooks
- Power BI / Tableau for dashboards
- Simulated datasets for realistic analysis

---

## Author

Berkay Korcum

---

## License

This project is for educational and demonstration purposes.




