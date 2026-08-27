#Task 3 User Menu

order_amount = list()


while True:
    t = input('1 — Add order amount to a running list\n2 Show all orders and totals after applying discounts\
\nq — Quit\n')
    if t=='1':
        order_amount.append(int(input('Enter Order Amount ')))
        continue
    elif t=='2':
        for order in order_amount:
            if order >= 2000:
                discount =15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            else:
                discount = 0
            final_amount = order - order*discount/100
            print(f'{order} Price {discount}% discount {final_amount}rs Final Amount')     
        continue
    elif t=='q':
        break
    else:
        print('Invalid Input')
        continue
    
        