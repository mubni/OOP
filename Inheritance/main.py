from Med import medStock
from Tech_stock import Tech_stock

TSt1= Tech_stock("abc", 50, "Mobile Phones")
TSt1.display_info()
TSt1.set_stockname("Apple")
TSt1.set_stockprice(52)
TSt1.display_info()

MSt1= medStock("pfizer", 41, "Operatinal drugs")
MSt1.dispay_info()
