list1 = [1, 2, 3, 4, 5, 6, 8]
list2 = [6, 7, 8, 9, 10, 11, 12,13]
# i=0
print("odd index no of List1 is:")
for odd in range(list1[1], list1[6], 2):
    print(odd)

print("even index no of list2 is:")
for even in range(list2[0], list2[7], 2):
    print(even)
