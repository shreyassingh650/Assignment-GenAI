#task 3
def check_age(age):
    try:
        if(age<1 or age>120):
            raise ValueError('Age Must be between 1 and 120')
        print('Age is Valid')
    except ValueError as ex1:
        print('Invalid Age', ex1)

age = int(input('Enter Age: '))
check_age(age)
