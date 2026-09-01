#Main.py
import math_utils
from math_utils import square

from string_utils import *

import shop_package.discount as disc
from shop_package.billing import calculate_total
import shop_package.billing
#task 1
print(math_utils.add(5,6))
print(math_utils.subtract(5,1))
print(square(4),'\n') 

#task2
print(capitalize_words('Approve The Assignment'))
print(reverse_string('Approve The Assignment'))
print(word_count('Approve The Assignment'),'\n')

#task 4
print(disc.apply_discount(1000,10))
print(disc.flat_discount(1000))
print(calculate_total([100,200,300]))
print(shop_package.billing.apply_tax(100))



