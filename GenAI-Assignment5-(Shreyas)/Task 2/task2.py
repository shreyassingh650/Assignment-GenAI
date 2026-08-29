#Task2 Read File in Different Ways
file_path = 'sales_data.txt' #file path

with open(file_path,'r') as f:
    print(f.read(),'--Read() Output\n')
    f.seek(0) # to reset cursor at starting point
    print(f.readline(),'--Readline()  First Line Output\n')
    f.seek(0)
    print(f.readlines(),'--Readlines() All Line Output\n')
    f.seek(0)
    list_of_int = list((int(x) for x in f.readlines()))
    
print(list_of_int,'--List of Integer')
