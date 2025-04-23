import time
#print("Hello")

# Variables are the containers for storing data 

# x = 2
# print("The number is " + str(x))

# x = 3
# y =4 
# print("The sum of x and y is " + str(x + y))


# A String is a sequence of characters enclosed in either single or doublw quotes 

# str = "Hi dude"
# print(str[0:2]) # slicing
# print(len(str)) # length
# print(str.upper()) # to upperCase

#list are ordered and the mutable collection of items , which can be of any datatype

# stuff = [ 'book', 'pen', 12, 'mobile' , 1.22]
# print(stuff)
# print(stuff[0])
# stuff.pop()
# print(stuff)
# stuff.reverse()
# print(stuff)

#Taking input from user 
# name = input("Enter your name ")
# age = int(input("Enter your age "))
# print("Hello " , name, " and you are ", str(age) , "years old" )

#Print formatting 
# name = input("Enter your name ")
# age = int(input("Enter your age "))
# print(f"Hi,Your name {name} and you are {age} years old")

# Convert a string input into an integer and add 10 to it
# num = input("Enter the number to convert into to add 10 ")
# print(int(num) + 10)

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# print(f"The Sum of {num1} and {num2} is {num1+num2}")
# print(f"The Substraction of {num1} and {num2} is {num1-num2}")
# print(f"The Multiplication of {num1} and {num2} is {num1*num2}")
# print(f"The Division of {num1} and {num2} is {num1/num2}")

# Task
# Ask the user for:Their full name,Their birth year
# Calculate their current age (Assume the current year is 2025)
# Print a message like: "Hello [Name], you are [Age] years old in 2025."
# Also, tell them how many years are left until they turn 100 years old.
# name = input("Enter your full name ")
# year = int(input("Enter your birth year "))
# current_age = (2025 - year)
# print(f"Hello {name}, you are {current_age} years old in 2025")
# expiry = (100-current_age)
# print(f"{expiry} are left before you turn 100 years old ")

# Control Flow : These are used to decide the flow of the code while executing 
#if , else, elif , comparision operator, logical operator

# age = int(input("Enter your age : "))
# if age >= 18:
#     print("Court : State vs A nobody is not applied ")
# else:
#     print("Court : State vs A nobody is applied "

# marks = int(input("Enter your marks "))
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75 and marks <=90:
#     print("Grade B")
# else:
#     print("Manchiga saduvuko bidda")

# Ask the user for their age and check:
# If age < 13 → "Child"
# If 13 <= age < 18 → "Teen"
# If 18 <= age < 60 → "Adult"
# Else → "Senior"

# age = int(input("Enter you age : "))
# if age < 13:
#     print("Child")
# elif age >=13 and age < 18:
#     print("Teen")
# elif age >= 18 and age < 60 :
#     print("Adult")
# else:
#     print("Senior")

# num = int(input("Enter a number : "))
# if num > 0 :
#     print(f"{num} is positive")
# elif num <0 :
#     print(f"{num} is negative")
# elif num == 0 :
#     print(f"{num} is zero") 
# else:
#     print("Invalid Input")

# Write a Python program that:
# Asks the user to enter a number.
# Checks:
# If the number is divisible by both 3 and 5, print "FizzBuzz"
# If divisible by only 3, print "Fizz"
# If divisible by only 5, print "Buzz"
# Otherwise, print the number itself.

# num = int(input("Enter a number : "))
# if num % 3 == 0 and num % 5 ==0 :
#      print("FizzBuzz")
# elif num % 3 ==0 :\
#      print("Fizz")
# elif num % 5 ==0 : 
#     print("Buzz")
# else:
#      print(num)

# Loops are used to iterate a block of code until the condition is true like while, for, for else , range, break and continue
#While
# count = 1
# while count <=5 :
#     print("Count is", count)
#     time.sleep(1)
#     count+=1

#for loop in range

# for i in range(1,10):
#     print(" i : ",i)

#loop with break
# for i in range(0,10):
#     if i ==5:
#         break
#     print(i)

# Loop with continue
# for i in range(0,10):
#     if i ==5:
#         continue
#     print(i)

#Print numbers from 1 to 10 using a while loop.
#Print even numbers between 1 and 20 using a for loop.
#Ask the user for a number and print the multiplication table up to 10.
#Print numbers 1 to 10, but skip 5 using continue.
#Stop the loop if the number is 7 using break.

# i = 1
# while i<=10:
#     print("i is", i)
#     i+=1

# for i in range(0,21,2):
#     print(i)
# for i in range(1,21):
#     if i % 2 ==0 :
#         print(f"{i} is Even")
#     else: 
#         print(f"{i} is Odd")

# num = int(input("Enter the number : "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num * i}")

# for i in range(1,11):
#     if i ==5:
#         continue
#     print(i)

# for i in range(1,10):
#     if i == 7 :
#         break
#     print(i)

#Data Structure : List, Tuple, Sets, Dictionaries
#List : List are ordererd, changeable and also allows duplicates 
# cars = ["Tata", "Toyota", "Ferrari", "Honda"]
# print(cars[2])
# cars.append("Hyundai")
# print(cars)
# cars[2]= "Suzuki"
# print(cars)

#Tuples are also like list, but they are immutable, the changes cannot be made
# tup = ('bow', 'axe', 'arrow', 'mace')
# print(tup)
# tup[3] = "chariot"
# print(tup)

#sets : unordered, but no duplicates 
# nums = {1,2,2,3,3,2,11,1,2}
# print(nums)

#Dictionaries : These are used to store in the form of key: value pairs , which can be unordered 
# Student = {
#     "name" : "Sai",
#     "age" : 24,
#     "course" : "Python"
# }
# print(Student["name"])
# Student["Email"] = "Sai@gmail.com"
# print(Student)

