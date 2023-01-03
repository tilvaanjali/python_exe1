"""def addvalue()
for i in range(0, 5):
    no = int(input('Enter No {}: '.format(i + 1)))
    lst.append(no)


def max_no():
    max1_no = lst[0]
    for no in range(len(lst)):
        if lst[no] >= max1_no:
            max1_no = lst[no]

    print('Max No. is: {}'.format(max1_no))


def min_no():
    min_no = lst[0]
    for no in range(len(lst)):
        if lst[no] <= min_no:
            min_no = lst[no]

    print('Min No. is: {}'.format(min_no))


def ascending_order():
    temp = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])


def descending_order():
    temp = 0
    print("Dessending order")
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] <= lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])"""

from choice_module1 import maximum_no, minimum_no
from choice_module2 import ascending_order, descending_order

lst = []
for i in range(0, 5):
    no = int(input('Enter No {}: '.format(i + 1)))
    lst.append(no)

while True:
    print("1.Maximum no")
    print("2.Minimum no")
    print("3.Ascending  order")
    print("4.Descending order")

    choice = int(input("enter choice"))
    if choice == 1:
        maximum_no(lst)
        #print(a)
    elif choice == 2:
        b=minimum_no(lst)
    elif choice == 3:
        c=ascending_order(lst)
    elif choice == 4:
        d=descending_order(lst)
    else:
        print("close")
        break
