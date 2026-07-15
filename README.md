
# Brent Oil Price Change Point Analysis

## Project Overview
This project analyzes how major geopolitical and economic events affect Brent oil prices using Bayesian change point detection. The analysis covers daily Brent oil prices from May 20, 1987, to September 30, 2022.

## Project Objectives
1. Identify key events that have significantly impacted Brent oil prices
2. Quantify how much these events affect price changes using statistical methods
3. Provide clear, data-driven insights to guide investment strategies and policy development

## Key Findings
- Change Point Detected: August 30, 2018
- Price Before: $74.91 per barrel
- Price After: $77.20 per barrel
- Price Change: +$2.29 (+3.1%)
- Multiple Change Points: 8 significant structural breaks identified

## Interactive Dashboard
An interactive dashboard is included to explore the analysis results:

Features:
- Price history chart with change points
- Log returns (volatility) chart
- Price distribution by decade
- Top 5 events by price impact
- Complete list of detected change points

How to Open:
1. Download Brent_Oil_Dashboard_Final.html
2. Double-click to open in your browser
3. No internet connection needed!

## How to Run
1. Clone this repository
2. Install dependencies: pip install -r requirements.txt
3. Open the notebook: jupyter notebook notebooks/brent_oil_analysis.ipynb
4. Run all cells

## Dependencies
- Python 3.8+
- PyMC for Bayesian modeling
- ArviZ for model diagnostics
- Pandas, NumPy for data manipulation
- Matplotlib, Seaborn for visualization
- Statsmodels for stationarity testing
- Ruptures for multiple change point detection
- Flask for API backend

## Results
The Bayesian change point model detected a structural break in oil prices around August 30, 2018. This period coincided with:
- US re-imposition of sanctions on Iran
- Venezuela's ongoing production decline
- Market adjustments to OPEC production decisions

## Author
Blen Assefa

## Date
July 16, 2026

## License
MIT
