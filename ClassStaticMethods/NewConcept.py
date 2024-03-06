class Item:
    pay_rate = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity: float):
        #run all validations
        assert price >= 0, f"Price {price} can't be negative!"

        #assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)
        
    
    def total_pay_price(self):
        return self.price * self.quantity;
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate #using Item gives for item but self changes it 

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        
item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

print(Item.all)

