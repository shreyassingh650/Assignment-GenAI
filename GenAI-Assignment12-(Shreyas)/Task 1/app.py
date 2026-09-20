#task 1 Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../performance.csv')

sns.relplot(data=df,x='Hours_Studied',y='Attendance',hue='Parental_Involvement',kind='line')
sns.relplot(data=df,x='Hours_Studied',y='Attendance',hue='Parental_Involvement',kind='scatter')
plt.show()


