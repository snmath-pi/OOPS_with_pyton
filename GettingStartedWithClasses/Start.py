class Item:
    def calculate_total_price(self, x, y): #python always passes the instance of class in the method
        return x * y
        

item1 = Item() #creating an instance of the class
item1.name = "phone"
item1.price = 100
item1.quantity = 5

# print(type(Item)) # our own datatype

item2 = Item() #creating an instance of the class
item2.name = "laptop"
item2.price = 10000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))


