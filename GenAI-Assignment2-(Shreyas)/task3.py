#Task 3 
price_dict = {'mobile':3000,'headphone':4000.21,'charger':190.50,'pen':10.50,'book':150,'watch':975.00}

#small code block
price_dict['bag'] = 500.0
#update
price_dict.update({'mobile':5000})
#remove
del price_dict['headphone']

print(price_dict)

#average price
avg = sum(price_dict.values()) / len(price_dict.values())
print(avg)

#optional
max = max(price_dict.values()); min= min(price_dict.values())
print(max , min)