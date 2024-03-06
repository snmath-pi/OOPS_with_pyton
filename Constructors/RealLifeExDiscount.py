class Item:
    pay_rate = 0.8
    
    def __init__(self, name: str, price: float, quantity: float):
        assert price >= 0, f"Price {price} can't be negative!"
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_pay_price(self):
        return self.price * self.quantity;
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate #using Item gives for item but self changes it 
        
        
item1 = Item('Laptop', 1000, 5)

item1.apply_discount();
print(item1.price)

item2 = Item('Mobile', 500, 1)
item2.pay_rate = 0.5
item2.apply_discount()

print(item2.price)

