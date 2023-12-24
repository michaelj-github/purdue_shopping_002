import os
from user import User, Admin, Shopper
from product import Product, Category

def main_menu():
    """
    Display the main menu

    """
    os.system('clear') # Clear screen for Ubuntu
    print("Initialization in progress ...")
    print("\nAn Admin account has been created.")
    print("Items are being added to the database.")
    for id, category in Category.categories.items():
        print(f"Category ID: {id}, Description: {category.name}")
    for id, product in Product.products.items():
        print(f"Product ID: {id}, Description: {product.name}, Price: {product.price:.2f}, Category: {Category.categories[product.category].name}")
    print("\n... Initialization completed.")
    input("\nEnter to continue: ")

    # display the main menu, register, login, or exit
    while True:
        os.system('clear')
        print("\n\nWelcome to the Marketplace")
        print(f"\n1. Login")
        print(f"2. Register")
        print(f"3. Exit")
        selection = input(f"\nMake a selection: ")
        if selection == '1':
            user = User.login()
            if user:
                if user.type == 'admin':
                    admin_menu()
                elif (user.type == 'shopper'):
                    shopper_menu(user)
        elif selection == '2':
            User.register()
        elif selection == '3':
            os.system('clear')
            print("\nThank you for using the Marketplace.\n\n")
            break

def admin_menu():
    """
    Display the admin menu

    """
    while True:
        os.system('clear')
        print("\nAdmin Menu\n")
        print("1. View Product Catalog")
        print("2. Add New Product")
        print("3. Update Existing Product")
        print("4. Delete Product")
        print("5. View Categories")
        print("6. Add New Category")
        print("7. Delete Category")
        print("8. View User Accounts")
        print("9. Log out and return to main menu")
        selection = input(f"\nMake a selection: ")
        if selection == '1':
            Product.view_products()
        elif selection == '2':
            Product.add_product()
        elif selection == '3':
            Product.update_product()
        elif selection == '4':
            Product.delete_product()
        elif selection == '5':
            Category.view_categories()
        elif selection == '6':
            Category.add_category()
        elif selection == '7':
            Category.delete_category()
        elif selection == '8':
            User.view_users()
        elif selection == '9':
            break
        else:
            print("\nInvalid selection")
            input("\nEnter to continue: ")

def shopper_menu(user):
    """
    Display the shopper menu

    """
    while True:
        os.system('clear')
        print("\nMenu\n")
        print("1. View Product Catalog")
        print("2. Add an item to your cart")
        print("3. View your cart")
        print("4. Remove an item from your cart or adjust the quantity")
        print("5. Checkout")
        print("6. Log out")
        selection = input(f"\nMake a selection: ")
        if selection == '1':
            Product.view_products()
        elif selection == '2':
            Shopper.add_to_cart(user)
        elif selection == '3':
            Shopper.view_cart(user)
        elif selection == '4':
            Shopper.adjust_cart(user)
        elif selection == '5':
            Shopper.checkout(user)
        elif selection == '6':
            break
        else:
            print("\nInvalid selection")
            input("\nEnter to continue: ")


# initialize starting data items for admin, categories, and products
User.users['admin'] = Admin('admin', 'password')
User.users['michael'] = Shopper('michael', 'password')
User.users['a'] = Admin('a', 'a') # for ease of testing use 'a', 'a'
Category.categories[1] = Category('Electronics')
Category.categories[2] = Category('Clothing')
Category.categories[3] = Category('Footwear')
Product.products[1] = Product('Laptop', 1000, 1)
Product.products[2] = Product('Jacket', 99, 2)
Product.products[3] = Product('Boots', 19.99, 3)

main_menu()
