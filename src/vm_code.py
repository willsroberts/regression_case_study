import pandas as pd
import numpy as np
import random
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

train_data = pd.read_csv('../data/Train.csv')
train_data.head()

# create list of features that matter for regression, exclude those that don't
excluded = ['SalePrice','SalesID', 'MachineID', 'ModelID', 'datasource', 'auctioneerID', 'fiModelDesc', 'fiBaseModel', 'fiSecondaryDesc', 'fiModelSeries', 'fiModelDescriptor']

# remove features with lots of null values
high_NaN_count = ['auctioneerID', 'MachineHoursCurrentMeter','UsageBand', 'fiSecondaryDesc','fiModelSeries','fiModelDescriptor']
cols = list(train_data)

def remove_from_list(l, to_exclude):
    for elem in to_exclude:
        if elem in l:
            l.remove(elem)

remove_from_list(cols, excluded)
remove_from_list(cols, high_NaN_count)

features = '+'.join(cols)
query = 'SalePrice~' + features

big_model = smf.ols(formula = query,data=df).fit()
