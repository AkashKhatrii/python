class Product():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self) -> str:
        return f"{self.name} {self.price} {self.category}"


class ShoppingCart():
    def __init__(self):
        self.products = []
    
    def add_product(self, product: Product):
        self.products.append(product)
    
    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)
    
    def calculate_total(self):
        return sum(product.price for product in self.products)
    
    def view_cart(self):
        if not self.products:
            print("Your cart is empty")
            return
        for product in self.products:
            print(product)
        print(f"Total: {self.calculate_total()}")

class User():
    def __init__(self, username) -> None:
        self.username = username
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product: Product):
        self.shopping_cart.add_product(product)
        print(f"{product.name} added to your cart.")
    
    def remove_from_cart(self, product: Product):
        self.shopping_cart.remove_product(product)
        print(f"{product.name} removed from your cart.")
    
    def view_cart(self):
        print(f"{self.username}'s cart:")
        self.shopping_cart.view_cart()
    
    def place_order(self):
        total = self.shopping_cart.calculate_total()
        print(f"{self.username}'s order total: {total}")
        self.shopping_cart = ShoppingCart()

laptop = Product("Laptop", 1000, "Electronics")
phone = Product("Phone", 500, "Electronics")

user = User("John Doe")

user.add_to_cart(laptop)
user.add_to_cart(phone)
user.view_cart()

user.remove_from_cart(phone)
user.view_cart()

user.place_order()
user.view_cart()
    
    


# cart = ShoppingCart()
# cart.add_product(laptop)
# cart.add_product(phone)
# cart.view_cart()

# print(laptop)
# print(phone)