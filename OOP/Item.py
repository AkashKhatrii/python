class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"item: {self.name}, {self.price}")
    
class RegularItem(Item):
    def apply_discount(self, percentage):
        new_amount =  self.price - (percentage * self.price) / 100
        self.price = new_amount

class PremiumItem(Item):
    def apply_discount(self, percentage):
        new_percentage = percentage + 5
        self.price -= (self.price * new_percentage) / 100

class ShoppingCart():
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def display_cart(self):
        for item in self.items:
            item.display_info()
    
    def total_price(self):
        total = sum(item.price for item in self.items)
        return total
    
item1 = RegularItem('Laptop', 1000)
item2 = PremiumItem('SmartPhone', 1000)

cart = ShoppingCart()
cart.add_item(item1)
cart.add_item(item2)

cart.display_cart()
print("Toal cart price: ", cart.total_price())

item1.apply_discount(10)
item2.apply_discount(10)

cart.display_cart()
print("Toal cart price: ", cart.total_price())
