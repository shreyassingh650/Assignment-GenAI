#Task 7 Mini Use Case: Sales Analysis
import numpy as np
sales = np.array([1200,1500,900,2000,1800,1700,1600])

Total_weekly_sales = np.sum(sales)
Average_daily_sales = np.average(sales)
Highest_andlowest = np.array([np.max(sales),np.min(sales)])
Standarddeviation = np.std(sales)
lowsales = [x for x in sales if x<np.average(sales)]

print('Total Weekly Sales',Total_weekly_sales)
print('Average Daily Sales', Average_daily_sales)
print('High and low', Highest_andlowest)
print('Standard Deviation', Standarddeviation)
print('Sales above average', lowsales)