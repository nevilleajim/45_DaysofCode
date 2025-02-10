def add():
      id = input("Enter Customer ID: ")
      name = input("Enter Customer Name: ")
      addr = input("Enter Customer Address: ")
      phone = input("Enter the Customer Phone No: ")

      row = id + "\t" + name + "\t" + addr + "\t" + phone + "\n"

      with open("customer.txt", "a") as f:
            f.write(row)
            print("Record added Successfully.")
            f.close()

def delete():
      id = input("Enter the Customer ID to delete: ")

      with open("customer.txt", "r") as f:
            all = f.readlines()
            f.close()
      
      with open("customer.txt", "w") as f:
            flag = False

            for data in all:
                  d = data.split("\t", 1)

                  if d[0] != id:
                        f.writelines(data)
                  else:
                        flag = True
            f.close()
      if flag == True:
            print("Record Deleted successfully")
      else:
            print("No Record found")

def update():
      id = input("Enter customer ID to be searched: ")

      with open("customer.txt", "r") as f:
            all = f.readlines()
            f.close()
      
      with open("customer.txt", "w") as f:
            flag = False

            for data in all:
                  d = data.split("\t", 1)

                  if d[0] == id:
                        name = input("Enter new Customer Name: ")
                        addr = input("Enter new Customer Address: ")
                        phone = input("Enter new Customer Phone No: ")    

                        f.writelines(d[0] + "\t" + name + "\t" + addr + "\t" + phone + "\n")
                        flag = True

                  else:
                        f.writelines(data)
                  f.close 

            if flag == True:
                  print("Record Updated Successfully")
            else:
                  print("No Record was Found")

def search():
      id = input("Enter the customer ID to be searched: ")

      with open("customer.txt", "r") as f:
            all = f.readlines()
            flag = False
            
            for data in all:
                  d = data.split("\t", 1)

                  if d[0] == id:
                        print(data)
                        flag = True
            
      if flag == False:
            print("No record found")

      f.close()

def show():
      f = open("customer.txt", "r") 
      print("ID\tName\tAddress\tPhone No.")
      print(f.read())

print("Welcome to the Customer portal: ")
while True:
      print("Options: ")
      print("1. Add Customer")
      print("2. Delete Customer")
      print("3. Update Customer")
      print("4. Search Customer")
      print("5. Show all Customer")
      print("6. Exit")

      ch = int(input("Enter your choice: "))

      if ch==1:
            add()
      elif ch==2:
            delete()
      elif ch==3:
            update()
      elif ch==4:
            search()
      elif ch==5:
            show()
      elif ch==6:
            print("Breaking")
            break
      else:
            print("Invalid input. Please try again")
      print(" ")