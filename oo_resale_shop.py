from typing import Dict, Union, Optional
""" inventory: a dictionary where we'll store our inventory
    The key is an int representing the item number
    The value is another dictionary containing information about the machine
"""
""" ResaleShop is the name of the class"""
class ResaleShop:

    # What attributes will it need?
    #  """ The next line defines the attribute of the inventory"""
    inventory = {}   
    itemID = 0 # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
def __init__(self, inventory, itemID):  
    self.inventory= inventory
    self.itemID= itemID

    def buy(self,computer: Dict[str, Union[str, int, bool]]):
     global itemID
     self.itemID += 1 # increment itemID
     self.inventory[self.itemID] = computer
     return self.item_id

    def update_price(self, item_id: int, new_price: int):
     if self.item_id in self.inventory:
        self.inventory[self.item_id]["price"] = new_price
     else:
        print("Item", self.item_id, "not found. Cannot update price.")

    def sell(self,item_id: int):
     if self.item_id in self.inventory:
        del self.inventory[self.item_id]
        print("Item", self.item_id, "sold!")
     else: 
        print("Item", self.item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
    # If the inventory is not empty
     if self.inventory:
        # For each item
        for self.item_id in self.inventory:
            # Print its details
            print(f'Item ID: {self.item_id} : {self.inventory[self.item_id]}')
     else:
        print("No inventory to display.")

     def refurbish(self, item_id: int, new_os: Optional[str] = None) :
      if self.item_id in self.inventory:
        computer = self.inventory[self.item_id] # locate the computer
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
        else:
         print("Item", self.item_id, "not found. Please select another item to refurbish.")         