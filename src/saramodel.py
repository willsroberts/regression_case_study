import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
import statsmodels.formula.api as smf
from patsy.contrasts import Treatment
from statsmodels.formula.api import ols

training_data = pd.read_csv("Train.csv")

cleaning = training_data.groupby(['datasource'])
cleaning = cleaning[cleaning['YearMade'] != 1000]

# cleaned = training_data.dropna(axis = 0,how = 'all',thresh=5)
# #
# model_1a = smf.ols(formula = 'SalePrice ~ Enclosure+Forks+Hydraulics', data = cleaned)
# modeled_1a = model_1a.fit()
# print (modeled_1a.summary())

#model_auctioneer = sm.ols(formula = 'SalePrice ~ ModelID, data=training_data)
#modeled_auctioneer = model_auctioneer.fit()
#print(modeled_auctioneer.summary())

#mod = ols('SalePrice ~ C(fiBaseModel, Treatment)', data = training_data)
#res = mod.fit()
#print (res.summary())

#ModelID --> Stringifying
#ModelID --> associating
#Dropping null rows

#res1 = smf.ols(formula='Lottery ~ Literacy : Wealth - 1', data=df).fit()
#res2 = smf.ols(formula='Lottery ~ Literacy * Wealth - 1', data=df).fit()
#print res1.params, '\n'
#print res2.params
