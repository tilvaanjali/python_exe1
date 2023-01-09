class Category:

    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def display(self):
        print("name is:", str(self.name), "," "code is:", str(self.code), "," "no of products:",
              str(self.no_of_products))


class Product(Category):

    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

        category.no_of_products += 1

    def display(self):
        # print("name is:", str(self.name), "," "code is:", str(self.code), "," "category is:", str(self.category.name),
        #       "," "price is:", str(self.price))
        return "name: " + str(self.name) + ', '"code :" + str(self.code) + ', ' "category:" + self.category + ',' "price" + str(self.price) + ','


fur_obj = Category("Furniture", "f1")
ele_obj = Category("electronic", "e1")
vhl_obj = Category("vehicle", "v1")

lst = [Product("chair", "f1", fur_obj, 70),
       Product("Mobile", "e1", ele_obj, 15),
       Product("Window", "f1", fur_obj, 65),
       Product("Laptop", "e1", ele_obj, 60),
       Product("verna", "v1", vhl_obj, 5000),
       Product("tablet", "e1", ele_obj, 65000),
       Product("Ford", "v1", vhl_obj, 116000),
       Product("Door", "f1", fur_obj, 60000),
       Product("Volvo", "v1", vhl_obj, 63000),
       Product("BMW", "v1", vhl_obj, 800000)]

fur_obj.display()
ele_obj.display()
vhl_obj.display()

print("Price According low to high:")

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i].price >= lst[j].price:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

for a in range(len(lst)):
    print("name: " + lst[a].name + "," "code: " + lst[a].code + "," "category: " + lst[
        a].category.name + "," "price: " + str(lst[a].price))

print("Price According high to low:")

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i].price <= lst[j].price:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp

for a in range(len(lst)):
    print("name: " + lst[a].name + "," "code: " + lst[a].code + "," "category: " + lst[
        a].category.name + "," "price: " + str(lst[a].price))

# Serching:

code1 = input("enter code you want to search:")
for i in range(len(lst)):
    for j in range(1):
        if code1 == lst[i].code:
            print("name is:{}".format(lst[i].name))
            print("code is:{}".format(lst[i].code))
            print("category is:{}".format(lst[i].category.name))
            print("price is:{}".format(lst[i].price))
            print("####################################")
            break