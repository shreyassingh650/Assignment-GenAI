#task 5 Statistical Operations
import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])

print('Mean', np.mean(marks))
print('Median', np.median(marks))
print('Variance', np.var(marks))
print('Standard Deviation', np.std(marks))
print('Min and Max', np.min(marks),np.max(marks))
print('Range Max-Min', np.max(marks)-np.min(marks))