# functions:

def addition():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    print("sum of 2 number is : ", value1 + value2)
    
def substraction():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    print("sum of 2 number is : ", value1 - value2)

def multiplication():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    print("sum of 2 number is : ", value1 * value2)

def division():
    value1 = int(input("enter first number : "))
    value2 = int(input("enter second number : "))
    print("sum of 2 number is : ", value1 / value2)
        
        
while 2==2:
    print("press 1 for ""+")
    print("press 2 for ""-")
    print("press 3 for ""*")
    print("press 4 for ""/")
    print("press 5 for ""exit")

    c = input(" ENTER YOUR NUMBER : ")

    if c == "1":
        addition()

    elif c =="2":
        substraction()

    elif c == "3":
        multiplication()

    elif c == "4":
        division()

    elif c =="5":
        print(" THANKS FOR USING OUR CALCULATOR")
 
else:
    print("INVALID INPUT PLEASE TRY AGAIN")

print("program continue.....")    
