class User:
    def __init__(self, username, user_id):
        self.username = username
        self.id = user_id
        self.money = 0
        self.cart = []
        
    def add_to_cart(self, restaurant, product_name):
        product = restaurant.get_product(product_name)
        if product:
            self.cart.append(product)
            return True
        else:
            print("There is no enough product")
            return False
    
    def checkout(self):
        total_cost = sum([product.price for product in self.cart])
        if self.money >= total_cost:
            self.money -= total_cost
            self.cart = []
            print("Purchase successful!")
        else:
            print("Not enough money!")