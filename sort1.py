

# 1.add number
while True:
    print("1.Add numbers")
    print("2.Assending order")
    print("3.Dessending order")
    print("4.Quit")

    b=int(input("enter choice"))
    if b==1:
        a = int(input("enter total nos:"))
        lst = []
        for i in range(a):
            no = int(input("enter no:"))
            lst.append(no)
#2.Assending order

    if b == 2:
        """a = int(input("enter total nos:"))
        lst = []
        for i in range(a):
            no = int(input("enter no:"))
            lst.append(no)"""

        for i in range(a):
            for j in range(i+1, a):
                if (lst[i] >= lst[j]):
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
            print(lst[i])

# 3. Dessending order

    if b == 3:
        """ a = int(input("enter total nos:"))
        lst = []
        for i in range(a):
            no = int(input("enter no:"))
            lst.append(no)"""

        for i in range(a):
            for j in range(i + 1, a):
                if (lst[i] <= lst[j]):
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
            print(lst[i])

# 4. quit

    if b == 4:
        print("quit")
        break

