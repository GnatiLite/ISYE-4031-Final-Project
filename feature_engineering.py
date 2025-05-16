import numpy as np
import pandas as pd

def engineer_features(data):
    data['log_CO2'] = np.log(data['Emissions'])
    data['log_GDP'] = np.log(data['GDP'])
    data['log_Population'] = np.log(data['Population'])
    data['log_ArableLand'] = np.log(data['ArableLand'])

    # Encode income group
    data['IncomeGroup'] = pd.Categorical(data['IncomeGroup'])
    dummies = pd.get_dummies(data['IncomeGroup'], drop_first=True)
    data = pd.concat([data, dummies], axis=1)

    return data
