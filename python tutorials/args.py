# This script takes a number of inputs from the user, stores them in a list, and then calculates the sum of those numbers.
"""
n = int(input("Enter the number of values you want to sum: "))
nums = []
for i in range(n):
    v = int(input("enter a number : "))
    nums.append(v)
print(nums)

def sum(x):
    count = 0
    for i in x:
        count +=i
        print("The sum of given numbers is : ",count)
sum(nums)
"""
"#________________________________________________________________________________________"

n = int(input("enter number of students : "))
biodata = []
for i in range(n):
    print("Enter details for student", i + 1)
    name = input("Enter name: ")
    city = input("Enter city: ")
    age = int(input("Enter age: "))
    biodata.append((name, city, age))
#print(biodata)

def student_info(name,city,age):
    print("Name:", name , " City:", city, " Age:", age)
 
for student in biodata:
    student_info(student[0], student[1],student[2])

#________________________________________________________________________________________ 
# kwargs example:
