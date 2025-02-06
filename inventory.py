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

