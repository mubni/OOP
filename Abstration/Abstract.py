from abc import ABC, abstractmethod

class Stock(ABC):
    @abstractmethod
    def IncreaseStock(self):
        pass
    
class tech_stock(Stock):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def IncreaseStock(self):
        self.price = self.price *2

    def display_info(self):
        print(f"{self.name} has an stock of price {self.price}")
    
obj1= tech_stock("S21 ultra", 22)
obj1.display_info()
obj1.IncreaseStock()
obj1.display_info()