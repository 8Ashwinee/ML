# STATIC CALCULATOR FOR 2 DIGIT NUMBERS : (+,-,*,/,)

while 2==2:
    print("press 1 for ""+")
    print("press 2 for ""-")
    print("press 3 for ""*")
    print("press 4 for ""/")
    print("press 5 for ""exit")

    c = input(" ENTER YOUR NUMBER : ")

    if c == "1":
        value1 = int(input("enter first number : "))
        value2 = int(input("enter second number : "))
        print("sum of 2 number is : ", value1 + value2)
    
    elif c == "2":
        value1 = int(input("enter first number :"))
        value2 = int(input("enter second number :"))
        print("subtraction of 2 number is :", value1-value2)

    elif c == "3":
        value1 = int(input("enter first number :"))    
        value2 = int(input("enter second number :"))    
        print("multiplication of 2 number is :", value1*value2)

    elif c == "4":
        value1 = int(input("enter your number : ",))
        value2 = int(input("enter second number : ",))
        print("division of 2 number is :", value1/value2)

    elif c =="5":
        print(" THANKS FOR USING OUR CALCULATOR")
        break

    else:
        print("INVALID INPUT PLEASE TRY AGAIN")

    print("program continue.....")    


