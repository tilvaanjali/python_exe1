class Category:

    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = 0
        self.products = 0

    def display_name(self):
        print("name is:" + str(self.name) + "," "code is:" + str(self.code) + "," "no of products:" + str(
            self.no_of_products) + ",""parent is:" + str(self.parent) + ',')


class Product(Category):

    def __init__(self, name, code, category, price):
        self.name = name
        self.price = price
        self.category = category
        self.code = code
        category.no_of_products += 1

    def display_name(self):
        return "name: " + str(self.name) + ',' "price" + str(self.price) + ','


# Parent object

vhl_obj = Category("vehicle", "v1")
chl_obj = Category("Chocolate", "c1")
fd_obj = Category("Food", "f1")
ty_obj = Category("toys", "t1")
wc_obj = Category("watch", "w1")

# child object

c1 = Category("car", vhl_obj)
c2 = Category("Dark Chocolate", chl_obj)
c3 = Category("Pizza", fd_obj)
c4 = Category("Teddy", ty_obj)
c5 = Category("Hand Watch", wc_obj)

# Child of Child Object

childofc1 = Category("Audi", c1)
childofc2 = Category("Amul", c2)
childofc3 = Category("women", c5)



p1 = Product("Audi A8", "v1", c1, 225),
p2 = Product("Cadbury dark", "c1", c2, 100),
p3 = Product("Margrita", "f1", c3, 1200000),
p4 = Product("Lily’s Dark", "c1", c2, 400),
p5 = Product("Silver Watch", "w1", c5, 300),
p6 = Product("Italiyan", "f1", c3, 2500000),
p7 = Product("Pink teddy", "t1", ty_obj, 500),
p8 = Product("Black teddy", "t1", ty_obj, 3500000),
p9 = Product("i20", "v1", vhl_obj, 340000),
p10 = Product("Fruit & Nuts", "c1", chl_obj, 340)

# list of category

category_list = [vhl_obj, chl_obj, fd_obj, ty_obj, wc_obj]

# product list

product_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]

vhl_obj.display_name()