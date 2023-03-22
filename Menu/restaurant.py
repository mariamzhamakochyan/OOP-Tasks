class Restaurant:
    def __init__(self, name):
        self.name = name
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def get_product(self, product_name):
        for product in self.products:
            if product.name == product_name and product.count > 0:
                product.count -= 1
                return product
        return None