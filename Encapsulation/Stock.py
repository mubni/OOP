# Encapsulation is process of bundling data (attributes) and methods in a single unit
class Stock:
    #Constructing an instance(object) of a class
    def __init__(self, name, type, price):
        self.name = name
        self.type= type
        self.price = price

    #manually setting the name of stock
    def set_stockname(self, name):
        self.name= name

    #manually setting the type of the stock
    def set_stocktype(self, type):
        self.type= type

    #manually setting the stock price
    def set_stockprice(self, price):
        self.price= price
    
    #Increase in stock price
    def increase_stock_price(self):
        self.price = self.price *  2

    #decrease in stock price
    def decrease_stock_price(self):
        self.price= self.price / 2

    #printing the information of the Stock
    def __str__(self):
        print (f"The {self.name} stock which is of {self.type} type has a price of {self.price}")


#Creating an instance and applying methods to it    
Tech_stock= Stock("Microsoft", "Technology", 23 )
Tech_stock.__str__()
Tech_stock.set_stockname("Youtube")
Tech_stock.__str__()
Tech_stock.set_stockprice(40)
Tech_stock.__str__()
Tech_stock.set_stocktype("Online")
Tech_stock.__str__()
Tech_stock.increase_stock_price()
Tech_stock.__str__()
Tech_stock.decrease_stock_price()
Tech_stock.__str__()