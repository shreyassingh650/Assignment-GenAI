#Task 1 Product Category

products = ['Mobile','TV','Laptops','Geyser','Charger','Light']
sample_product = ('Mobile','20000','Electronics')

print(products[1],products[-1])

products.extend(['Bed','Pillow'])
print(products)

#optional
temp_list = list(sample_product)
temp_list[1] = '30000'
sample_product = tuple(temp_list)

print(sample_product)



