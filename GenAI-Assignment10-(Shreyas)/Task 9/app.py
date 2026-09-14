#Task 9 Mini Use Case
import pandas as pd
sales = {'Day':['Mon','Tue','Wed','Thu','Fri'],'Revenue':[1200,1500,900,2000,1800]}
df = pd.DataFrame(sales)
avg = df['Revenue'].sum()/len(df['Revenue'])
print(df['Revenue'].sum())
print('Average is ',avg)
print(df[df['Revenue']==df['Revenue'].max()])
print(df[df['Revenue']>avg])

# plotting 
df.plot(x='Day',y='Revenue')