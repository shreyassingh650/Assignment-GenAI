#Task 3  Append New Sales
file_path = 'sales_data.txt' #file path

with open(file_path,'a') as f:
    f.writelines(['5000\n','2500\n','1700\n'])

with open(file_path,'r') as f:
    print(f.read())
    f.seek(0)
    #optional
    print('\nTotal Length: ',len(f.readlines()))
        