def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def divition(a, b):
    return a / b


num1 = int(input("enter no"))
num2 = int(input("enter no"))

while True:
    print("1.Addition:")
    print("2.subtraction:")
    print("3.multiplication:")
    print("4.divition:")
    choice = (int(input("enter choice:")))
    if choice == 1:
        print("addition:", addition(num1, num2))
    elif choice == 2:
        print("subtraction:", subtraction(num1, num2))
    elif choice == 3:
        print("multiplication:", multiplication(num1, num2))
    elif choice == 4:
        print("divition:", divition(num1, num2))
    else:
        print("quit")
        break




