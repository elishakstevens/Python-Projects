

from abc import ABC, abstractmethod

class house(ABC):
    #regular method
    def invoice(self, amount):
        print("Your final bill amount: $", amount)
#this function is telling us to pass in an argument but we won't
#   tell you how or what kind of data it will be - abstract method
    @abstractmethod
    def payment(self, amount, payAmt):
        pass

#child class of car()
class CashPayment(house):
    #defining implementation of parent's abstract method
    def payment(self, amount, payAmt):
        refund = int(payAmt) - int(amount)
        print('You paid $', payAmt)
        print('Refund Due: $', refund)
              
        

#object using parent and child methods
obj = CashPayment()
obj.invoice("425000")
obj.payment("425000", "425746")
