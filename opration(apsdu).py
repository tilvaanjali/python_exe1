from oprationmod1 import *

"""val1 = int(input('Enter value1: '))
val2 = int(input('Enter Value2: '))
print("Sum is : ",operations.sum(val1,val2))"""

while True:
    print("1.Add Details:")
    print("2.print Details:")
    print("3.search Details:")
    print("4.delete Details:")
    print("5.update Details:")
    choice = int(input("enter Choice:"))
    # lst = ["enter name", "enter age", "enter email", "enter pho no:"]
    if choice == 1:
        enter_details()
    elif choice == 2:
        printdetails()
    elif choice == 3:
        search_detaills()
    elif choice == 4:
        delete_details()
    elif choice == 5:
        update_details()
    else:
        print("quit")
        break