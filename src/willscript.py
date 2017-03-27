import pandas as pd
import statsmodels.formula.api as smf
import sys

print "Number of Args: " + str(len(sys.argv))
print sys.argv

def dummify(df,column):
    print '{} is your baseline'.format(sorted(df[column].unique())[-1])
    dummy = pd.get_dummies(df[column]).rename(columns=lambda x: column+'_'+str(x)).iloc[:,0:len(df[column].unique())-1]
    df = df.drop(column,axis=1) #Why not inplace? because if we do inplace, it will affect the df directly
    return pd.concat([df,dummy],axis=1)

file_loc = sys.argv[1]
test_data_loc = sys.argv[2]

train_unc_data = pd.read_csv(file_loc)
test_data = pd.read_csv(test_data_loc)


categorical_cols = ['Travel_Controls','Ripper','Hydraulics','Enclosure','Transmission','Blade_Type','fiProductClassDesc','fiModelDescripter','fiModelSeries','fiBaseModel','fiModelDesc','UsageBand']

train_cln_data = train_unc_data[train_unc_data['MachineHoursCurrentMeter'].notnull() ]
train_cln_data = train_cln_data[train_cln_data['Transmission'].notnull() ]
train_cln_data = train_cln_data[train_cln_data['ProductSize'].notnull() ]
train_cln_data = train_cln_data[train_cln_data['YearMade'] != 1000]

for each in categorical_cols:
    train_clean_data= dummify(test_data, each)

# train_cln_data = train_unc_data

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

# test_data = test[[train_cln_data.columns.values]]

# final_predictions = est.predict(test_data)
