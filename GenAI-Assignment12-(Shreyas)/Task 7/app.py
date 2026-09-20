#Task 7 Regression Plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('../performance.csv')
df['Parental_Education_Level'] = df['Parental_Education_Level'].astype('category')

sns.regplot(data=df,x='Hours_Studied',y='Attendance')
sns.lmplot(data=df,x='Hours_Studied',y='Attendance',hue='Parental_Education_Level')

plt.show()
