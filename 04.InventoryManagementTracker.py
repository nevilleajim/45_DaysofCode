# INVENTORY TRACKER APPLICATION

inventory = {}
def addItem():
      item = input("Enter the item to be added to the inventory: ")
      quantity = int(input("Enter the quantity of "+item+" : "))

      if item in inventory:
            inventory[item]+=quantity
      else:
            inventory[item] = quantity
      print(str(quantity) + " of "+item+" has been added to the inventory")

def displayInventory():
      print("\nCurrent inventory")
      for item,quantity in inventory.items():
            print(item+" : "+str(quantity))
      print()

def removeItem():
      item = input("Enter the name of the item to be removed: ")
      if item in inventory:
            del inventory[item]
            print(" "+item+" has been removed from the inventory.")
      
      else:
            print("Item not found in the Inventory.")

def updateItem():
      item = input("Enter the item to be updated: ")
      if item in inventory:
            quantity = int(input("Enter the new quantity for "+item))
            inventory[item] = quantity
            print("Quantity of "+item+" has been updated to "+str(quantity))
      else:
            print(" "+item+" not found in the inventory.")

def searchItem():
      item = input("Enter the item to be searched: ")
      if item in inventory:
            print(" "+item+" is in the inventory with quantity: "+str(inventory[item]))
      else:
            print(" "+item+" not found in the inventory.")

def main():
      while True:
            print("-----------INVENTORY TRACKER----------")
            print("--------------------------------------")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Item")
            print("4. Search Item")
            print("5. Display Inventory")
            print("6. Exit")
            print("--------------------------------------")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                  addItem()
            elif choice == 2:
                  removeItem()
            elif choice == 3:
                  updateItem()
            elif choice == 4:
                  searchItem()
            elif choice == 5:
                  displayInventory()
            elif choice == 6:
                  break
            else:
                  print("Choice Invalid!!! Try Again!!!")

if __name__ == "__main__":
      main()