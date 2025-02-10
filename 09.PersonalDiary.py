import os
from datetime import datetime

def writeEntry():
      entry = input("Write the diary entry: ")
      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

      with open('diary.txt', 'a') as file:
            file.write(f"{timestamp}\n{entry}\n\n")

def viewEntries():
      if not os.path.exists("diary.txt"):
            print("No Diary Entries Found!!!")
            return
      
      with open("diary.txt", 'r') as file:
            entries = file.read()
      print("\n--------Diary Entries---------")
      print(entries)

def main():
      while True:
            print("Personal Diary")
            print("\n 1. Write a new entry")
            print("\n 2. View entries")
            print("\n 3. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                  writeEntry()
            elif choice == 2:
                  viewEntries()
            elif choice == 3:
                  break
            else:
                  print("Invalid Choice.")

if __name__ == '__main__':
      main()