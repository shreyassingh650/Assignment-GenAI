#task 1 : Basic Class & Object Creation
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print({self.name},'Name',{self.price},'Price',{self.category},'Category')
    def apply_discount(self,percent):
        return self.price-self.price*percent/100

obj1 = Product('Samsung',30000,'Electronics')
obj2 = Product('Book',500,'Stationary')
Product.get_info(obj1)
Product.get_info(obj2)
print(obj1.apply_discount(5))
        