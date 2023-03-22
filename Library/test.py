from books import Book
from library import Library
from user import User

lib = Library()

book1 = Book("No longer human", "Dazai Osamu")
book2 = Book("Self-Portraits", "Dazai Osamu")
book3 = Book("Great Expectations", "Charles Dickens")

lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)

user1 = User("Alice")
user2 = User("Bob")

lib.borrow_book("No longer human", user1)
lib.borrow_book("No longer human", user2)
lib.borrow_book("Great Expectations", user2)

for book in lib.books:
    print(book.get_info())
