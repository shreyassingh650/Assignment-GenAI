#task 6 Magic Method & Operator Overloading
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print({self.name},'Name',{self.price},'Price',{self.category},'Category')
    def apply_discount(self,percent):
        return self.price-self.price*percent/100
    def __str__(self):
        return f'Product({self.name},{self.price},{self.category})'
    def __add__(self,other):
        return f'The Total Combined Price: {self.price + other.price}'

p1=Product('Lamp',100,'Study')
p2=Product('Watch',500,'Wearable')
p3 = p1+p2
print(p1)
print(p3)