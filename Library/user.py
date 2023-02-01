from collections import defaultdict
class User:
    def __init__(self):
        self.user = {}
        
    def add_user(self, name):
        self.user[name] = defaultdict(list)
        
    def add_book(self, name, author, title):
        if author in librsr:
            if title in libvali mej uremn:
                aut = self.user[name]
                title_list = aut[author]
                title_list.append(title)
            else:
                print("ayd vernagrov girq cavoq ays pahin arka chka")
        else:
            print("tvyal nhexinakic grqer ays pahin arka chka")
            
    def show(self):
        return self.user

u = User()
u.add_user("Chūya Nakahara")
u.add_book('Chūya Nakahara', 'Dazai Osamu', "No longer human")
u.add_book('Chūya Nakahara', 'Dazai Osamu', "Self-Portraits")
u.add_user("Akutagawa")
u.add_book('Akutagawa', 'Charles Dickens', "Great Expectations")
u.add_book('Akutagawa', 'Charles Dickens', "Hard Times")
# print(u.show())
