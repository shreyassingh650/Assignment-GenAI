#task 3 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../WHO.csv')
df['Status'] = df['Status'].astype('category')
df.dropna(subset='Life expectancy',inplace=True)
data = df.groupby('Status')['Life expectancy'].mean()

x=data.index
y=data.values


# plt.bar(x,y) #Vertical Bar Chart
plt.barh(x,y,color='blue')
plt.title('Life Expect vs Country Status')
plt.xlabel('Life Expect')
plt.ylabel('Country')
plt.xlim(10,100)
plt.show()

