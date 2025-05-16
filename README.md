# CO₂ Emissions Analysis Project

This project explores the key economic, demographic, and environmental factors that influence a country's annual CO₂ emissions, using data from the World Bank. We applied both regression and time series methods to understand historical patterns and forecast future emissions in the absence of the COVID-19 pandemic.

## Objectives
- Identify key drivers of CO₂ emissions across 165 countries.
- Analyze trends using linear regression with log-transformed variables.
- Forecast emissions using exponential smoothing models.

## Key Insights
- **GDP** and **Population** are the strongest predictors of CO₂ emissions.
- Linear regression models improved with added variables and transformations.
- **Exponential smoothing** produced accurate forecasts, especially for recent years and large emitters like China.

## Methods
- Multiple Linear Regression (8 models with incremental variables)
- Log transformation and dummy variable encoding
- Time series analysis for top 6 emitters: China, USA, India, Russia, Japan, Brazil
- Ljung-Box tests for autocorrelation

## Technologies
- Python (pandas, statsmodels, matplotlib)
- World Bank data (1989–2019)

## Limitations
- Sudden events like pandemics are difficult to capture.
- Future work could incorporate fossil fuel data and more advan

## Project Structure

### 1. `load_and_clean.py`
- Loads and preprocesses data from CSV.
- Renames key columns and drops missing values.

### 2. `feature_engineering.py`
- Applies log transformations on relevant columns (`CO2`, `GDP`, etc.).
- Encodes categorical income groups using one-hot encoding.

### 3. `regression_models.py`
- Builds and evaluates 8 regression models, incrementally adding features.
- Uses `statsmodels` to output model summaries.

### 4. `time_series_analysis.py`
- Performs time-series forecasting using Exponential Smoothing.
- Evaluates model performance with the Ljung-Box test for autocorrelation.

### 5. `visualization.py`
- Provides functions for plotting:
  - Variable correlations
  - Residual plots from regression models
  - Actual vs. forecasted CO₂ emissions

## Requirements

- pandas
- numpy
- matplotlib
- seaborn
- statsmodels

You can install the requirements via pip:
```bash
pip install pandas numpy matplotlib seaborn statsmodels
```

## Usage

1. Prepare the cleaned and merged dataset (with CO₂ emissions and predictors).
2. Use `load_and_clean_data()` to load the dataset.
3. Apply `engineer_features()` to transform and encode data.
4. Run `run_regression_models()` to analyze linear regression models.
5. Use `run_time_series_forecast()` to forecast emissions for selected countries.
6. Generate visualizations with `plot_correlation`, `plot_residuals`, and `plot_time_series`.

## Notes

- This analysis is based on World Bank data covering 165 countries from 1989 to 2019.
- Forecasting assumes no impact from COVID-19, providing a counterfactual view of CO₂ emissions.
