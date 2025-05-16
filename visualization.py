import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation(data):
    sns.pairplot(data, vars=['log_CO2', 'log_GDP', 'log_Population', 'Electricity', 'LifeExpect'])
    plt.suptitle('Correlation Plot', y=1.02)
    plt.show()

def plot_residuals(model):
    residuals = model.resid
    plt.figure()
    plt.scatter(model.fittedvalues, residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.title('Residual Plot')
    plt.xlabel('Fitted values')
    plt.ylabel('Residuals')
    plt.show()

def plot_time_series(actual, forecast, title):
    plt.figure()
    plt.plot(actual.index, actual.values, label='Actual')
    plt.plot(forecast.index, forecast.values, label='Forecast', linestyle='--')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions')
    plt.legend()
    plt.show()
