import csv

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item (
                
            )
        
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        


Item.instantiate_from_csv()

