#Task 7 Mini Project - Export Discounted Prices
prices = {
    'Mouse':500,
    'Keyboard':800,
    'Monitor':7000,
    'Pendrive':400,
    'Camera': 5000
}
discount = int(input('Tell Discount Percentage%'))
dis_list = list()
with open('discount_report.txt','w') as f:
    f.write("Product | Original Price | Discounted Price\n")
    for x,y in prices.items():
        dis = y-y*discount/100
        f.write(x +" | " + str(y) +" | " + str(dis)+"\n")
        dis_list.append(dis)
        
        
        
#optional
with open('discount_report.txt','a') as f:
    TotalItems = len(prices)
    AverageDiscountedPrice = sum(dis_list)/len(dis_list)
    f.writelines([f'Total Items: {TotalItems}\n',f'A. Discounted Price: {AverageDiscountedPrice}'])

with open('discount_report.txt','r') as f:
    print(f.read())
    
    