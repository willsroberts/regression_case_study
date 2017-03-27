import pandas as pd
import statsmodels.formula.api as smf

train_unc_data = pd.read_csv('data/Train.csv')

train_cln_data = train_unc_data[train_unc_data['MachineHoursCurrentMeter'].notnull() ]
train_cln_data = train_cln_data[train_cln_data['Transmission'].notnull() ]
train_cln_data = train_cln_data[train_cln_data['ProductSize'].notnull() ]
train_cln_data = train_cln_data[train_cln_data['YearMade'] != 1000]

cols = train_unc_data.columns.values
query_cols = ''
for x in cols:
    if train_cln_data[x].count() > 0:
        if x not in ['SalePrice','saledate','auctioneerID','state','fiSecondaryDesc','datasource']:
            query_cols += x + "+"
query_cols = query_cols[:-1]

final_query = "SalePrice ~ " + query_cols

est = smf.ols(formula=final_query,data=train_cln_data).fit()
print est.summary()
