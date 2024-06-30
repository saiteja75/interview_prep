from .PaymentProcessor import PaymentProcessor

class CreditCardProcessor(PaymentProcessor):
    def __init__(self):
        pass
    
    def processPayment(self):
        print('Payment Processed through CreditCard')


cc = CreditCardProcessor()
cc.processPayment()
