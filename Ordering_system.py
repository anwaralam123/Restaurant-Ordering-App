import datetime

class MenuItem:
    def __init__(self, name, price, discount, preparation_time):
        self.name = name
        self.price = price
        self.discount = discount
        self.preparation_time = preparation_time

class Menu:
    def __init__(self):
        self.items = {
            'sandwich': MenuItem('sandwich', 10, '10% if 5 or more are ordered', 10),
            'salad': MenuItem('salad', 8, '10% if ordered with a Soup', 8),
            'soup': MenuItem('soup', 6, '20% ir ordered with Sandwich and Salad', 15),
            'coffee': MenuItem('coffee', 5, None, 5),
            'tea': MenuItem('tea', 5, None, 5)
        }

    def display_menu(self):
        print("+++++++++++++++++++++Menu+++++++++++++++++++++")
        for item in self.items.values():
            if item.discount:
                discount_info = f"\t Discount: {item.discount}"
            else:
                discount_info = f"\t Discount: N/A"
            print(f"{item.name}: Rs.{item.price}{discount_info}\t Preparation_time: {item.preparation_time} min")
        print()

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = {}
        self.total = 0
        self.max_preparation_time = 0

    def add_item(self, item_name, quantity, menu):
        if item_name in menu.items:
            if item_name in self.items:
                self.items[item_name] += quantity
            else:
                self.items[item_name] = quantity
        else:
            print("Item is not available yet. Choose from Menu..!")

    def calculate_total(self, menu):
        total = 0
        max_preparation_time = 0
        for item_name, qty in self.items.items():
            item = menu.items[item_name]
            discount = 0
            if item_name == 'sandwich' and qty >= 5:
                discount = 0.1
            elif item_name == 'salad' and 'soup' in self.items:
                discount = 0.1
            elif item_name == 'soup' and 'salad' in self.items and 'sandwich' in self.items:
                discount = 0.2

            discounted_price = item.price * (1 - discount) * qty
            total += discounted_price
            max_preparation_time += item.preparation_time

            print(f"{item_name}\t\t{qty}\t\t{discounted_price:.2f}")

        tax = 0.05
        tax_amount = tax * total
        total_with_tax = total + tax_amount

        self.total = total_with_tax
        self.max_preparation_time = max_preparation_time

        current_date_time = datetime.datetime.now()
        current_date = current_date_time.strftime("%d/%m/%y")
        order_ready_time = (current_date_time + datetime.timedelta(minutes=max_preparation_time)).strftime("%I:%M:%S %p")

        print(f"\nTax:\t\t{tax_amount:.2f}\nTotal:\t\t{total_with_tax:.2f}")
        print(f"\n<{current_date}> Your order will be ready in <{order_ready_time}>")

class RestaurantOrderingSystem:
    def __init__(self):
        self.menu = Menu()

    def take_order(self):
        print("\n++++++++ Ordering System For Restaurant ++++++++\n")
        customer_name = input("Please Enter Your Name: ")
        self.menu.display_menu()
        
        order = Order(customer_name)
        
        while True:
            ordered_item = input("Enter the name of item you want to order: ").lower()
            if ordered_item in self.menu.items:
                qty = int(input(f"Enter the Quantity for {ordered_item}: "))
                order.add_item(ordered_item, qty, self.menu)
            else:
                print("Item is not available yet. Choose from Menu..!")
            
            another_item = input("Do you want to add another order? (Yes/No): ").lower()
            if another_item != 'yes':
                break
        
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"\n{customer_name}, Thanks for your order\n")
        print("Items\t\tQty\t\tPrice")

        order.calculate_total(self.menu)

        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


order_system = RestaurantOrderingSystem()
order_system.take_order()