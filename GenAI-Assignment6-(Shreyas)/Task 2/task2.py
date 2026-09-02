#task 2 Bill Calculate with Error Handling
prices = [120,350,'abc',500,-200,800]
total =0
for x in prices:
    try:
        if not isinstance(x,(int,float)):
            raise TypeError(x,'Only Number is Allowed\n')
        if x<1:
            raise ValueError(x,'Negative Price Not Allowed\n')
        total+=x
    except TypeError as ex1:
        print(ex1)
    except ValueError as ex2:
        print(ex2)
        
print('Final Amount is: ',total)