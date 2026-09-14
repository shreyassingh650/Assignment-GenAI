#task 1 Pandas Series Basics
import pandas as pd
marks = [78,85,90,66,72]
series = pd.Series(marks)
print(series)
print('The Index is:', series.index)
print('The Data Type is',series.dtype)

#Accessing Element
print('First Element', series[1])
print('Last two Element\n',series[:-3:-1])

