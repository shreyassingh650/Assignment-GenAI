#Task 1 - Load Data from CSV
import pandas as pd 

df = pd.read_csv('../performance.csv')
print(df.shape)
print(df.columns)
print(df.head())
df.info()
print(df['Gender'].value_counts())
print(df.describe())