#Task 5 Understanding the Data
import pandas as pd 

df = pd.read_csv('../performance.csv')
print(df.shape)
print(df.dtypes)
print(df.select_dtypes('int64'))
print(df.select_dtypes('category'))
print(df['Sleep_Hours'].isna().sum())
print(df['Sleep_Hours'].value_counts())
df.info()