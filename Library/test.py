from books import Library
from user import User

l = Library()
l.add_author("Dazai Osamu")
l.bookname("Dazai Osamu", "No longer human")
l.bookname("Dazai Osamu", "The setting sun")
l.bookname("Dazai Osamu", "Self-Portraits")
print(l.show())
u = User()
author = 'Dazai Osamu'
if author in l.books:
    u.add_user("Chūya Nakahara")
    u.add_book('Chūya Nakahara', author, "No longer human")
    # u.add_book('Chūya Nakahara', 'Dazai Osamu', "Self-Portraits")
else:
    print("no")
# u.add_user("Akutagawa")
# u.add_book('Akutagawa', 'Charles Dickens', "Great Expectations")
# u.add_book('Akutagawa', 'Charles Dickens', "Hard Times")
# print(u.show())
