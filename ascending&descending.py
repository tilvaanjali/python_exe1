
lst = []
def addvalue():
    a = int(input("enter total nos:"))
    for i in range(a):
        no = int(input("enter no:"))
        lst.append(no)

def assending():
    temp = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])

def dessending():
    temp = 0
    print("Dessending order")
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i] <= lst[j]):
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
        print(lst[i])


while True:
    print("1.Add numbers")
    print("2.Assending order")
    print("3.Dessending order")
    print("4.Quit")
    choice = int(input("enter choice"))
    if choice == 1:
        addvalue()
    elif choice == 2:
        assending()
    elif choice == 3:
        dessending()
    else:
        print("quit")
        break
