#task 6 Combined Utility Function
def process_prices(prices):
    discounted_prices = list(map(lambda x: x-(x*10/100),prices))
    filtered_prices = list(filter(lambda x: x>300,prices))
    return discounted_prices,filtered_prices
dprice, fprice = process_prices([100,500,900,50,750])
print(f'The discounted Price is {dprice}\nand The Filtered Price is {fprice}')