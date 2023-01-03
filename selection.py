list1=[20,30,25,10,12]
list2=[]
print(list1)

while list1:
    min=list1[0]
    for x in list1:
        if x < min:
            min=x
    list1.append(min)
print(list1)


"""min=list1[0]
while list1:
    for i in range(list1):
        if i >= min:
            min=i
    print(min)"""
