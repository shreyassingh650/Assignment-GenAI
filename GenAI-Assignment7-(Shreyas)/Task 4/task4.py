#task 4 File Reader with Exception Handling
file_name = input('Enter File Name: ')

try:
    with open(file_name,'r') as f:
        pass
except FileNotFoundError as ex1:
    print(ex1)
except PermissionError as ex2:
    print(ex2)
else:
    with open(file_name,'r') as f:
        for x in range(3):
            print(f.readline())
finally:
    print('File Operation attempted.')
        