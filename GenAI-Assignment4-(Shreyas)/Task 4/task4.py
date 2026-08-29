#task 4 Generate Summary

with open('sales_data.txt','r') as f:
    data = f.readlines()
    converted = [int(x) for x in data]
    
print('\nTotal Data',converted,'\n')
def calculation(converted):
    print('Total Sales: ', sum(converted))
    print('Highest Sales: ', max(converted))
    print('Lowest Sales: ', min(converted))
    print('Average Sales: ', sum(converted)/len(converted))
    
calculation(converted)

