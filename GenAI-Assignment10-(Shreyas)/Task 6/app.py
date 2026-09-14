#Task 6: Filtering and Conditional Selection
import pandas as pd
students ={'Name':['Amit','Neha','Rahul','Sneha','Pooja'],'Marks':[78,85,90,66,72],'Subject':['Math','Math','Science','Science','Math']}

df = pd.DataFrame(students)

print(df[df['Marks']>75])
print(df[df['Subject']=='Math'])
#more than average marks
print(df[df['Marks']>(sum(df['Marks'])/len(df['Marks']))])
print(df[df['Marks']<70])