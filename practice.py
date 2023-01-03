class Category:

    def __init__(self, name, code,parent,d_name):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.d_name = d_name
        #self.products = 0

    def display_name(self):
        print("name is:" + str(self.name) + "," "code is:" + str(self.code) + "," "no of products:" + str(
            self.no_of_products) + ",""parent is:" + str(self.parent) + ','"display_name is:" + str(
            self.d_name) +  ',')
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
        #return "name: " + str(self.name) + ',' "code: " + str(self.code) + ','"category:" + str(
         #   self.category) + ','"price" + str(self.price) + ','
        print("product is:" + str(self.name) + ",""code is:" + str(self.code) + ",""category is:" + str(self.category) + ",""price is:" + str(self.price) + ",")

"""vhl_obj = Category("vehicle", "f1")
fd_obj = Category("Food", "f1")
anm_obj = Category("animal", "a1")
ty_obj = Category("toys", "t1")
wc_obj = Category("watch", "w1")

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

vhl_obj.display_name()"""

vhl_obj = Category("Vehicle", "v1","Car","Audi")
chl_obj = Category("Chocolate", "c1","Dark Chocolate","Amul")
fd_obj = Category("Junk Food", "f1","Pizza","Domino's")
ty_obj = Category("Soft toys", "t1","Teddy","Flipcart")
wc_obj = Category("Watch", "w1","Hand Watch","women")

""" Child Object

c1 = Category("vehicle", vhl_obj)
c2 = Category("Dark Chocolate", chl_obj)
c3 = Category("Pizza", fd_obj)
c4 = Category("Teddy", ty_obj)
c5 = Category("Hand Watch", wc_obj)

# Child of Child Object

childofc1 = Category("Audi", "v1",vhl_obj)
childofc2 = Category("Amul", "c1",chl_obj)
childofc3 = Category("women","w1", wc_obj)"""

# Name of All Products

pro1 = Product("Audi A8", "v1", vhl_obj, 225)
pro2 = Product("Cadbury dark", "c1", chl_obj, 100)
pro3 = Product("Margrita", "f1", fd_obj, 1200000)
pro4 = Product("Lily’s Dark", "c1", chl_obj, 400)
pro5 = Product("Silver Watch", "w1", wc_obj, 300)
pro6 = Product("Italiyan", "f1", fd_obj, 2500000)
pro7 = Product("Pink teddy", "t1", ty_obj, 500)
pro8 = Product("Black teddy", "t1", ty_obj, 3500000)
pro9 = Product("i20","v1", vhl_obj, 340000)
pro10 = Product("Fruit & Nuts","c1", chl_obj, 340)




product_list = [pro1, pro2, pro3, pro4, pro5, pro6, pro7, pro8, pro9, pro10]
for a in range(len(product_list)):
    vhl_obj.display_name()
    print("product is: " + product_list[a].name + "," "price is: " + str(product_list[a].price))
