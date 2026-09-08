#task 4: Aggregation Operations
import numpy as np
data = np.array([[10,20,30],[40,50,60],[70,80,90]])

print('The Row Wise Sum')
print(np.sum(data,axis=1))
print('\nColumn Wise Sum')
print(np.sum(data,axis=0))
print(np.min(data),'Minimum Value')
print(np.max(data),'Maximum Value')
print(np.mean(data),'Mean Value')
