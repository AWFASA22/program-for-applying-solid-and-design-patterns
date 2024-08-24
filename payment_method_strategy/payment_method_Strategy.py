from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, order):
        pass