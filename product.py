from os import system

class Product:
    products = {}
    product_id = 0
    def __init__(self, name, price, category):
        Product.product_id += 1
        self.id = Product.product_id
        self.name = name
        self.price = price
        self.category = category

    def view_products():
        system('clear')
        print("\nProduct Catalog: \n")
        for id, product in Product.products.items():
            print(f"Product ID: {id}, Description: {product.name}, Price: {product.price:.2f}, Category: {Category.categories[product.category].name}")
        input("\nEnter to continue: ")

    def add_product():
        # select a category first
        # display a list of categories to select from
        system('clear')
        print("\nProduct Catagories: \n")
        for id, category in Category.categories.items():
            print(f"Category ID: {id}, Description: {category.name}")
        while True:
            try:
                selection = int(input("\nSelect a category: "))
                if selection == 0:
                    break
                if selection in Category.categories.keys():
                    print(f"\nAdd a product in the {Category.categories[selection].name} Category: ")
                    name = ''
                    while name.strip() == '':
                        name = input("\nProduct Description: ").strip().capitalize()
                        if name.lower() == "exit":
                            return
                        if name.strip() == '':
                            print("\nPlease enter a description or 'Exit' to exit without adding a product.")
                    price = Product.get_price()
                    new_product = Product(name, price, selection)
                    Product.products[new_product.id] = new_product
                    print(f"\nProduct added. Description: {name}, Price: {price:.2f}.")
                    input("\nEnter to continue: ")
                    break
                else:
                    print("\nPlease select a category from the list or 0 to exit.")
            except ValueError:
                print("\nPlease select a category from the list or 0 to exit.")

    def get_price():
        while True:
            try:
                price_input = input("\nPrice: ")
                price = float(price_input)
                if price < 0:
                    print("\nPrice cannot be less than zero.")
                    continue
                return price
            except ValueError:
                print("\nPrice must be a number.")

    def update_product():
        system('clear')
        print("\nProduct Catalog: \n")
        for id, product in Product.products.items():
            print(f"Product ID: {id}, Description: {product.name}, Price: {product.price:.2f}, Category: {Category.categories[product.category].name}")
        while True:
            try:
                selection = int(input("\nSelect a product: "))
                if selection == 0:
                    break
                if selection in Product.products.keys():
                    product = Product.products[selection]
                    print(f"\nProduct selected: {product.name}")
                    choice = ''
                    while choice.lower() not in ['d', 'p', 'b', 'x']:
                        choice = input("\nSelect 'D' to update the product Description, 'P' to update the price, 'B' to update both, or 'X' to exit: ")
                        if choice.lower() == 'x':
                            break
                        if choice.lower() in ['d', 'b']:
                            name = input("\nEnter a new product description: ")
                            if name.strip() != '':
                                product.name = name.strip().capitalize()
                        if choice.lower() in ['p', 'b']:
                            price = Product.get_price()
                            product.price = price
                        print(f"\nProduct updated: {product.name}, Price: {product.price:.2f}")
                        input("\nEnter to continue: ")
                    return
                else:
                    print("\nPlease select a product from the list or 0 to exit.")
            except ValueError:
                print("\nPlease select a product from the list or 0 to exit.")

    def delete_product():
        system('clear')
        print("\nProduct Catalog: \n")
        for id, product in Product.products.items():
            print(f"Product ID: {id}, Description: {product.name}, Price: {product.price:.2f}, Category: {Category.categories[product.category].name}")
        while True:
            try:
                selection = int(input("\nSelect a product to delete: "))
                if selection == 0:
                    break
                if selection in Product.products.keys():
                    product = Product.products[selection]
                    print(f"\nProduct selected: {product.name}")
                    choice = ''
                    while choice.lower() not in ['d', 'x']:
                        choice = input("\nSelect 'D' to confirm delete, or 'X' to exit: ")
                        if choice.lower() == 'x':
                            break
                        if choice.lower() == 'd':
                            print(f"\nProduct deleted: {product.name}")
                            del Product.products[product.id]
                            input("\nEnter to continue: ")
                    return
                else:
                    print("\nPlease select a product from the list or 0 to exit.")
            except ValueError:
                print("\nPlease select a product from the list or 0 to exit.")
        return

class Category:
    categories = {}
    category_id = 0
    def __init__(self, name):
        Category.category_id += 1
        self.id = Category.category_id
        self.name = name

    def view_categories():
        system('clear')
        print("\nProduct Catagories: \n")
        for id, category in Category.categories.items():
            print(f"Category ID: {id}, Description: {category.name}")
        input("\nEnter to continue: ")

    def add_category():
        system('clear')
        print("\nAdd a Product Category: \n")
        name = ''
        while name.strip() == '':
            name = input("\nCategory Description: ").strip().capitalize()
            if name.lower() == "exit":
                return
            if name.strip() == '':
                print("\nPlease enter a description or 'Exit' to exit without adding a category.")
        new_category = Category(name)
        Category.categories[new_category.id] = new_category
        print(f"\nCategory added. Description: {name}")
        input("\nEnter to continue: ")

    def delete_category():
        system('clear')
        print("\nDelete a Product Category: \n")
        for id, category in Category.categories.items():
            print(f"Category ID: {id}, Description: {category.name}")
        while True:
            try:
                selection = int(input("\nSelect a category to delete: "))
                if selection == 0:
                    break
                if selection in Category.categories.keys():
                    category = Category.categories[selection]
                    print(f"\nCategory selected: {category.name}")
                    choice = ''
                    while choice.lower() not in ['d', 'x']:
                        choice = input("\nSelect 'D' to confirm delete, or 'X' to exit: ")
                        if choice.lower() == 'x':
                            break
                        if choice.lower() == 'd':
                            product_keys = list(Product.products.keys())
                            for product in product_keys:
                                if Product.products[product].category == selection:
                                    del Product.products[product]
                            del Category.categories[category.id]
                            print(f"\nCategory deleted: {category.name}")
                            input("\nEnter to continue: ")
                    return
                else:
                    print("\nPlease select a category from the list or 0 to exit.")
            except ValueError:
                print("\nPlease select a category from the list or 0 to exit.")
