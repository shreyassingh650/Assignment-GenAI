#Task2 Recursive Function: factorial

def factorial(x):
    if(x<0):
        return 'Error Cant Be Negative'
    if(x==0 or x==1):
        return 1
    else:
        return (x*factorial(x-1))
    
print(factorial(5))
print(factorial(0))
print(factorial(-3))
