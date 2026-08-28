#Task 1 Price After Discount
def apply_discount(price, discount_percent=5):
    if discount_percent>60: #optional
        return 'discount cant exceed above 60'
    return (price - (price*discount_percent/100))

print(apply_discount(500,61))

