"""from choice import max_no, min_no
lst=[]
while True:
    print("2.Maximum no")
    print("3.Minimum no")
    print("4.Ascending  order")
    print("5.Dessending order")
    choice = int(input("enter choice"))
    if choice == 2:
        max_no()

    elif choice == 3:
        min_no()
        break
    else:
        print("close")
        break"""




def maximum_no(lst):

    #print(lst)
    max_no = lst[0]
    for no in range(len(lst)):
        if lst[no] >= max_no:
            max_no = lst[no]
            #return max_no

    print('Max No. is: {}'.format(max_no))


def minimum_no(lst):

    for no in range(len(lst)):
        min1_no = lst[0]
        if lst[no] <= min1_no:
            min1_no = lst[no]

    print('Min No. is: {}'.format(min1_no))
