class CreditCardPayment():
    def process_payment(self, order):
        return order.amount * 1.02 # 2% fee