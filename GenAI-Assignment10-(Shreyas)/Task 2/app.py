#task 2 Math Operations on Series
import pandas as pd
marks = [78,85,90,66,72]
series = pd.Series(marks)
#adding 5 grace marks to all student
series += 5
print('5 Marks added',series)

#using on same series cuz question doesnot say to not modify the existing one 

#Sub 2 marks from all values
series -= 2
print('2 marks sub',series)
# multiply all marks by 1.05
series *= 1.05
print('multiply',series)
#divide all by 2
series /=2
print('Divibe by 2',series)