# Create a list of 5 of your favorite movies and: Print the third movie, Replace the second movie, Append a new movie to the end
# Create a tuple of 4 programming languages and print them in a loop
# Create a set of your favorite fruits, add one more, and remove one
# Create a dictionary with:Your name, Age, Favorite languageAdd a new key: “is_student” with value True
# Print all keys and values

# fav_movies = ['The Godfather', "The Dark Knight", "Mayabazar", "Pulp fiction", "Shankarabharanam"]
# print(fav_movies[2])
# fav_movies[1]="Inception"
# fav_movies.append("The Dark Knight")
# print(fav_movies)

# tup = ('Java', 'Python', 'JavaScript', 'C')
# for i in tup:
#     print(i)

# fruits = {"Mango", "Banana","Apple"}
# fruits.add("Pomegranate")
# print(fruits)
# fruits.remove("Banana")
# print(fruits)

# details = {
#     "Name" : "Sai",
#     "age" : 24,
#     "fav_lang" : "Python"
# }
# print(details)
# details['is_student'] = True;
# print(details)

students = [
    {
        "Name" : "Sai",
        "Age" : 24,
        "Skills" : ("Python", "C++"),
        "Certifications" : {"AWS" , "GCP"}
    },
    {
        "Name" : "Deeraj",
        "Age" : 26,
        "Skills" : ("Java", "React.js"),
        "Certifications" : {"Full Stack" , "AWS"}
    },
    {
        "Name" : "Vaishnavi",
        "Age" : 22,
        "Skills" : ("Linux", "Python"),
        "Certifications" : {"Udemy", "AWS" , "GCP"}
    },
    {
        "Name" : "Goutham",
        "Age" : 25,
        "Skills" : ("C", "Frontend"),
        "Certifications" : {"Infosys" , "AWS", "Udemy"}
    },
]


# print(students)
new_student = {
    "Name" : "Pooja",
    "Age" : 24,
    "Skills" : ("Java", "Python"),
    "Certifications" : {"Google", "Infosys" , "AWS"}
}
students.append(new_student)
# print(students)

# for i in students:
#     if i["Age"] < 25 and "Python" in i["Skills"] :
#         print(i["Name"])

# common_certs = students[0]["Certifications"]
# for student in students[1:]:
#     common_certs = common_certs & student["Certifications"]
# print(common_certs)
# sum = 0
# for i in students:
#     sum = sum + i["Age"]
# avg = sum / len(students)
# print(f"The Average age of students is {avg}")


# for i in students:
#     Names = i["Name"]
#     print(Names.upper())

# total_skills =0 
# for i in students:
#     length = len(i["Skills"])
#     total_skills = total_skills + length
# print(f"The total number of skills are {total_skills}")

# total_certs = 0 
# for i in students:
#     certs = len(i["Certifications"])
#     total_certs = total_certs + certs
# print(f"The total number of certifications are {total_certs}")


#fruits = ["apple", "banana", "cherry", "date"]
#Print the first and last element of the list.
# print(fruits[0])
# print(fruits[-1])

#Append "kiwi" to the list, Remove "banana" from the list,Print the updated list
# fruits.append("Kiwi")
# fruits.remove("banana")
# print(fruits)

#Reverse the list using slicing.
#print(fruits[::-1])

# colors = ["red", "blue", "red", "green", "blue", "red"]
# print(f"There are {colors.count("red")} RED's")

#Find the max and second max
# nums = [12, 45, 78, 23, 56, 89, 78]
# nums.sort()
# print(f"The largest number in the list is {nums[-1]}")
# print(f"The second number in the list is {nums[-2]}")

#Remove Duplicates Without Using Set
# raw = [1, 2, 2, 3, 4, 4, 5]
# new_raw = []
# for i in raw:
#     if i not in new_raw:
#         new_raw.append(i)
# print(new_raw)
    
#data = [("John", 25), ("Jane", 30), ("John", 25), ("Doe", 22), ("Jane", 30)]
# data = [("John", 25), ("Jane", 30), ("John", 28), ("Doe", 22), ("Jane", 35)]
# seen_names= set()
# new_data = []
# for i in data:
#     #print(i[0])
#     if i[0] not in seen_names:
#         new_data.append(i)
#         seen_names.add(i[0])
# print(seen_names)
# print(new_data)

# people = [("John", 25), ("Jane", 30), ("Doe", 25), ("Alice", 30), ("Bob", 22)]
# aged_sort = {}

# for name, age in people:
#     #print(name)
#     #print(age)
#     if age in aged_sort:
#         aged_sort[age].append(name)
#     else:
#         aged_sort[age] = [name]
# print(aged_sort)

#Challenge 1: Count Frequency of Elements
#Given a list of elements, count the frequency of each element and store it in a dictionary.

# data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# countFeq = {}
# count = 1
# for i in data:
#     #print(i)
#     if i not in countFeq:
#         countFeq[i] = count
#     else:
#         countFeq[i] += 1 
# print(countFeq)

# Write a program to find the most frequent element in a list, but the catch is: if there are multiple elements with the same maximum frequency, return the smallest element. If the list is empty, return a message saying so.

data = [3, 1, 4, 1, 5, 5, 5, 1, 2, 2, 3, 4, 3, 2, 1, 2, 4, 3, 2, 1]
new_data = {}
most_repeat = []
count = 1
for i in data:
    #print(i)
    if i not in new_data:
        new_data[i] = count
    else :
        new_data[i] += 1 
print(new_data)
# for j in new_data:
#     print(j)