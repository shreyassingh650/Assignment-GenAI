#task 4 
products = ['Mobile','TV','Laptops','Geyser','Charger','Light']
categories_set = {'electronics','cloths','furniture'}
price_dict = {'Mobile':3000,'headphone':4000.21,'charger':190.50,'pen':10.50,'book':150,'watch':975.00}

catalog = [('Mobile',4000,'electronics'),('Laptops',5000,'electronics'),('H&M',500,'cloths')]
category_to_products = {}
for products,price,category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(products)
print(category_to_products)
