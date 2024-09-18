"""
Week 7 Lab 1
Question 4: Python code to create a library management system
Author: Sukhjyot Singh Saini
"""

class Book():
    def __init__(self,title,author,publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.availability_status = True

    def book_unavailable(self):
        self.availability_status = False
        
    def book_available(self):
        self.availability_status = True

    def __str__(self):
        return f"{self.title}({self.publication_year}) by {self.author} is currently {'available' if self.availability_status else 'unavailable'}"
    

class Patron():
    def __init__(self, patron_name,patron_id):
        self.patron_name = patron_name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.availability_status:
            book.book_unavailable()
            self.borrowed_books.append(book)
            print(f"{self.patron_name}({self.patron_id}) borrowed {book.title}")

        else:
            print(f"{book.title} is not available")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.book_available()
            self.borrowed_books.remove(book)
            print(f"{self.patron_name}({self.patron_id}) returned {book.title}")

        else:
            print(f"{self.patron_name}({self.patron_id}) did not borrow {book.title}")

    def list_borrowed_books(self):
        if self.borrowed_books:
            print(f"Borrowed books by {self.patron_name}({self.patron_id})")
            for book in self.borrowed_books:
                print(book)

        else:
            print(f"{self.patron_name}({self.patron_id}) has no borrowed books.")

    def __str__(self):
        return f"{self.patron_name}({self.patron_id})"


class Library():
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self,book):
        self.books.append(book)

    def add_patron(self,patron):
        self.patrons.append(patron)

    def list_books(self):
        if self.books:
            print("List of books:")
            for book in self.books:
                print(book)

        else:
            print("No books available")

    def list_patrons(self):
        if self.patrons:
            print("List of patrons:")
            for patron in self.patrons:
                print(patron)

        else:
            print("No registered patrons")

    def track_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        
        return None
    
    def track_patron(self, name):
        for patron in self.patrons:
             if patron.patron_name.lower() == name.lower():
                return patron
        return None

    
def menu():
    print("Library Management System: ")
    print("1. List available books")
    print("2. List registered patrons")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. List borrowed books")
    print("6. Add a book to the library")
    print("7. Exit")

def main():
    manage_library = Library()
    manage_library.add_book(Book("Norwegian Wood", "Haruki Murakami", 1987))
    manage_library.add_book(Book("The Way of Kings", "Brandon Sanderson", 2010))
    manage_library.add_book(Book("Deathnote", "Tsugumi Ohba", 2006))

    customers = Library()
    customers.add_patron(Patron("Alice", 301))
    customers.add_patron(Patron("Julia", 302))

    while True:
        menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manage_library.list_books()

        elif choice == "2":
            customers.list_patrons()

        elif choice == "3":
            customer_name = input("Enter your Name: ").strip()
            book_title = input("Enter Book Title to borrow: ").strip()
            customer = customers.track_patron(customer_name)
            book = manage_library.track_book(book_title)
            if customer and book:
                customer.borrow_book(book)
            elif not customer:
                print("Patron not found.")
            elif not book:
                print("Book not found.")

        elif choice == "4":
            customer_name = input("Enter your Name: ").strip()
            book_title = input("Enter Book Title to return: ").strip()
            customer = customers.track_patron(customer_name)
            book = manage_library.track_book(book_title)
            if customer and book:
                customer.return_book(book)
            elif not customer:
                print("Patron not found.")
            elif not book:
                print("Book not found.")


        elif choice == "5":
            customer_name = input("Enter your Name: ").strip()
            customer = customers.track_patron(customer_name)
            if customer:
                customer.list_borrowed_books()

            else:
                print("Patron not found.")

        elif choice == "6":
            title = input("Enter Book Title: ").strip()
            author = input("Enter Book Author: ").strip()
            publication_year = int(input("Enter Book Publication Year: "))
            manage_library.add_book(Book(title,author,publication_year))
            print(f"Book {title} added to the library.")

        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

