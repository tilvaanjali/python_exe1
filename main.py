class Department:
    def __init__(self, name, emps=0):
        self.name = name
        self.emps = emps

    def display(self):
        print('Deartment: ', self.name)
        print('Employees: ', self.emps)


class Employee(Department):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
        department.emps += 1

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Department: ", self.department.name)


it_dept = Department("IT")
admin_dept = Department('Admin')

emp1 = Employee("ABC", 20, it_dept)
emp2 = Employee("XYZ", 28, it_dept)
emp3 = Employee("ABC", 20, admin_dept)

it_dept.display()
admin_dept.display()
emp1.display()
emp2.display()
emp3.display()



