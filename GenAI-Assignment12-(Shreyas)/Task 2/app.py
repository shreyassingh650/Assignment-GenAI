#task 2 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../performance.csv')
df['Parental_Education_Level'] = df['Parental_Education_Level'].astype('category')

sns.lineplot(data=df, x='Parental_Education_Level',y='Physical_Activity',hue='Gender')
sns.relplot(data=df,x='Parental_Education_Level',y='Physical_Activity',hue='Gender',markers='o',kind='line',col='Family_Income')
plt.show()
