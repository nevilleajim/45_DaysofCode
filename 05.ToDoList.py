# TODO LIST

toDoList = []
completedList = []

def addItem():
      item = input("Enter the item to add: ")
      toDoList.append(item)
      print(" "+item+ " has been successfullty added to the ToDo List")

def removeItem():
      index = input("Enter the index of the item to remove: ")
      if index.isdigit() and 1 <= int(index) <= len(toDoList):
            removedItem = toDoList.pop(int(index)-1)
            print(" "+removedItem+" has been removed from the ToDo List successfully.")
      
      else:
            print("Invalid Index. Please try again.")

def displayList(lst, listName):
      print("\n"+listName+": ")
      for index,item in enumerate(lst, start=1):
            print(str(index)+"."+item)
            print(" ")

def markItemCompleted():
      index = input("Enter the index of the item to mark as completed: ")
      if index.isdigit() and 1 <= int(index) <= len(toDoList):
            completedItem = toDoList.pop(int(index)-1)
            completedList.append(completedItem)
            print(" "+completedItem+" has been marked as completed.")
            
      else:
            print("Invalid index. Please try again.")

def main():
      while True:
            print("----------------ToDo List------------------")
            print("-------------------------------------------")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Mark Item as Completed")
            print("4. Display ToDo List")
            print("5. Display Completed List")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                  addItem()

            elif choice == 2:
                  removeItem()
            
            elif choice == 3:
                  markItemCompleted()
            
            elif choice == 4:
                  displayList(toDoList, "To Do List")
            
            elif choice == 5:
                  displayList(completedList, "Completed List")
            
            elif choice == 6:
                  break

            else:
                  print("Invalid choice. Please Try again")

if __name__ == "__main__":
      main()