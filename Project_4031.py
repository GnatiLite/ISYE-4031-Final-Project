import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tools import add_constant

# Load the data
data = pd.read_csv('/Users/nattie/Downloads/API_EN.GHG.ALL.MT.CE.AR5_DS2_en_csv_v2_3850.csv', skiprows=4)

# Preprocessing: Select and clean columns
data = data.rename(columns={'Country Name': 'Country'})
data = data.dropna()  # Drop rows with missing values for simplicity

# Define log-transformed variables
data['log_CO2'] = np.log(data['Emissions'])  # Replace with actual column for CO2
data['log_GDP'] = np.log(data['GDP'])  # Replace with actual column for GDP
data['log_Population'] = np.log(data['Population'])
data['log_ArableLand'] = np.log(data['ArableLand'])

# Categorical encoding for IncomeGroup
data['IncomeGroup'] = pd.Categorical(data['IncomeGroup'])  # Replace with the actual column name

# Define independent variables incrementally
X1 = add_constant(data[['log_GDP']])
X2 = add_constant(data[['log_GDP', 'log_Population']])
X3 = add_constant(data[['log_GDP', 'log_Population', 'Electricity']])
X4 = add_constant(data[['log_GDP', 'log_Population', 'Electricity', 'LifeExpect']])
X5 = add_constant(data[['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture']])
X6 = add_constant(data[['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture', 'log_ArableLand']])
X7 = add_constant(data[['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture', 'log_ArableLand', 'RenewableConsumption']])
X8 = add_constant(pd.get_dummies(data[['log_GDP', 'log_Population', 'Electricity', 'LifeExpect', 'Agriculture', 'log_ArableLand', 'RenewableConsumption', 'IncomeGroup']], drop_first=True))

# Dependent variable
y = data['log_CO2']

# Run models incrementally
models = []
for X in [X1, X2, X3, X4, X5, X6, X7, X8]:
    model = sm.OLS(y, X).fit()
    models.append(model)

# Display summary of all models
for i, model in enumerate(models):
    print(f"\nModel {i+1}:")
    print(model.summary())
