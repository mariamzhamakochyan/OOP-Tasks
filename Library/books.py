class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrower = None

    def borrow(self, user):
        self.borrower = user

    def is_available(self):
        return self.borrower is None

    def get_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nBorrower: {self.borrower}"