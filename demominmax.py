lst=[]
for i in range(0,5):
    no=int(input("enter No {}".format(i+1)))
    lst.append(no)

max_no = lst[0]
for no in range(len(lst)):
    if lst[no] >= max_no:
       lst[no] = max_no
       lst.append((lst[no]))
print("max no is:{} ".format(lst[no]))

