"""from choice import ascending_order, descending_order
from choice_module1 import min_no, max_no

while True:
    print("2.Maximum no")
    print("3.Minimum no")
    print("4.Ascending  order")
    print("5.Descending order")

    choice = int(input("enter choice"))
    if choice == 4:
        ascending_order()
    elif choice == 5:
        descending_order()
    else:
        print("close")
        break"""
lst=[]
def ascending_order(lst):
    temp = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])



def descending_order(lst):
    temp = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] <= lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])


