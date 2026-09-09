#task 1 Pandas
import pandas as pd
file = pd.read_csv('../titan.csv').squeeze('columns')
df = pd.read_csv('tit.csv')
file1 = pd.read_csv('Titanic-Dataset.csv',index_col='Name').squeeze('columns')
print(file1)
print(file1.sort_values())