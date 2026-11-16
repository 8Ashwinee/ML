#WAP to find the SUM of the 2 numbers:
"""
def sum():
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print("sum of 2 number is: ", a+b)

sum()    
"""
#WAP to reverse given string
"""
def reverse_string():
    string = input("enter a string: ")
    reverse_string = string[::-1]
    print("reversed_string id :"< reverse_string)

reverse_string()
"""
#WAP to SWAP first & last element of the list
"""
def swap():
    list = [1,2,3,4,5,6,7,]
    print("original list is : ",list)
    list[0],list[-1] = list[-1],list[0]
    print("swapped list is:",list)

swap()    
"""
#WAP to SWAP 2nd & second last element of the list
"""
def swap2():
    list = [1,2,3,4,5,6,7,]
    print("original list is : ",list)
    list[1],list[-2] = list[-2],list[1]
    print("swapped list is:",list)

swap2()    
"""
#WAP to find the DUPLICATE values of the list:
"""
def duplicate():
    list = [1,2,3,4,5,6,7,8,9,1,2,3]
    print("original list is : ",list)
    duplicate_values = []
    for i in list:
        if list.count(i) > 1 and i not in duplicate_values:
            duplicate_values.append(i)
    print("duplicate values are: ",duplicate_values)

duplicate()
"""
# WAP to find the FACTORIAL given value
'''
def fact():
    num = int(input("enter a number : "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("factorial of ", num , "is:", factorial)

fact()
'''
#WAP to find the word is symmetrical or not:
'''
def symmetrical():
    s = input("enter your string :")
    len = s[::-1]
    if: 
    print(s, "is symmetrical")
    else:
        print(s, "is not symmetrical")
'''
#WAP to find word is palindrome or not:

