#task 5 Abstraction (Using Abstract Base Class)
from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(amount):
        pass
class CreditCardPayment(Payment):
    def process_payment(self,amount):
        print('This is Credit Card Amount',amount)
class UPIPayment(Payment):
    def process_payment(self,amount):
        print('This is UPI Amount',amount)

#Test all classes
c1 = CreditCardPayment()
upi = UPIPayment()
c1.process_payment(30000)
upi.process_payment(199)
