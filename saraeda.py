import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from pandas.tools.plotting import scatter_matrix
import statsmodels.formula.api as smf

training_data = pd.read_csv("Train.csv")
model = training_data['ModelID']
years = training_data['YearMade']


#Seeing potential correlation between model ID and saleprice: result is that there's no clear correlation between model ID increasing and increased.
model2 = sm.ols(formula = 'SalePrice ~ ModelID, data=training_data)
modeled2 = model.fit()
print(modeled2.summary())

#saleprice regressed with columns that have low numbers of NaN but seem to potentially be correlated.
model = sm.ols(formula = 'SalesPrice ~ YearMade + state + Hydraulics + Enclosure + auctioneerID', data=training_data)
modeled = model.fit()
print modeled.summary()

#scatter matrix for many of our potentially correlated datapoints
scatter_matrix(training_data,figsize=(12,12))
est = smf.ols(formula='SalePrice ~  + SalesID +MachineID+ModelID+datasource+saledate+fiModelDesc+fiBaseModel+fiProductClassDesc+state+ProductGroup+ProductGroupDesc+YearMade +Enclosure',data=training_data).fit()
