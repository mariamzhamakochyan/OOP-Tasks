class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def find_book(self, book_name):
        for book in self.books:
            if book.title == book_name:
                return book
        return None

    def borrow_book(self, book_name, user):
        book = self.find_book(book_name)
        if book is not None and book.is_available():
            book.borrow(user)
            return True
        else:
            return False
