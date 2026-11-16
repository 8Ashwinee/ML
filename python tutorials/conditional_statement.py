
#a = int(input(" Enter a number :"))

#if a>0:
#    print("Number is positive")
#elif a<0:
#    print("Number is negative")    
#elif a==0:
#    print("Number is also positive")

'''
username="ashwinee"
password="123" 


u = input(" ENTER A USERNNAME :")
p = input(" ENTER A PASSWORD :")

if u==username and p==password :
    print("login successfull")
elif u!=username or p!=password:
    print("login failed")

'''

"""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
"""


#username = "ashwinee"
#password = "123"

'''
u = input("ENTER YOUR USERNAME :")
if u == username:
    p = input("ENTER YOUR PASSWORD :")
    if p == password:
        print("LOGIN SUCCESSFULL..")
    elif p!=password:
        print("INVALID PASSWORD")

elif u!=username:
    print("INVALID USERNAME") 
    '''


# wap 

name = input("ENTER YOUR NAME : ")
rollno = input("ENTER YOUR ROLLNO. : ")
physics = int(input("ENTER YOUR PHYSICS MARKS : "))
chemistry= int(input("ENTER YOUR CHEMISTRY MARKS : "))
maths= int(input("ENTER YOUR MATHS MARKS : "))
english = int(input("ENTER YOUR ENGLISH MARKS : "))
hindi = int(input("ENTER YOUR HINDI MARKS : "))


total_marks = (int(physics) + int(chemistry) + int(maths) + int(english) + int(hindi))
percentage = (total_marks / 5)


if percentage >= 90:
    print("Grade A+")
    print("Name:",name)
    print("Rollno:",rollno)
    print("Physics marks:",physics)
    print("Chemistry marks:",chemistry)
    print("Maths marks:",maths)
    print("English marks:",english)
    print("Hindi marks:",hindi)

elif percentage <90 >=70:
    print("Grade A")
    print("Name:",name)
    print("Rollno:",rollno)
    print("Physics marks:",physics)
    print("Chemistry marks:",chemistry)
    print("Maths marks:",maths)
    print("English marks:",english)
    print("Hindi marks:",hindi)

elif percentage <70 >=50:
    print("Grade B")
    print("Name:",name)
    print("Rollno:",rollno)
    print("Physics marks:",physics)
    print("Chemistry marks:",chemistry)
    print("Maths marks:",maths)
    print("English marks:",english)
    print("Hindi marks:",hindi)    

elif percentage <50 >=33:
    print("Grade C")
    print("Name:",name)
    print("Rollno:",rollno)
    print("Physics marks:",physics)
    print("Chemistry marks:",chemistry)
    print("Maths marks:",maths)
    print("English marks:",english)
    print("Hindi marks:",hindi)

elif percentage <33:
    print("FAIL")
    print("Name:",name)
    print("Rollno:",rollno)
    print("Physics marks:",physics)
    print("Chemistry marks:",chemistry)
    print("Maths marks:",maths)
    print("English marks:",english)
    print("Hindi marks:",hindi)

    