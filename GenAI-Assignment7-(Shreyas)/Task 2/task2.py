#task 2 Constructor and Encapsulation
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.__price = price
        self.category = category
    def get_price(self):
        return self.__price
    def set_price(self,new_price):
        if new_price >0:
            self.__price = new_price
#create geter and setter
p1 = Product('iphone',10000,'Electronics')
p1.set_price(10)
print(p1.get_price())