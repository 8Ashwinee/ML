#WAP to count no. of characters in given strings:
'''
x = "apple"
x = input("ENTER A STRING : ")
count = 0
for i in x:
    count +=1
print("NUMBER OF CHARACTERS IN THE STRING IS : ", count)
'''
#---------------------------------------------------------------------------
#WAP to print list in capital letters:
'''
s = ["apple","banana","strwaberry","orange","kiwi","grapes","mango","peach","pear","pomegranate"]
for i in s:
    print(i.upper())
'''
#-----------------------------------------------------------------------------
# WAP to print the length of string:
'''
s = ["apple","banana","strwaberry","orange","kiwi","grapes","mango","peach","pear","pomegranate"]
for i in s:
    print(len(i))
    '''
#-----------------------------------------------------------------------------
# WAP to print all ODD numbers of the list:
'''
n = [1,2,3,4,5,6,7,8,9,10]
for i in n:
    if i % 2!=0:
        print(i)
'''        
#-----------------------------------------------------------------------------
# WAP to print all EVEN numbers of the list:
'''
s = int(input("enter how many numbers you want to enter: "))
n = []
for i in range(s):
    x = int(input("enter a number: "))
    n.append(x)
for i in n:
    if i % 2 == 0:
        print(i)
        '''

#WAP to find the SQUARE of all numbers of the list:
'''
s = [1,2,3,4,5,6,7,8,9,10]
for i in s:
    square = i**2
    print(f"Square of {i} is {square}")
    '''
#-----------------------------------------------------------------------------
#WAP to find the CUBE of all numbers of the list:
'''
s = [1,2,3,4,5,6,7,8,9,10]
for i in s:
    cube = i**3
    print("cube of ",i,"is",cube)
'''
# WAP to find the square of even numbers in a list
'''
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in s:
    if num % 2 == 0:
        square = num ** 2
        print(num,"squared is",square)
'''
#WAP to find word is symmetrical or not:
"""
word = input("ENTER A WORD : ")
length =len(word)
word = length//2
#print(word)
part1=""
part2=""
z = 1
for i in word:
    if z <= length//2:
        part1 += i
        z += 1
    elif z > length//2:
        part2 += i
        z += 1  
if part1 == part2:
    print("The word is symmetrical")
else:
    print("The word is not symmetrical")
   """ 
#-----------------------------------------------------------------------------
#patterns
#check armstrong number
#check prime number
# WAP to check if a number is prime

n = int(input("Enter a number to check if it is prime: "))

for i in range(2,n):
    if n% i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# WAP to print a right-angled triangle pattern of stars
'''
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)
'''

# WAP to print a pyramid pattern of stars
'''
rows = int(input("Enter the number of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
'''

# WAP to print an inverted right-angled triangle pattern of stars
'''
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    print("*" * i)
    '''