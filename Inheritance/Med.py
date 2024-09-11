from Stock import Stock

class medStock(Stock):
    def __init__(self, name, price, Drug_type):
        super().__init__(name, price)
        self.Drug_type= Drug_type

    def set_Drug_Type(self, Type):
        self.Drug_type= type

    def set_stockprice(self, price):
        return super().set_stockprice(price)
    
    def set_stockname(self, name):
        return super().set_stockname(name)
    
    def dispay_info(self):
        super().display_info()
        print(f"The drug type is {self.Drug_type}")