import os
from product import Product, Category

class User:
    users = {} # Simulated database for users

    def __init__(self, name, password, type="shopper"):
        self.name = name
        self.password = password
        self.type = type

    def login():
        name = input(f"\nEnter your name: ")
        password = input("Enter your password: ")
        if name in User.users.keys() and User.users[name].password == password:
            print(f"\nLogin successful")
            input("\nEnter to continue: ")
            return User.users[name]
        else:
            print(f"\nInvalid Credentials")

    def register():
        name = input(f"\nEnter your name: ")
        if name in User.users.keys():
            print("That name is already registered. Please log in or register with another name.")
            return
        password = input("Enter your password: ")
        User.users[name] = Shopper(name, password)
        print(f"\nRegistration successful")
        input("\nEnter to continue: ")

    def view_users():
        os.system('clear')
        print("\nRegistered Users: \n")
        for name in User.users.keys():
            print(f"User name: {name}, Password: {User.users[name].password}, Type: {User.users[name].type}") # for testing only
            if User.users[name].type != 'admin':
                keys = list(User.users[name].shopping_cart.keys())
                for id in keys:
                    if id not in Product.products.keys():
                        del User.users[name].shopping_cart[id]
                print(f"  Shopping cart for {name}:")
                total = 0
                for id in User.users[name].shopping_cart.keys():
                    print(f"    Product ID: #{Product.products[id].id}, {Product.products[id].name}, Quantity: {User.users[name].shopping_cart[id]} at ${Product.products[id].price:.2f}, Subtotal = ${(Product.products[id].price * User.users[name].shopping_cart[id]):.2f}")
                    total += Product.products[id].price * User.users[name].shopping_cart[id]
                print(f"\n  Total: ${total:.2f}\n")
        input("\nEnter to continue: ")

class Shopper(User):
    def __init__(self, name, password):
        super().__init__(name, password)
        self.shopping_cart = {}  # Only shoppers have carts

    def add_to_cart(user):
        os.system('clear')
        print("\nProduct Catalog: \n")
        for id, product in Product.products.items():
            print(f"Product ID: {id}, Description: {product.name}, Price: {product.price:.2f}, Category: {Category.categories[product.category].name}")
        while True:
            try:
                selection = int(input("\nSelect a product to add to the cart: "))
                if selection == 0:
                    break
                if selection in Product.products.keys():
                    product = Product.products[selection]
                    print(f"Product selected: {product.name}")
                    qty = int(input("Quantity to add: "))
                    if qty > 0:
                        if product.id in user.shopping_cart:
                            user.shopping_cart[product.id] += qty
                        else:
                            user.shopping_cart[product.id] = qty
                        print(f"\n {qty} of {product.name} added to cart at ${Product.products[product.id].price:.2f}, Subtotal = ${(Product.products[product.id].price * user.shopping_cart[product.id]):.2f}")
                        input("\nEnter to continue: ")
                    break
                else:
                    print("\nPlease select a product from the list or 0 to exit.")
            except ValueError:
                print("\nPlease select a valid number or 0 to exit.")

    def view_cart(user):
        os.system('clear')
        # check if a product in the catalog has been removed since the cart was saved
        keys = list(user.shopping_cart.keys())
        key_removed = False
        for id in keys:
            if id not in Product.products.keys():
                del user.shopping_cart[id]
                key_removed = True
        if key_removed:
            print("An item has been removed from your cart as it is no longer in the catalog.")
            input("\nEnter to continue: ")
        if not user.shopping_cart:
            print("\nYour cart is empty.")
            input("\nEnter to continue: ")
            return
        total = 0
        print("\nItems in your shopping cart:\n")
        for id in user.shopping_cart.keys():
            print(f"Product ID: #{Product.products[id].id}, {Product.products[id].name}, Quantity: {user.shopping_cart[id]} at ${Product.products[id].price:.2f}, Subtotal = ${(Product.products[id].price * user.shopping_cart[id]):.2f}")
            total += Product.products[id].price * user.shopping_cart[id]
        print(f"\nTotal: ${total:.2f}")
        input("\nEnter to continue: ")

    def adjust_cart(user):
        os.system('clear')
        if not user.shopping_cart:
            print("\nYour cart is empty.")
            input("\nEnter to continue: ")
            return
        print("\nItems in your shopping cart:\n")
        for id in user.shopping_cart.keys():
            print(f"Product ID #{Product.products[id].id}, {Product.products[id].name}, Quantity: {user.shopping_cart[id]} at ${Product.products[id].price:.2f} = ${(Product.products[id].price * user.shopping_cart[id]):.2f}")
        while True:
            try:
                selection = int(input("\nEnter the product ID # of an item to adjust the quantity: "))
                if selection == 0:
                    break
                if selection in user.shopping_cart.keys():
                    product = Product.products[selection]
                    print(f"\nProduct selected: {product.name}")
                    qty = int(input("\nQuantity to remove: "))
                    if product.id in user.shopping_cart:
                        user.shopping_cart[product.id] -= qty
                        if user.shopping_cart[product.id] <= 0:
                            del user.shopping_cart[product.id]
                            print(f"\n{product.name} has been removed from your cart.")
                        else:
                            print(f"\nThe quantity of {product.name} has been adjusted in your cart.")
                        input("\nEnter to continue: ")
                    break
                else:
                    print("\nPlease select a product from the list or 0 to exit.")
            except ValueError:
                print("\nPlease select a valid number or 0 to exit.")

    def checkout(user):
        os.system('clear')
        if not user.shopping_cart:
            print("\nYour cart is empty.")
            input("\nEnter to continue: ")
            return
        total = 0
        print("\nItems in your shopping cart:\n")
        for id in user.shopping_cart.keys():
            print(f"Product ID: #{Product.products[id].id}, {Product.products[id].name}, Quantity: {user.shopping_cart[id]} at ${Product.products[id].price:.2f}, Subtotal = ${(Product.products[id].price * user.shopping_cart[id]):.2f}")
            total += Product.products[id].price * user.shopping_cart[id]
        print(f"\nTotal: ${total:.2f}")
        checkout = input("\nProceed with checkout? y/n: ").strip().lower()
        if checkout != 'y':
            print("\nYour order has not been placed.")
            input("\nEnter to continue: ")
            return
        checkout = input("\nSelect a payment method 1. PayPal, 2. Credit Card, 3. Debit Card: ").strip().lower()
        if checkout not in ['1', '2', '3']:
            print("\nThat is not a valid payment method. Your order has not been placed.")
            input("\nEnter to continue: ")
            return
        print("\nYour order has been placed. Thanks for shopping with us!")
        user.shopping_cart.clear()
        input("\nEnter to continue: ")

class Admin(User):
    def __init__(self, name, password):
        super().__init__(name, password, type="admin")
