#task 3 inheritance
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print({self.name},'Name',{self.price},'Price',{self.category},'Category')
    def apply_discount(self,percent):
        return self.price-self.price*percent/100
class ElectronicProduct(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, price, category)
        self.warranty_years = warranty_years
    def get_info(self):
        print({self.name},'Name',{self.price},'Price',{self.category},'Category',{self.warranty_years},'Warrenty')

#Demonstrate
p1 = Product('iphone',10000,'Electronics')
ep = ElectronicProduct('Washing Machine',10500,'Electronics','10 Years')
p1.get_info()
ep.get_info() #overriding