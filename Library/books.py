class Library:
    def __init__(self):
        global
        self.books = {}
        
    def add_author(self, author):
        self.books[author] = []

    def bookname(self, author, title):
        self.books[author].append(title)
     
    def show(self):
        return self.books

l = Library()
l.add_author("Dazai Osamu")
l.bookname("Dazai Osamu", "No longer human")
l.bookname("Dazai Osamu", "The setting sun")
l.bookname("Dazai Osamu", "Self-Portraits")
print(l.show())
