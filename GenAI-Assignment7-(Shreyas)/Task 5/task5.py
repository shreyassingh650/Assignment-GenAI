#task 5 Mini Program: Safe Shopping Cart
cart = [] # list 
total_bill = 0
while True:
    temp = input('Enter The Prices: \n')
    if temp=='q':
        break
    
    try:
        temp = float(temp)
        if temp<0:
            raise ValueError('Price is Negative')
        cart.append(temp)
        total_bill += temp
    except ValueError as ex1:
        print(ex1)
    except Exception as ex2:
        print(ex2)
print('Total Items', len(cart))
print('Total Bill', total_bill)