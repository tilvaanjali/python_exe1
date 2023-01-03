class Category:

    def __init__(self, name, code, parent=0):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = 0
        self.display_name = 0
        self.products = 0


    def display_name(self):
        print("name is:" + str(self.name) + "," "code is:" + str(self.code) + "," "no of products:" + str(
            self.no_of_products) + ",""parent is:" + str(self.parent) + ','"display_name is:" + str(
            self.display_name) + ',' "products is:" + str(self.products) + ',')
        """print("name is:" + str(self.name))
        while (category_list == product_list):
            print(category_list, ">", product_list)"""


class Product(Category):

    def __init__(self, name, code, category, price):
        self.name = name
        self.price = price
        self.category = category
        self.code = code
        category.no_of_products += 1

    def display_name(self):
        return "name: " + str(self.name) + ',' "code: " + str(self.code) + ','"category:" + str(
            self.category) + ','"price" + str(self.price) + ','


"""vhl_obj = Category("vehicle", "v1", "petrol", "car", "BMW")
fd_obj = Category("Food", "fd1", "junk food", "pizza", "margrita")
anm_obj = Category("animal", "an1", "Birds", "parroat", "African Grey Parrots")
ty_obj = Category("toys", "t1", "soft toys", "teddy", "pink teddy")
wc_obj = Category("watch", "w1", "hand watch", "silver balt", "titan")"""
# Parent object

vhl_obj = Category("vehicle", "f1")
fd_obj = Category("Food", "f1")
anm_obj = Category("animal", "a1")
ty_obj = Category("toys", "t1")
wc_obj = Category("watch", "w1")

"""lst = [Product("BMW", "v1", vhl_obj, 700000),
       Product("Margrita", "fd1", fd_obj, 500),
       Product("Parroat", "an1", anm_obj, 6000),
       Product("teddy", "t1", ty_obj, 650),
       Product("titan", "w1", wc_obj, 5000),
       Product("verna", "v1", vhl_obj, 650000),
       Product("Italiyan", "fd1", fd_obj, 400),
       Product("sparrow", "an1", anm_obj, 20000),
       Product("doll", "t1", ty_obj, 630),
       Product("creta", "v1", vhl_obj, 800000)]"""

p1 = Product("BMW", "v1", vhl_obj, 500000)
p2 = Product("Pizza", "f1", fd_obj, 500)
p3 = Product("Parroat", "a1", anm_obj, 6000)
p4 = Product("teddy", "t1", ty_obj, 650)
p5 = Product("titan", "w1", wc_obj, 5000)
p6 = Product("verna", "v1", vhl_obj, 650000)
p7 = Product("Italiyan", "f1", fd_obj, 400)
p8 = Product("sparrow", "a1", anm_obj, 20000)
p9 = Product("doll", "t1", ty_obj, 630)
p10 = Product("creta", "v1", vhl_obj, 800000)

vhl_obj.display_name()

# list of category

category_list = [vhl_obj, fd_obj, anm_obj, ty_obj, wc_obj]

# product list

product_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
