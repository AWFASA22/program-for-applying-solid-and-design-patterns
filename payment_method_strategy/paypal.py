from payment_method_strategy.payment_method_Strategy import PaymentStrategy


class PayPalPayment(PaymentStrategy):
    def process_payment(self, order):
        return order.amount + 5 # Flat $5 fee