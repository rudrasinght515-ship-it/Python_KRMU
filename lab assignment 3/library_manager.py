"""

Project: Calorie Tracker program (CLI)

Name: Rudra Singh
Roll No: 2501730339
Section: C

Description: 
      A easy program to record your daily reading in library inventory. 

"""

import json
from pathlib import Path

#*****************************

        # Book Class

#*****************************

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self):
        return {"title": self.title, "author": self.author, "isbn": self.isbn, "status": self.status}

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False


#*****************************

    # Library Inventory

#*****************************

class LibraryInventory:
    def __init__(self, file_path="catalog.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_catalog()

    def add_book(self, book):
        self.books.append(book)
        self.save_catalog()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return [str(b) for b in self.books]

    def save_catalog(self):
        with open(self.file_path, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def load_catalog(self):
        if self.file_path.exists():
            try:
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.books = [Book(**d) for d in data]
            except Exception:
                self.books = []


#*****************************

        # CLI Menu

#*****************************

def menu():
    inventory = LibraryInventory()

    while True:
        print("\n--- Library Inventory Manager ---")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            isbn = input("ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_catalog()
                print("Book issued!")
            else:
                print("Book not available.")

        elif choice == "3":
            isbn = input("ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_catalog()
                print("Book returned!")
            else:
                print("Book not found or already available.")

        elif choice == "4":
            for b in inventory.display_all():
                print(b)

        elif choice == "5":
            title = input("Enter title keyword: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()