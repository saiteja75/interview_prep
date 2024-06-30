from .PaymentProcessor import PaymentProcessor



class PayPalProcessor(PaymentProcessor):
    def __init__(self):
        pass
    
    def processPayment(self):
        print('Payment Processed through paypal')
        