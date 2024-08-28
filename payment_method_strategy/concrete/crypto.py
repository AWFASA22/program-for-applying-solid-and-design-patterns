from payment_method_strategy.interface.payment_method_Strategy import PaymentStrategy


class CryptoPayment(PaymentStrategy):
    def process_payment(self, amount):
        print(f"paid {amount} using crypto")