#task 4 map() function 
prices=[100,250,400,1200,50]
prices_with_gst = list(map(lambda x: x+(x*18/100),prices))

print('Original List',prices)
print('Prices After GST',prices_with_gst)

