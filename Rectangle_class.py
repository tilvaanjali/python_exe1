# class and object:
"""class Rectangle:
    def __init__(self, length, width):
        self.length = int(input("enter length:"))
        self.width = int(input("enter width:"))

    def perimeter(self):
        return 2* (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("length is:", self.length)
        print("width is:", self.width)
        print("perimeter is:", self.perimeter())
        print("area is:", self.area())


rect = Rectangle(7, 5)
rect.display()"""

# Inheritance Type:
"""class person:
    def person_info(self, name, age):
        print("this is child1 class")
        print("Name is:", name, "age is:", age)


class comapny(person):
    def child2(self, name1, location):
        print("this is child2 class")
        print("name is:", name1, "location is:", location)


class worker(person):
    def werker_info(self, id, salary):
        print("id is:", id, "salary is:", salary)


class employee(worker, comapny):
    def child2(self, salary, position):
        print("this is child3 class")
        print("salary is:", salary, "position is:", position)

obj = person()
obj1 = comapny()
obj2 = worker()
obj3 = employee()
obj.person_info("arjun", 20)
obj1.child2("reliutuin", "rajkot")
obj2.werker_info(10000, "manager")
obj3.child2(1, 1000000)"""


# method overriding:

class Father:
    def child(self, name, age):
        self.name = name
        self.age = age
        print("name is:", self.name, "age is:", self.age)


class Mother(Father):
    def child(self, name, age):
        super().child("Bhautik", 24)
        self.name = name
        self.age = age
        print("name is:", self.name, "age is:", self.age)


m = Mother()
m.child("Anjali", 22)



