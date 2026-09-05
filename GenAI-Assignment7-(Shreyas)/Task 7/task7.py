#Task 7 Mini Project
class Product:
    def __init__(self,name,price,category):
        self.name = name
        self.price = price
        self.category = category
    def get_info(self):
        print({self.name},'Name',{self.price},'Price',{self.category},'Category')
    def apply_discount(self,percent):
        return self.price-self.price*percent/100
    def __add__(self,other):
            return self.price + other.price
class Inventory:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def remove_product(self,name):
        for x in self.products:
             if x.name == name:
                self.products.remove(x)
                break
    def get_total_value(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    def show_all_products(self):
        for product in self.products:
            product.get_info()
class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")

        product = Product(name, price, category)
        self.inventory.add_product(product)

    def show_summary(self):
        print("Store:", self.store_name)
        print("Total Items:", len(self.inventory.products))
        print("Total Value:", self.inventory.get_total_value())
    
store = Store("Shreya Store")

store.add_new_product()
store.add_new_product()
store.add_new_product()

print("\n All Products ")
store.inventory.show_all_products()

print("\n Store Summary ")
store.show_summary()

print("\n Removing Product ")
store.inventory.remove_product("Laptop")

store.show_summary()

print("\n Operator Overloading ")
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Mouse", 1000, "Accessories")

print("Combined Price:", p1 + p2)