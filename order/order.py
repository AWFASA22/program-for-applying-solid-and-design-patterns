
class Order:
    def __init__(self, PaymentStrategy):
        self.PaymentStrategy = PaymentStrategy

    def set_payment_strategy(self, PaymentStrategy):
        self.PaymentStrategy = PaymentStrategy
    
    def make_payment(self, amount):
        self.PaymentStrategy.process_payment(amount)
