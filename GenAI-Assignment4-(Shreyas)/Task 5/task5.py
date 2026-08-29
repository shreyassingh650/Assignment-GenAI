#task 5 Create Product Info File
ProductName = list()
Price = list()

while len(Price)<3:
    ProductName.append(input("Enter The Product Name: "))
    Price.append(input(f"Enter The Product Price: "))
    
with open('products.txt','w') as f:
    for x in range(0,3):
        f.write(ProductName[x]+ " | " + Price[x]+'\n')
        
with open('products.txt','r') as f:
    print(f.read())
