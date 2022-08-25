class Clothing:
    def __init__(self, color, size, style, price):
        self.color=color,
        self.style=size,
        self.size=style,
        self.price=price

    def change_price(self, price):
        self.price = price 

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

    def describe(self):
        return f"a {self.color} {self.size} {self.style} {self.price}, cloth"

class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):
        super().__init__(color, size, style, price)
        self.long_or_short=long_or_short

    def double_price(self):
        self.price *= 2

    def describe(self):
        return super().describe()

class Pants(Clothing):
    """
    Inherit from the Clothing class
    1. in the __init__ method include parents attributes needed
    2. Include the new child class attribute in the _init__ method too.
    3. Inlude a super(). definition and include the parent class attributes
    """
    def __init__(self, color, size, style, price, waist): 
        super().__init__(color, size, style, price)
        self.waist=waist
    
    def calculate_discount(self, discount):
        return self.price * (1 - discount/2)