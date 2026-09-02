num= int(input('Enter Numerator: '))
den= int(input('Enter Denominator: '))
try:
    result = num/den
except ValueError as ex1:
    print(ex1)
except ZeroDivisionError as ex2:
    print(ex2)
else:
    print('The Result is ',result)
finally:
    print('Operation Completed')