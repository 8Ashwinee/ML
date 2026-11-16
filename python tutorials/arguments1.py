# non default arguments:
"""
def student(name, age):
    print("Name is",name)
    print("Age is",age)

student("Ashwinee", 19) 
student("xyz",20)   
student("abc", 21)

def my_function(name , age):
    print(name," ",age)
"""
""""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def sum(x,y):
    print("sum of two number is: ", x + y)

sum(a,b)

num = int(input("Enter a number to find its factorial: "))
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial of", n, "is:", result)


factorial(num)
"""
# default arguments:
"""
n = int(input("Enter number: "))
def student(name, roll_no, institution="ABC University"):
    print(name , " ", roll_no, " ", institution)

for i in range(n):
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    student(name, roll_no)   
#____________________________________________________________________________ 
    
def user_info(n , c,  a):
    print("Name:", n)
    print("City:", c)
    print("Age:", a)

user_info("ashwinee","xyz",19)
user_info("xyz","abc",20)    
"""
#_______________________________________________________________________________
"""
n = int(input("Enter a number : "))
def student_info(n , c, a):
    print("Name:", n, " City:", c, " Age:", a)
for i in range(n):

    print("Enter details for student", i + 1)
n = input("Enter name: ")
c = input("Enter city: ")
a = int(input("Enter age: ")) 
student_info(n,c,a)   
"""