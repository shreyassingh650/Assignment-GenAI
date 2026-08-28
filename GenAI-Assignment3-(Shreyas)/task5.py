#task 5
prices = [100, 250, 400, 1200, 50, 2000, 850]
prices_greater_than_500 = list(filter(lambda x:x>500,prices))
prices_less_thaneq_500 = list(filter(lambda x:x<=500,prices))
print(f'Greater: {prices_greater_than_500}\nLess and Equal: {prices_less_thaneq_500}')