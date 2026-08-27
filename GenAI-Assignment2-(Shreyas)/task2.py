#2 process multiple orders
orders = [1200, 2500, 800, 1750, 3000]

temp = list()
for order_amount in orders:
    
    if order_amount >= 2000:
        temp.append([(order_amount-order_amount*(15/100)),15])
    elif order_amount>= 1500:
        temp.append([(order_amount-order_amount*(10/100)),10])
    elif order_amount>= 1000:
       temp.append([(order_amount-order_amount*(7/100)),7])
    else:
        temp.append([(order_amount),0])

t=0 # for total revenue
for (x,y),order_amount in zip(temp,orders):
        print(f'order amount: {order_amount} discount: {y}% final amount: {x}')
        t += x
print(f'Total Revenue: {t}')

    
    