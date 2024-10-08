''' 
Imagine you have a class called PaymentProcessor that handles payments for your e-commerce 
application. Initially, it only supports credit card payments:

'''
from abc import ABC,abstractmethod 

class PaymentProcessor(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def processPayment(self):
        pass
        