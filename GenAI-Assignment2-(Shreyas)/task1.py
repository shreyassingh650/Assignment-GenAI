#Task 1 Discount Rules
order_amount = int(input('Enter the Number:'))
# if user gave wrong input it will cause error
if order_amount >= 2000:
    print(order_amount-order_amount*(15/100))
elif order_amount>= 1500 and order_amount<2000:
    print(order_amount-order_amount*(10/100))
elif order_amount>= 1000 and order_amount<1500:
    print(order_amount-order_amount*(7/100))
else:
    print(order_amount)


