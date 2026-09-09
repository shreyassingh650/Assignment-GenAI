#Task 6: Percentiles & Sorting
import numpy as np
marks = np.array([78,85,90,66,72,88,95,60])
print(np.sort(marks))
print(np.percentile(marks,25))
print(np.percentile(marks,50))
print(np.percentile(marks,75))

count =0

for i in marks:
    avg = np.average(marks)
    if i>avg:
        count += 1
print('Student Who Scored Above The Average Marks',count)
