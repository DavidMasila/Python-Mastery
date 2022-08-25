
class Pants:
    def __init__(self, color, waist_size, length, price):
        self.color=color
        self.waist_size=waist_size
        self.length=length
        self.price=price

    def change_price(self, new_price):
        self.price = new_price

    def discount_given(self, discount):
        return self.price * (1 - discount)

class Salesperson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name=first_name
        self.last_name=last_name
        self.id=employee_id
        self.salary=salary
        self.pants_sold= []
        self.total_sales=0

    def sell_pants(self, pants):
        self.pants_sold.append(pants)
    
    def display_sales (self):
        #y will represent the list to write less
        y=self.pants_sold
        for i in range(len(y)):
            print(f"color: {y[i].color}, waist_size: {y[i].waist_size}, length: {y[i].length}, price: {y[i].price}")
    
    def calculate_sales(self):
        y=self.pants_sold
        for i in range(len(y)):
            self.total_sales += self.pants_sold[i].price

        print(f"\n{self.first_name} made {self.total_sales} dollars in sales")
    
    def calculate_commission(self, percentage):
        commission = percentage/100 * self.total_sales
        print(f"{self.first_name} made {commission} commision in sales")

