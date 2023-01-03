list1 = []
lst = ["enter name", "enter age", "enter email", "enter pho no:"]

"""def enter_details():
    name = input("enter name:")
    age = input("enter age:")
    email = input("enter email:")
    phn_no = input("enter phone no:")"""


def adddetails():
    i = 0
    for i in range(len(lst)):
        no = int(input(lst[i]))
        list1.append(no)
    print(list1)
    #enter_details()
    #list1.append(enter_details())


def printdetails():
    if list1:
        emp1 = {}
        for i in range(len(list1)):
           """ name = int(input("enter name:"))
            age = int(input("enter age:"))
            email = int(input("enter email:"))
            phn_no = int(input("enter phn_no:"))

            emp1["enter name:"]: name
            emp1["enter age"]: age
            emp1["enter email"]: email
            emp1["phn_no"]: phn_no

        print(emp1)"""

        emp1 = {["enter name"]: list1[i]}
         #lst[i]]=list1[i]
        print(emp1)

    else:
        print("No Record Found")


while True:
    print("1.Add Details:")
    print("2.print Details:")
    print("3.Exit Details:")
    choice = input("enter Choice:")
    if choice == 1:
        adddetails()

    elif choice == 2:
        printdetails()

    else:
        print("Thank You..!!")
        print("quit")
        break
