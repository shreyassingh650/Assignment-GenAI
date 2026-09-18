#task 2 Scatter Plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../Sales.csv')
print(df.sample())
df['Temperature'] = df['Temperature'].astype('int16')
print(df['Temperature'].unique())
data = df.groupby('Temperature')['Fuel_Price'].mean()
x = data.index
y = data.values
plt.scatter(x,y,marker='+',color='pink')
plt.title('Temperature vs Fuel Graph')
plt.xlabel('Temperature')
plt.ylabel('Fuel Price')
plt.show()