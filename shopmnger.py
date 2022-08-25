"""
Modular code demonstration practice
We are going to import the shop module here and use its methods

"""

from shop import Salesperson 
from shop import Pants

pant_one=Pants('white','L',20,45)
pant_two=Pants('red','XL',20,50)

salesman1=Salesperson('Masila','David',1,35000)
salesman1.sell_pants(pant_one)
salesman1.sell_pants(pant_two)

salesman1.display_sales()

salesman1.calculate_sales()

salesman1.calculate_commission(20)