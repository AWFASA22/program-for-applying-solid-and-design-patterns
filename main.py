from order.order import Order
from payment_method_strategy.concrete.credit import CreditCardPayment
from payment_method_strategy.concrete.paypal import PayPalPayment
from payment_method_strategy.interface.payment_method_Strategy import PaymentStrategy


if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
  
    Order.set_payment_strategy(paypal)
    
    Order.make_payment(100)

