#Task 6: Categorical Plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../performance.csv')
df['Motivation_Level'] = df['Motivation_Level'].astype('category')

sns.barplot(data=df,x='Motivation_Level',y='Hours_Studied')
plt.figure()
sns.boxplot(data=df,x='Motivation_Level',y='Hours_Studied')
plt.figure()
sns.violinplot(data=df,x='Motivation_Level',y='Hours_Studied')
plt.figure()
sns.countplot(data=df,x='Motivation_Level')
plt.show()