#task 4: Bivariate Distribution
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../performance.csv')
sns.histplot(data=df,x='Hours_Studied',y='Attendance')
plt.figure()
sns.kdeplot(data=df,x='Hours_Studied',y='Attendance')
plt.show()