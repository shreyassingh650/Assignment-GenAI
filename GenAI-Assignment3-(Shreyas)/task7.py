#Task 7
prices_list =[100,500,900,50,750]

#functions
def add_price(prices_list,price):
    prices_list.append(price)
    print('The New List Is: ',prices_list)
    
def get_average_price(prices_list):
    return sum(prices_list)/len(prices_list)

def get_max_price(prices_list):
    return max(prices_list)

while True:
    t = input('1 — Add Price\n2 Show Average Price\
    \n3 Show Highest Price\nq — Quit\n------------------\n')
    if t=='1':
        price = int(input('Enter The Price To Append in List: \n'))
        add_price(prices_list,price)
    elif t=='2':
        print('The Average Price is: ',get_average_price(prices_list))
    elif t=='3':
        print('The Highest Price is: ',get_max_price(prices_list))
    elif t=='q':
        break
    else:
        print('Invalid Input')
    continue