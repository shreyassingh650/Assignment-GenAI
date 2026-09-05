#task 4 Polymorphism
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print({self.name},'Name',{self.price},'Price',{self.category},'Category')
    def apply_discount(self,percent):
        return self.price-self.price*percent/100
class Laptop(Product):
    def get_info(self):
        print({self.name},'The Laptop Name will be only Visible')
class Mobile(Product):
    def get_info(self):
        print({self.name},'The Laptop Name will be only Visible')
laptop1 = Laptop('Acer',2000,'Electronics')
Mobile1 = Mobile('Iphone',2030,'Electronics')
Products = [laptop1,Mobile1] # polymorphism 
for x in Products:
    x.get_info()