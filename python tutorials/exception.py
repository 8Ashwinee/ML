# exception handling
'''

print("program start")

try:
    a = int(input("enter first number : "))
    b = int(input("enter second number : "))
    print(a+b)
except Exception as ashwinee:
    print(ashwinee)

print("program continue")
'''

#----------------------------------------
'''
list = [1,2,3,4,5,6,7]
try:
    r = int(input("Enter a list you want to add : "))
    list.append(r)
    print(list)
except Exception as mistake:
    print(mistake)
print("continue.....")    
'''
#-----------------------------------------------
# static calculator by using exceptional handling if else elif & functions :

def addition():
    try:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("sum of numbers is : ", a + b)
    except Exception as error:
        print(error)

def subtraction():
    try:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("sub of numbers is : ", a - b)
    except Exception as error:
        print(error)

def multiplication():
    try:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("multiplication of numbers is : ", a * b)
    except Exception as error:
        print(error)

def division():
    try:
        a = int(input("enter first number : "))
        b = int(input("enter second number : "))
        print("division of numbers is : ", a / b)
    except Exception as error:
        print(error)

while True:
    print("press 1 for +")
    print("press 2 for -")
    print("press 3 for *")
    print("press 4 for /")
    print("press 5 for exit")

    c = input("ENTER YOUR NUMBER : ")

    if c == "1":
        addition()
    elif c == "2":
        subtraction()
    elif c == "3":
        multiplication()
    elif c == "4":
        division()
    elif c == "5":
        print("THANKS FOR USING OUR CALCULATOR")
        break
    else:
        print("INVALID INPUT PLEASE TRY AGAIN")
print("program continue......")        

#--------------------------------------------------