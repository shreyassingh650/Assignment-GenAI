#Task 1 Write Sales Records to a File
sales = [1200, 450, 980, 1500, 3000]
file_path = 'sales_data.txt' #file path

#write then close
sales_data = open(file_path,'w')
for s in sales:
    sales_data.write(str(s) + '\n')
sales_data.close()

#then open and read. used different type for learning purpose
with open(file_path,'r') as f:
    data = f.read()
    print(data)