tshirt_collection=[]
shirt_one={'color':'orange','size':'M','sleeve':'Short sleeve','price':60}
shirt_two={'color':'orange','size':'M','sleeve':'Short sleeve','price':60}
shirt_three={'color':'orange','size':'M','sleeve':'Short sleeve','price':60}

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)


print(tshirt_collection)

for shirts in tshirt_collection:
    print(f"color: {shirts.color}, waist_size: {shirts.waist_size}, length: {shirts.length}, price: {shirts.price}") 