class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) < 5:
            self.borrowed_books.append(book)
            print(f"Book {book.title} borrowed by {self.name} ")
            return True
        else:
            print(f"{self.name} has already borrowed 5 books.")
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"Book {book.title} return by {self.name}")
            return True
        else:
            print(f"{self.name} does not have the book '{book.title}'.")
            return False

class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.total_copies = total_copies
        self.available_copies = self.total_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"One copy of {self.title} borrowed. {self.available_copies} left.")
            return True
        else:
            print(f"No copies of {self.title} available.")
            return False
    
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f"One copy of '{self.title}' returned. {self.available_copies} copies available.")
            return True
        else:
            print(f"All copies of '{self.title}' are already in the library.")
            return False


class Library:
    def __init__(self):
        self.users = {}
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            print(f"Book {self.title} already present. Adding more copies")
            self.books[book.isbn].total_copies += book.total_copies
            self.books[book.isbn].available_copies += book.available_copies
        else:
            self.books[book.isbn] = book
        print(f"Book '{book.title}' added to the library.")

    def register_user(self, user):
        if user.user_id in self.users:
            print(f"User {user.name} already present.")
        else:
            self.users[user.user_id] = user

        print(f"User '{user.name}' added to the library.")

    def borrow_book(self, user_id, isbn):
        user = self.users.get(user_id)
        book = self.books.get(isbn)

        if not user:
            print(f"User with id {user_id} not found")
            return False
        if not book:
            print(f"Book with ISBN {isbn} not found.")
            return False

        if book.borrow_book():
            if user.borrow_book(book):
                return True
            else:
                book.return_copy()
        return False

    def return_book(self, user_id, isbn):
            user = self.users.get(user_id)
            book = self.books.get(isbn)

            if not user:
                print(f"User with ID {user_id} not found.")
                return False
            if not book:
                print(f"Book with ISBN {isbn} not found.")
                return False

            if user.return_book(book):
                book.return_book()
                return True
            return False


if __name__ == "__main__":
    # Initialize the library
    library = Library()

    # Add books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "12345", 3)
    book2 = Book("1984", "George Orwell", "67890", 2)
    library.add_book(book1)
    library.add_book(book2)

    # Register users
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    library.register_user(user1)
    library.register_user(user2)

    # Borrow books
    library.borrow_book(1, "12345")  # Alice borrows "The Great Gatsby"
    library.borrow_book(1, "67890")  # Alice borrows "1984"
    library.borrow_book(2, "12345")  # Bob borrows "The Great Gatsby"

    # Return books
    library.return_book(1, "12345")  # Alice returns "The Great Gatsby"
    library.return_book(2, "12345")  # Bob returns "The Great Gatsby"

    # Attempt invalid operations
    library.borrow_book(3, "12345")  # Invalid user
    library.return_book(1, "11111")  # Invalid book
