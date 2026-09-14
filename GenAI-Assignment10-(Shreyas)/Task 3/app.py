#task 3 Python Functionalities on Series
import pandas as pd
marks = [78,85,90,66,72]
series = pd.Series(marks)

print(max(series))
print(min(series))
print(sum(series))
print(series.mean())

# apply lamdba to check passing >=70
passing_check = lambda a:a>=70

print(series.apply(passing_check))
print(sum(passing_check(series)))

