"""def welcome_msg(name):
    print('Welcome: ',name)

def hello_msg(name):
    print('Hello: ',name)

def sum(a,b):
    return a+b"""
list1 = []
def enter_details():
    name = input("enter name: ")
    age = input("enter age")
    email = input("enter email")
    phn_no = input("enter phn_no")
    dict1 = {
        "name": name,
        "age": age,
        "email": email,
        "phn_no": phn_no,
    }
    list1.append(dict1)
    # print(list1)


def search_detaills():
    i = input("enter email you have to find:")
    for k in list1:
        if i in k.values():
            print("your name is:{}".format(k['name']))
            print("your age is:{}".format(k['age']))
            print("your email is:{}".format(k['email']))
            print("your phn_no is:{}".format(k['phn_no']))
        else:
            print("not present in the list")


def delete_details():
    i = input("enter email you have to find:")
    for k in range(len(list1)):
        if list1[k]["email"] == i:
            del list1[k]
            # print(k)
            print("record deleted sucessfully")
            break

    else:
        print("data not found")


def update_details():
    i = input("enter email you have to find:")
    for k in list1:
        if i in k.values():
            print("your name is:{}".format(k['name']))
            print("your age is:{}".format(k['age']))
            print("your email is:{}".format(k['email']))
            print("your phn_no is:{}".format(k['phn_no']))

            name1 = input("enter name:")
            age1 = input("enter age:")
            phn_no1 = input("enter phn_no:")

            k.update({"name": name1})
            k.update({"age": age1})
            k.update({"phn_no": phn_no1})


def printdetails():
    if list1:
        for i in list1:
            print("your name is:{}".format(i['name']))
            print("your age is:{}".format(i['age']))
            print("your email is:{}".format(i['email']))
            print("your phn_no is:{}".format(i['phn_no']))
            print("######################")


    else:
        print("no record found")