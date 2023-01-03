list1 = [50,10,20,3,5]
list2 = []

while list1:
    min = list1[0]
    for x in list1:
        if x < min:
            min = x
    list1.append(min)
    list2.remove(min)

print(list1)