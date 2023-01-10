class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Movement:
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity


""" @staticmethod
 def movements_by_product(product):"""


class Category:

    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = self.name
        # self.set_display_name()
        self.products = []


class Product(Category):

    def __init__(self, name, code, category, price):
        self.name = name
        self.price = price
        self.category = category
        self.code = code
        category.no_of_products += 1
        category.products.append(self.name)
