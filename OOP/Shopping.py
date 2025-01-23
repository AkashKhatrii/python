class Product:
    def __init__(self, product_id, name, description, price, stock):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"{quantity} units of '{self.name}' purchased. Remaining stock: {self.stock}.")
            return True
        else:
            print(f"Insufficient stock for '{self.name}'. Requested: {quantity}, Available: {self.stock}.")
            return False

    def is_in_stock(self, quantity):
        return self.stock >= quantity

    def __str__(self):
        """
        Return a string representation of the product.
        """
        return f"Product {self.product_id}: {self.name}, Price: ${self.price}, Stock: {self.stock}"


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = {}

    def add_item(self, product, quantity):
        if product.is_in_stock(quantity):
            if product in self.items:
                self.items[product] += quantity
            else:
                self.items[product] = quantity
            product.update_stock(quantity)
            print(f"Added {quantity} units of '{product.name}' to the cart.")
        else:
            print(f"Cannot add {quantity} units of '{product.name}' to the cart. Insufficient stock.")

    def remove_item(self, product):
        if product in self.items:
            removed_quantity = self.items.pop(product)
            product.stock += removed_quantity
            print(f"Removed {removed_quantity} units of '{product.name}' from the cart.")
        else:
            print(f"Product '{product.name}' is not in the cart.")

    def view_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for product, quantity in self.items.items():
                print(f"- {product.name}: {quantity} units, Price per unit: ${product.price:.2f}")
            print(f"Total Price: ${self.calculate_total():.2f}")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.items.items())
        return total

if __name__ == "__main__":
    # Create products
    laptop = Product(product_id=1, name="Laptop", description="High-performance laptop", price=999.99, stock=10)
    phone = Product(product_id=2, name="Smartphone", description="Latest model smartphone", price=699.99, stock=5)

    # Create a cart for a user
    cart = Cart(user_id=1)

    # Add items to the cart
    cart.add_item(laptop, 2)  # Add 2 laptops
    cart.add_item(phone, 1)   # Add 1 smartphone

    # View cart contents
    cart.view_cart()

    # Remove an item from the cart
    cart.remove_item(laptop)

    # View cart contents again
    cart.view_cart()
