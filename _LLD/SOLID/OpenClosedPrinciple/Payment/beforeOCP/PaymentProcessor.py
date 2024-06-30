''' 
Imagine you have a class called PaymentProcessor that handles payments for your e-commerce 
application. Initially, it only supports credit card payments:

'''

# PaymentProcessor only supports creditcard payments
class PaymentProcessor:
    def __init__(self):
        pass
    
    def processCreditCard(self):
        pass


# later you wanted to support paypal payments
# you need modify the existing class to implement it
# VOILATING OPEN/CLOSED Principle
class PaymentProcessor:
    def __init__(self):
        pass
    
    def processCreditCard(self):
        pass
    
    def processPayPal(self):
        pass