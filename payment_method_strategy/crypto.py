from payment_method_strategy.payment_method_Strategy import PaymentStrategy


class CryptoPayment(PaymentStrategy):
    def process_payment(self, order):
        return order.amount * 0.90 # 10% discount