# Find numbers divisible by 7 and multiples of 5 between 1500 and 2700 (inclusive)
'''
a =[]
for x in a (1500,2701):
    if (x % 7 ==0) and (x % 5 == 0):
        a.append(str(x))

print(','.join(a))
'''
'''
list = [-1,2,0,-4,5]
boolean_list = [bool(x) for x in list]
print(boolean_list)
'''
#WAP to print all even numbers between 1 to 50
'''
for i in range(2,51,2):
    print(i)

# WAP print all odd numbers between 1 to 50
for i in range(1,50,2):
    print(i)

#WAP to print all numbers those are divisible by 7 between 1 to 50:
for i in range(7,50,7):
    print (i)
'''
#WAP to print the multiplication table of 4
'''
t =4
for i in range(4,41,4):
    print(i)
'''
# WAP to print the multiplication table of given number 
'''
t= int(input("enter your number:  "))
for i in range(1, 11):
    print(f"{t} * {i} = {t*i}")

num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
        factorial *= i
print("Factorial of {num} is {factorial}")
'''
#WAP to reverse a string
# check palindrome
'''
s = input("enter your string :")
r = ""
for i in s:
    r = i + r
    if s == r:
        print("{s} is a palindrome")
    elif s!= r:
        print("{s} is not a palindrome")

# WAP add item in a list 
fruits =[]
n = int(input(" ENTER HOW MANY FRUITS YOU WANT TO ADD : "))
for i in range(n):
    value = input("enter a fruit name :")
    fruits.append(value)
print(fruits)

# check palindrome
s = input("enter your string: ")
r = s[::-1]
if s==r:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")

# check symmetrical :
s = input("enter your string :")
len = s[::-1]
if: print(s, "is symmetrical")
else:
    print(s, "is not symmetrical")
'''
#WAP for reverse string

a = input("ENTER A DESIRABLE STRING : ")
r = ""
for i in a:
    r = i + r
    print("REVERSED STRING IS :" + r)