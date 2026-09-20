#Task 7 Pie Chart (Market Share)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../Automotive.csv')
df['COUNTRY'] = df['COUNTRY'].astype('category')
#plotting
data = df.groupby('COUNTRY')['SALES'].sum()
arr = np.zeros(data.shape[0])
arr[0] = 0.1
plt.figure(figsize=(20,20))
plt.pie(data,labels=data.index,autopct='%0.1f%%',explode=arr,startangle=90)
plt.title('Country Sales')
plt.legend()
plt.show()

