class Category:

    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.no_of_products = 0
        self.parent = parent
        self.display_name = self.name
        self.set_display_name()
        self.products = []

    def set_display_name(self):
        obj = self

        while (obj.parent != None):
            self.display_name = f'{obj.parent.name} > {self.display_name}'
            obj = obj.parent


class Product(Category):

    def __init__(self, name, code, category, price, stock_at_locations={}):
        self.name = name
        self.price = price
        self.category = category
        self.code = code
        self.stock_at_locations = stock_at_locations
        # category.no_of_products += 1
        # category.products.append(self.name)
        # stock_at_locations.append(stock_at_locations)


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
        try:
            # print("{} \n{} > {} {}".format("product name:",self.product.name,"From location:",self.from_location.name,"To Location:",self.to_location.name,"Quntity:",self.quantity))
            print(f"product name: {self.product.name} \nFrom Location: {self.from_location.name}\nTo Location: {self.to_location.name}\nQuantity: {self.quantity}")
            print("--------------------")
        except:
            print("no any product")

    @staticmethod
    def movements_by_product(product):
        pass


# Location object:
rajkot = Location("Rajkot", "L001")
junagadh = Location("Junagadh", "L002")
jamnager = Location("Jamnager", "Loo3")
surat = Location("Surat", "L004")

list_of_location = [rajkot, junagadh, jamnager, surat]

# Category Object:
vehicle = Category("vehicle", "v1")
chocolate = Category("chocolate", "c1")
food = Category("junk food", "f1")
toy = Category("toys", "t1")
watch = Category("watch", "w1")

# Product object:
vehicle = Product("Car", "v1", vehicle, 5000000, {rajkot: 100, junagadh: 20})
dark_chocolate = Product("Dark Chocolate", "c1", chocolate, 100, {junagadh: 20})
bus = Product("Bus", "v1", vehicle, 400, {jamnager: 30, surat: 89})
soft_toy = Product("Soft Toy", "t1", toy, 500, {surat: 10})
women_watch = Product("Women Watch", "w1", watch, 3000, {rajkot: 12})
chocolate = Product("Chocolate", "c1", chocolate, 80, {surat: 8})

product_list=[vehicle,dark_chocolate,bus,soft_toy,women_watch,chocolate]

# Movement object:

movement1 = Movement(rajkot, junagadh, vehicle, 20),
movement2=Movement(junagadh, surat, dark_chocolate, 50),
movement3=Movement(jamnager, junagadh, bus, 40),
movement4=Movement(surat, rajkot, soft_toy, 60),
movement5=Movement(jamnager, rajkot, women_watch, 30)

movement_list=[movement1,movement2,movement3,movement4,movement5]

"""for pl in product_list:
    print(pl.name)
print("------------------")"""

print("Display product details with its stock at various locations")

for pl in product_list:
    print(pl.name)
    for sl in pl.stock_at_locations:
        print(f"{sl.name} - {pl.stock_at_locations[sl]}")
    print("-------------------")

print("Display product list by location(group by location) ")

for lol in list_of_location:
    print(lol.name)
    for pl in product_list:
        if lol in pl.stock_at_locations:
            print(f"{pl.name} - {pl.stock_at_locations[lol]}")
    print("-------------------")
