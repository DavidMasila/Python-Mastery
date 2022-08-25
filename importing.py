from shirt import Shirt

new_shirt=Shirt('yellow','XXL','long sleeve',80)
yellow_shirt = Shirt('yellow','14','long sleeve', 20)

tshirt_collection=[]
shirt_one=Shirt('orange','M','Short sleeve',60)
shirt_two=Shirt('white','XL','long sleeve',40)
shirt_three=Shirt('Red','L','Short sleeve',60)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color)

new_shirt.change_price(50)
print(new_shirt.price)