class Stock:
    #Constructing an instance(object) of a class
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #manually setting the name of stock
    def set_stockname(self, name):
        self.name= name

    #manually setting the stock price
    def set_stockprice(self, price):
        self.price= price

    #printing the information of the Stock
    def display_info(self):
        print (f"The {self.name} stock has a price of {self.price}")
  