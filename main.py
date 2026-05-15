import json
import os


class Library:

    def __init__(self):
        self.file_name = "books.json"

        # Create file if not exists
        if not os.path.exists(self.file_name):
            with open(self.file_name, "w") as file:
                json.dump([], file)

    # Load books
    def load_books(self):
        with open(self.file_name, "r") as file:
            return json.load(file)

    # Save books
    def save_books(self, books):
        with open(self.file_name, "w") as file:
            json.dump(books, file, indent=4)

    # Add book
    def add_book(self):
        books = self.load_books()

        book_id = int(input("Enter Book ID: "))
        
        # Check duplicate ID
        for book in books:
            if book["id"] == book_id:
                print("Book ID already exists!")
                return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        new_book = {
            "id": book_id,
            "title": title,
            "author": author,
            "available": True
        }

        books.append(new_book)
        self.save_books(books)

        print("Book added successfully!")

    # View books
    def view_books(self):
        books = self.load_books()

        if not books:
            print("No books available.")
            return

        print("\n--- Book List ---")

        for book in books:
            status = "Available" if book["available"] else "Issued"

            print(f"""
Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
Status  : {status}
-------------------------
""")

    # Search book
    def search_book(self):
        books = self.load_books()

        keyword = input("Enter title to search: ").lower()

        found = False

        for book in books:
            if keyword in book["title"].lower():
                print(f"""
Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
""")
                found = True

        if not found:
            print("Book not found.")

    # Issue book
    def issue_book(self):
        books = self.load_books()

        book_id = int(input("Enter Book ID to issue: "))

        for book in books:
            if book["id"] == book_id:

                if not book["available"]:
                    print("Book already issued.")
                    return

                book["available"] = False
                self.save_books(books)

                print("Book issued successfully!")
                return

        print("Book not found.")

    # Return book
    def return_book(self):
        books = self.load_books()

        book_id = int(input("Enter Book ID to return: "))

        for book in books:
            if book["id"] == book_id:

                if book["available"]:
                    print("Book already available in library.")
                    return

                book["available"] = True
                self.save_books(books)

                print("Book returned successfully!")
                return

        print("Book not found.")


# Main Program
library = Library()

while True:

    print("""
====== LIBRARY MANAGEMENT SYSTEM ======

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")