import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.stats.diagnostic import acorr_ljungbox

def run_time_series_forecast(data, country, start_year=1989, end_year=2019):
    country_data = data[(data['Country'] == country)]
    country_ts = country_data.loc[:, str(start_year):str(end_year)].T.astype(float).squeeze()

    model = ExponentialSmoothing(country_ts, trend='add', seasonal=None).fit()
    forecast = model.forecast(4)

    lb_test = acorr_ljungbox(model.resid, lags=[10], return_df=True)
    return forecast, lb_test
