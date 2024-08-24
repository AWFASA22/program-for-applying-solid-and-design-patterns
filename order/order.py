class Order:
    def __init__(self, amount, payment_strategy=None):
        self.amount = amount
        self.payment_strategy = payment_strategy

    def final_amount(self):
        if self.payment_strategy:
            return self.payment_strategy.process_payment(self)
        return self.amount
    
    def __repr__(self):
        return f"Order amount: ${self.amount}, Final amount after payment: ${self.final_amount()}"