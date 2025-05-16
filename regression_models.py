import statsmodels.api as sm
from statsmodels.tools import add_constant

def run_regression_models(data):
    X_sets = [
        ['log_GDP'],
        ['log_GDP', 'log_Population'],
        ['log_GDP', 'log_Population', 'Electricity'],
        ['log_GDP', 'log_Population', 'Electricity', 'LifeExpect'],
        ['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture'],
        ['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture', 'log_ArableLand'],
        ['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture', 'log_ArableLand', 'RenewableConsumption'],
        ['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture', 'log_ArableLand', 'RenewableConsumption'] + list(data.select_dtypes(include='category').cat.categories[1:])
    ]

    y = data['log_CO2']
    models = []

    for i, features in enumerate(X_sets):
        X = add_constant(data[features])
        model = sm.OLS(y, X).fit()
        models.append(model)
        print(f"\nModel {i+1} Summary:\n{model.summary()}")

    return models
