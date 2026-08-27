#task 4 Loop Control with Conditions
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales =0
for a in daily:
    if a==0:
        continue
    elif a==-1:
        break
    else:
        total_sales += a
        print(f'current sales: {a} and total is : {total_sales}')
print(total_sales)

