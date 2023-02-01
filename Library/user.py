from collections import defaultdict
class User:
    def __init__(self):
        self.user = {}
    def add_user(self, name):
        self.user[name] = defaultdict(list)
    
    def add_book(self, name, author, title):
        by_subject = self.user[name]
        grade_list = by_subject[author]
        grade_list.append(title)
    def show(self):
        return self.user

u = User()
u.add_user("Chūya Nakahara")
u.add_book('Chūya Nakahara', 'Dazai Osamu', "No longer human")
u.add_book('Chūya Nakahara', 'Dazai Osamu', "Self-Portraits")
u.add_user("Akutagawa")
u.add_book('Akutagawa', 'Charles Dickens', "Great Expectations")
u.add_book('Akutagawa', 'Charles Dickens', "Hard Times")
print(u.show())
