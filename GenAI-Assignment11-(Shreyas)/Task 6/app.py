#Task 6: Histogram Marks Distribution
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../Automotive.csv')
# plotting

plt.hist(df['SALES'],bins=10,log=True)
plt.title('Sales Histogram')
plt.xlabel('Sales')
plt.ylabel('No of Sales')
plt.show()
