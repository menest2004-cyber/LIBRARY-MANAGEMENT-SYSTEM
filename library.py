# LIBRARY MANAGEMENT SYSTEM
# By M. Enest - menest2004-cyber

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, book_id):
        new_book = Book(title, author, book_id)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in library")
            return
        print("\n--- LIBRARY BOOKS ---")
        for book in self.books:
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"ID:{book.book_id} | {book.title} by {book.author} - {status}")

    def search_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                status = "Borrowed" if book.is_borrowed else "Available"
                print(f"Found: {book.title} by {book.author} - {status}")
                return
        print("Book not found")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You borrowed '{book.title}'")
                else:
                    print("Book already borrowed")
                return
        print("Book ID not found")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.is_borrowed = False
                print(f"You returned '{book.title}'")
                return
        print("Book ID not found")

# Main Program
if __name__ == "__main__":
    lib = Library()
    # Add sample books
    lib.add_book("Things Fall Apart", "Chinua Achebe", "001")
    lib.add_book("Born a Crime", "Trevor Noah", "002")
    lib.add_book("The Alchemist", "Paulo Coelho", "003")
    
    while True:
        print("\n1. View Books 2. Add Book 3. Search 4. Borrow 5. Return 6. Exit")
        choice = input("Choose: ")
        if choice == "1":
            lib.view_books()
        elif choice == "2":
            t = input("Title: ")
            a = input("Author: ")
            i = input("ID: ")
            lib.add_book(t, a, i)
        elif choice == "3":
            t = input("Search title: ")
            lib.search_book(t)
        elif choice == "4":
            i = input("Book ID to borrow: ")
            lib.borrow_book(i)
        elif choice == "5":
            i = input("Book ID to return: ")
            lib.return_book(i)
        elif choice == "6":
            break
