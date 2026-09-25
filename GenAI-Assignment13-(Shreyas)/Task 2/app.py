#Task 2 - Load Data From JSON
import pandas as pd

#convert json to pd.dataframe

df = pd.read_json('iris.json')
print(type(df))
print(df)