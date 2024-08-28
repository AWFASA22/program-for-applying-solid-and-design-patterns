from payment_method_strategy.card import Card
from payment_method_strategy.interface.payment_method_Strategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        card= Card("cardnumber","expiredate","cvv")    
        print(f"paid {amount} using credit card")