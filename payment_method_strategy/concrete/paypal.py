from payment_method_strategy.interface.payment_method_Strategy import PaymentStrategy


class PayPalPayment(PaymentStrategy):
    
    def process_payment(self, amount,email,password):
        # email="email"
        # password="pass"
        print(f"paid {amount} using paypal  ")