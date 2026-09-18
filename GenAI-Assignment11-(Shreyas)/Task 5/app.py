#task 5 Stacked Bar Chart
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

df = pd.read_csv('../Automotive.csv')
df['ORDERDATE'] = df['ORDERDATE'].astype('datetime64[ns]').dt.month_name().astype('category')
data = df.groupby('ORDERDATE')['SALES'].sum()
df['PRODUCT'] = df['PRODUCT'].astype('category')

print(df['PRODUCT'].value_counts().head(3))

c = df[df['PRODUCT']=='Classic Cars'].groupby('ORDERDATE')['SALES'].sum()
v = df[df['PRODUCT']=='Vintage Cars'].groupby('ORDERDATE')['SALES'].sum()
m = df[df['PRODUCT']=='Motorcycles'].groupby('ORDERDATE')['SALES'].sum()

#indexing
c.index = pd.CategoricalIndex(c.index,categories=months,ordered=True)
v.index = pd.CategoricalIndex(v.index,categories=months,ordered=True)
m.index = pd.CategoricalIndex(m.index,categories=months,ordered=True)

#sorting index
c = c.sort_index()
v = v.sort_index()
m = m.sort_index()
#plotting

plt.bar(months,c.values, label='Classic Car')
plt.bar(months,v.values,bottom=c.values, label='Vintage Car')
plt.bar(months,m.values,bottom=c.values+v.values, label='Motorcycles')
plt.title('Sales of different years')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.xticks(rotation=45)
plt.show()