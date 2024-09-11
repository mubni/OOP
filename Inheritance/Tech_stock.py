from Stock import Stock

class Tech_stock(Stock):
    def __init__(self, name, price, Tech_type):
        super().__init__(name, price)
        self.Tech_type = Tech_type
    
    def set_Techtype(self, T):
        self.Tech_type = T
    
    def set_stockname(self, name):
        return super().set_stockname(name)
    
    def set_stockprice(self, price):
        return super().set_stockprice(price)
    
    
    def display_info(self):
        super().display_info()
        print(f"The Tech type of the company is {self.Tech_type}")

