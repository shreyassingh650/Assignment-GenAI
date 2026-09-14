#task 5 Important DataFrame Functions
import pandas as pd
students ={'Name':['Amit','Neha','Rahul','Sneha','Pooja'],'Marks':[78,85,90,66,72],'Subject':['Math','Math','Science','Science','Math']}

df = pd.DataFrame(students)
print(df.info())
print(df.describe())
print(df.head())
print(df.tail())

df.sort_values('Marks',ascending=False,inplace=True)
print(df)
df.reset_index(inplace=True,drop=True)
print(df)