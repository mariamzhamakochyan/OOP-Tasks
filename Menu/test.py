# Create some products
pizza = Product("Pizza", 5, 10)
burger = Product("Burger", 3, 5)
salad = Product("Salad", 1, 7)
# Create some restaurants and add products to them
restaurant1 = Restaurant("Pizza Place")
restaurant1.add_product(pizza)
restaurant2 = Restaurant("Burger Joint")
restaurant2.add_product(burger)
restaurant3 = Restaurant("Salad Bar")
restaurant3.add_product(salad)
# Create a menu and add the restaurants to it
menu = Menu()
menu.add_restaurant(restaurant1)
menu.add_restaurant(restaurant2)
menu.add_restaurant(restaurant3)
# Create a user
user = User("Alice", 123)
# Add some products to the user's cart
user.add_to_cart(restaurant1, "Pizza")
user.add_to_cart(restaurant2, "Burger")
user.add_to_cart(restaurant3, "Salad")
# Set the user's money
user.money = 20
# Checkout the user's cart
user.checkout()