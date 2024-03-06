class Item:
    
    pay_rate = 0.8 # this is a class attribute 
    def __init__(self, name: str, age: float) -> None:
        #run validations
        
        assert age >=16, f"age {age} is not greater than 16!"
        #assign to self object
        self.name = name
        self.age = age
        
    def total_price(self):
        return self.name * self.age
    
item1 = Item('A', 21)
print(item1.name)
print(item1.age)
print(item1.total_price())
item1.has_numpad = False

print(Item.pay_rate)
print(item1.pay_rate)

print(Item.__dict__) #all the attributes for the class level
print(item1.__dict__) # all attributes for the instances
