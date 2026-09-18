#task 1 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../Sales.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['Date'] = df['Date'].dt.month_name()
df['Monthly_Sales'] = df['Monthly_Sales'].astype('int64')

data = df.groupby('Date')['Monthly_Sales'].sum()
month = ['January','February','March','April','May','June','July','August','September','October','November','December']
data.index = pd.CategoricalIndex(data.index,categories=month,ordered=True)
data = data.sort_index()
x = data.index
y = data.values

plt.plot(x,y)
plt.title('Sales Trend Over Months')

plt.xlabel('Months')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()


