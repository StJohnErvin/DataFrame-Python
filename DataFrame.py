import pandas as pd

mdata = pd.read_csv('Marketing.csv')

mdata.info()
mdata.head()

mdata.isnull().sum()

mdata[mdata['Date'].isna()]

mdata = mdata.dropna()
mdata.isnull().sum()

mdata['Day_Name'].describe()

mdata[mdata['Day_Name'] == 'Monday']

mdata[(mdata['Day_Name'] == 'Monday') & (mdata['Promo'] == 'No Promo')]

mdata = mdata.sort_values(by = 'Revenue', ascending = False)

mdata.head()

mdata.groupby('Day_Name')['Revenue'].sum()

mdata['Revenue per spend'] = mdata['Revenue'] / mdata['Marketing Spend']
mdata.head()
