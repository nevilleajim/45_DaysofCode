class Book:
      def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
      
      def __str__(self):
            return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
      
class library:
      def __init__(self):
            self.books = []
      
      def addBook(self, book):
            self.books.append(book)
            print("Book ", book.title, " has been successful added.")

      def viewBooks(self):
            if not self.books:
                  print("No books in the library.")
            else:
                  for i in self.books:
                        print(i)
      
      def searchBook(self, query):
            foundBook = [book for book in self.books if (query.lower() in book.title.lower()) or (query.lower() in book.author.lower()) or (query.lower() in book.isbn)]

            if not foundBook:
                  print("No books found.")
            
            else:
                  for book in foundBook:
                        print(book)
      
def main():
      lib = library()
      while True:
            print("\n Librart Menu")
            print("1. Add Books")
            print("2. Show books")
            print("3. Search Books")
            print("4. Exit")

            ch = int(input("Enter your choice(1, 2, 3, 4): "))

            if ch == 1:
                  title = input("Enter Book Title: ")
                  author = input("Enter Book author: ")
                  isbn = input("Enter ISBN: ")
                  book = Book(title, author, isbn)
                  lib.addBook(book)
            
            elif ch == 2:
                  lib.viewBooks()
            
            elif ch == 3:
                  query = input("Enter your query (title, author, isbn): ")
                  lib.searchBook(query)
            
            elif ch == 4:
                  print("Exiting the library Appliication...")
                  break

            else:
                  print("Invalib Option. Please Try Again")

if __name__ == "__main__":
      main()