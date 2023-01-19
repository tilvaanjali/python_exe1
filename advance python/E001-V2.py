class Category:

    def __init__(self, name, code, parent=None, no_of_products=0):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = self.name
        self.set_display_name()
        self.products = []

    def display_category(self):
        print(self.display_name)
        print("no_of_products:", self.no_of_products)
        print("products: ", self.products)
        print("--------------------------")

    def set_display_name(self):
        obj = self

        while (obj.parent != None):
            self.display_name = f'{obj.parent.name} > {self.display_name}'
            obj = obj.parent





class Product(Category):

    def __init__(self, name, code, category, price):
        self.name = name
        self.price = price
        self.category = category
        self.code = code
        category.no_of_products += 1
        category.products.append(self.name)

    def display_name(self):
        print("product is:" + str(self.name) + ",""price is:" + str(self.price) + ",""category is:" + str(
            self.category.name) + ",")


# parent object

vehicle = Category("vehicle", "v1")
chocolate = Category("chocolate", "c1")
food = Category("junk food", "f1")
toy = Category("toys", "t1")
watch = Category("watch", "w1")
# Child Object

car = Category("car", "v1", vehicle)
dark_chocolate = Category("dark Chocolate", "c1", chocolate)
pizza = Category("pizza", "f1", food)
teddy = Category("teddy", "t1", toy)
hand_watch = Category("hand Watch", "w1", watch)

# Child of Child Object

petrol = Category("petrol", "v1", car)
amul = Category("amul", "c1", dark_chocolate)
cheese = Category("cheese", "f1", pizza)
small = Category("small", "t1", teddy)
women = Category("women", "w1", hand_watch)

# Name of All Products

product_list = [Product("audi A8", "v1", petrol, 5000000),
                Product("audi A9", "v1", car, 340000),
                Product("audi A10", "v1", petrol, 340000),
                Product("cadbury dark", "c1", dark_chocolate, 100),
                Product("milk Chocolate", "c1", amul, 340),
                Product("silk", "c1", dark_chocolate, 80),
                Product("margrita", "f1", pizza, 400),
                Product("peri Peri", "f1", cheese, 500),
                Product("italiyan", "f1", pizza, 300),
                Product("pink teddy", "t1", small, 500),
                Product("black teddy", "t1", teddy, 550),
                Product("red teddy", "t1", small, 550),
                Product("silver Watch", "w1", women, 3000),
                Product("gold Watch", "w1", women, 3000),
                Product("rose Gold Watch", "w1", hand_watch, 3000)]

# product_list = [p1, p2, p3, p4, p5, p7, p8, p9, p10, p11, p12, p13, p14, p15]
category_list = [vehicle, chocolate, food, toy, watch, car, dark_chocolate, pizza, teddy, hand_watch, petrol, amul,
                 cheese, small, women]
category_list.sort(key=lambda high_low : high_low.display_name)
for cat in category_list:
    cat.display_category()



