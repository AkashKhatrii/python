from datetime import datetime

class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.copies = 3
        self.books = []

    def add_book(self, barcode, shelf):
        if len(self.books) >= self.copies:
            print(f"Cannot add more copies than allowed ({self.copies})")
            return None
        book_item = BookItem(self, barcode, shelf)
        self.books.append(book_item)
        return book_item
    
class BookItem:
    def __init__(self, book, barcode, shelf):
        self.book = book  # Fix: Assign the correct book reference
        self.barcode = barcode
        self.shelf = shelf  # Fix: Correct the attribute name
        self.is_available = True
        self.borrower = None
        self.borrowed_date = None
    
    def checkout(self, member):
        if not self.is_available:
            return False
        if len(member.checked_out_books) >= 5:
            return False
        self.is_available = False
        self.borrower = member
        self.borrowed_date = datetime.now()
        member.checked_out_books.append(self)
        return True
    
    def return_book(self):
        self.is_available = True
        if self.borrower:
            self.borrower.checked_out_books.remove(self)
            self.borrower = None

class LibraryMember:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.checked_out_books = []

    def checkout_book(self, book_item):
        return book_item.checkout(self)

    def return_book(self, book_item):
        book_item.return_book()
    

class Librarian:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def add_book(self, library, book):
        library.books.append(book)
    
    def remove_book(self, library, book):
        library.books.remove(book)


class LibrarySystem:
    def __init__(self):
        self.books = []
        self.members = []

    def search_books(self, title=None, author=None, subject=None, publication_date=None):
        results = []
        for book in self.books:
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (subject and subject.lower() in book.subject.lower()) or \
               (publication_date and publication_date == book.publication_date):
                results.append(book)
        return results
    
    def issue_book(self, member: LibraryMember, book_item: BookItem):
        return member.checkout_book(book_item)  # Fix: Call the correct method
    
    def return_book(self, member, book_item):
        member.return_book(book_item)


def main():
    # Create library system
    library = LibrarySystem()
    librarian = Librarian("L001", "Alice")
    member = LibraryMember("M001", "John Doe", "john@example.com")
    member2 = LibraryMember("M002", "akash", "akash@.com")
    
    # Add a book to the library
    book = Book("12345", "Python Basics", "Author A")
    librarian.add_book(library, book)
    
    # Add copies of the book
    book_item1 = book.add_book("B001", "Shelf 1")
    book_item2 = book.add_book("B002", "Shelf 2")
    
    # Add member to the library
    library.members.append(member)
    
    # Member checks out a book
    if book_item1 and library.issue_book(member, book_item1):
        print("Book checked out successfully.")
    else:
        print("Failed to checkout book.")

    if book_item1 and library.issue_book(member2, book_item1):
        print("Book checked out successfully.")
    else:
        print("Failed to checkout book.")
    
    # Member returns the book
    library.return_book(member, book_item1)
    print("Book returned successfully.")

    if book_item1 and library.issue_book(member, book_item1):
        print("Book checked out successfully.")
    else:
        print("Failed to checkout book.")
    
    # Search for a book
    found_books = library.search_books(title="Python Basics")
    print(f"Books found: {[book.title for book in found_books]}")
    
if __name__ == "__main__":
    main()
