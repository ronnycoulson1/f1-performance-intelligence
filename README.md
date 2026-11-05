# 🏎️ F1 Performance Intelligence

**Formula 1 Data Analytics & Machine Learning**

An end-to-end engineering project using Python, data analytics, and machine learning to analyze Formula 1 performance and predict race outcomes.

Part of **LIFE — Automotive AI & Motorsport Engineering**, exploring how AI and data can help us understand what makes cars fast.

## Project Objectives

- Analyze historical F1 driver and team performance.
- Identify trends in race results and starting positions.
- Develop machine learning models to predict race outcomes.
- Build an interactive performance analytics dashboard.
- Explore predictions for the 2027 F1 season.

## Project Progress

**Milestone 1 — Data Collection ✅**
- Collected all 24 races from the 2025 F1 season.
- Retrieved 479 driver results using the Jolpica F1 API.
- Organized the data into a structured CSV dataset.

**Milestone 2 — Data Analysis (Next)**
- Driver and team performance analysis.
- Positions gained/lost and consistency metrics.
- Data visualization.

**Milestone 3 — Machine Learning (Planned)**
- Random Forest and XGBoost prediction models.
- Top-10 finish and podium probability predictions.
- Model testing and evaluation.

**Milestone 4 — Dashboard (Planned)**
- Interactive visualization of F1 performance and predictions.

## Tech Stack

**Current:** Python, Pandas, Requests, Jolpica F1 API, Git.

**Planned:** Scikit-learn, XGBoost, Matplotlib, Streamlit.

## Getting Started

```bash
git clone https://github.com/ronnycoulson1/f1-performance-intelligence.git
cd f1-performance-intelligence

python3 -m venv .venv
source .venv/bin/activate

pip install pandas requests
python src/collect_data.py
```

The dataset is saved to `data/raw/f1_2025_results.csv`.

## Author

**Ronny Coulson**

Computer Science | AI & Machine Learning | Automotive Engineering

[GitHub](https://github.com/ronnycoulson1)
