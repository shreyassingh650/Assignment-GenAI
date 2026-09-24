#task 3 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../performance.csv')
sns.histplot(data=df,x='Hours_Studied')
plt.figure()
sns.kdeplot(data=df,x='Hours_Studied',fill=True)
plt.figure()
sns.rugplot(data=df,x='Hours_Studied')
plt.figure()
sns.histplot(data=df,x='Hours_Studied',stat='density')
sns.kdeplot(data=df,x='Hours_Studied',fill=True)
plt.show()

