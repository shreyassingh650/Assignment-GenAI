#Task 7 Grouping and Basic Analysis
import pandas as pd
students ={'Name':['Amit','Neha','Rahul','Sneha','Pooja'],'Marks':[78,85,90,66,72],'Subject':['Math','Math','Science','Science','Math']}

df = pd.DataFrame(students)
print(df.groupby('Subject')['Marks'].sum()/len(df.groupby('Subject')['Marks']))
print(df['Subject'].value_counts())
print(df.groupby('Subject')['Marks'].max())