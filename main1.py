class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        self.items.append(FoodItem(name, price))
    
    def display_menu(self):
        print("Menu:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}. {item.name} - ${item.price:.2f}")

class Order:
    def __init__(self):
        self.order_items = []
    
    def add_item(self, food_item, quantity):
        self.order_items.append((food_item, quantity))
    
    def calculate_total(self):
        total = 0
        for item, quantity in self.order_items:
            total += item.price * quantity
        return total
    
    def display_order(self):
        print("Your Order:")
        for item, quantity in self.order_items:
            print(f"{item.name} x{quantity} - ${item.price * quantity:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

def main():
    menu = Menu()
    menu.add_item("Burger", 5.99)
    menu.add_item("Pizza", 8.99)
    menu.add_item("Soda", 1.99)
    
    order = Order()
    
    while True:
        menu.display_menu()
        
        try:
            choice = int(input("Enter the number of the item you want to order (0 to finish): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(menu.items):
                quantity = int(input(f"How many of the {menu.items[choice - 1].name} do you want? "))
                order.add_item(menu.items[choice - 1], quantity)
            else:
                print("Invalid choice. Please select a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    order.display_order()

if __name__ == "__main__":
    main()
