class InventoryItem():

    def __init__(self, item_id, item_name, price, quantity):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
      

    def calculate_value(self):
        return self.price * self.quantity
    
    def str(self):
        return f"{self.item_id} {self.item_name} ${self.price} {self.quantity}"
    
    class discountedItem():
        def __init__(self, item_id, item_name, price, quantity, discount):
            super().__init__(item_id, item_name, price, quantity)
            self.discount = discount
    
        def calculate_value(self):
            return (self.price * self.quantity) * (1 - self.discount)
        
class Inventory():
    def __init__(self, inventoryItem):
        inventoryItem = inventoryItem

    def add_item(self, item_id):
        print("Adding item")

    def remove_item(self, item_id):
        print("Removing item")

    def display_information(self):
        print("Displaying information")

    def calculate_total_value(self):
        print("Calculating total value")


def print_menu():
    print("1. Add item")
    print("2. Update existing item")
    print("3. Remove item")
    print("4. Display information")
    print("5. Calculate total inventory value")
    print("6. Exit")

if __name__ == "__main__":
    keepGoing = True
    while keepGoing:
        print_menu()
        choice = input("Enter choice: ")
        while(choice < 1 or choice > 6):
            print("\n\nInvalid choice")
            print_menu()
            choice = input("Enter choice: ")
