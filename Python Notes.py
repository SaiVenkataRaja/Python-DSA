#print("Hello")

# -- Variable is the container for storing data or it also can be defined as the name that refers to a value
# -- Python is dynamically type, so we do not need to declare the type of variable

# name = "Sai"
# age = 24
# print(f"Hi, {name} , you are {age} years old")

#We can also reassign the variable for different types
# x=10
# x="Ten"
# print(x)

#Common datatypes :int 8 , float 1.2, str "Hi", bool True/False, list [], tuple(), dic {"":""}, sets {}

# -- Order of instructions (sequence of execution) --
#Python runs code line by line from top to bottom unless there is a control structure
# y = x + 5 
# x = 5
# print(y)


#BODMAS (Operator precedence) Brackets, Orders (Powers), Division, Multiplication, Addition, Substraction

#Playing with strings 
#Python strings are sequence of characters and we can slice, concatenate, repeat and access \

# name = "Sai"
# print(name[0]) #Indexing
# print(name[0:2]) #Slicing
# print("Hello " + name) #Concatenate
# print(name * 3) #Repeat
# print(len(name)) #Length

#Type conversion : This lets us to convert one data type to another 
#There are two types of conversions : Implicit(Conversion does automatically) and Explicit (Doing it manually)
#Implicit
# num1 = 1
# num2 = 3.3
# num3 = num1 + num2
# print(type(num1))
# print(type(num2))
# print(type(num3))
# #Explicit
# age = int("24")
# print(type(age))
# intgs = str(123)
# print(type(intgs))

# ------------------- Relational and Logical Operators ---
# There are used in conditions to compare values or combine conditions
# Relational (Comparision Operators)
#       " == " equals to
#       " != " Not equal to
#       " > "  Greater than
#       " < "  Less than
#       " >= " greater or equals
#       " <= " Less or equals
# 
# -------------------- Logical Operators
#       and - both conditions are true
#       or - at least one is true
#       not - true if false

# ---------------------- Loops are used to  iterate a block of code until it is true
# While loops are used when you do not know about how many times to run - it keeps going as long as a condition is True

# count = 1
# while count <= 5:
#     print(count)
#     count+=1

#------------------------For Loop : iterates until the condition is true, it is used to iterate over a sequence like a string, list and range of numbers

# for i in range(5):
#     print(i)
#Looping through string 
# for i in "Sai":
#     print(i)

# ------------------------ String methods : are like inbuilt operations on strings like .lower, .upper etc
# name = "    Sai"
# print(name.lower())
# print(name.upper())
# print(name.strip())
# print(name.replace("Sai", "Venkat"))
# name = "Sai, Venkata , Raja"
# print(name.split(","))
# #joining the list
# names = ["Sai", "Venkata", "Raja"]
# print(" ".join(names))

# url = "https://cesltd.com"
# print(url.startswith("htt"))
# print(url.endswith("om"))

#------------------------Nested loop : is the loop inside another loop

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

#------------------------Loop control statements : break, continue and pass
#
#Break : used to stop a loop completely, when the condition is met
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

#Continue : Skips the current iteration and moves to the next 
# for i in range(10):
#     if i == 6:
#         continue
#     print(i)

# pass : does nothing , it is just a placeholder to avoid syntax errors
# for i in range(3):
#     pass


#-----------------------Comparing strings
#String comparision is often used to validate input, sort list, check for duplicates, match keywords
# print("apple" == "apple")
# print("Apple" == "apple")
# print("apple" < 'banana')
# converting the string to either uppercase or lowercase, so no case sensitive issue
# print('apple'.upper() == "ApPle".upper())


# ------------------ List -----------
#List is collection that allows us to store multiple items, like numbers or strings in a single variable
#Lists are ordererd, mutable and can store different type of data like ints, strings, even other lists
# my_list = [1,2,4,4]
# print(my_list[0]) #indexing
# print(my_list)
# my_list[2] = 10 #modifying
# print(my_list)
# my_list.append("Thala for a reason") #adds at the end
# print(my_list)
# my_list.insert(2, 7) #inserts at specific index position
# print(my_list)
# my_list.remove(7) # removes the number (item)
# print(my_list)
# my_list.pop(0) # removes by index
# print(my_list)
# print(my_list[1:4]) # slicing
# print(len(my_list)) # length of list
#Nested lists : is a list inside another list
# nested_list = [[1,2,3], [4,5,6], [7,8,9]] #The outer contains 3 lists and inner listb has 3 elements
# print(nested_list[0])
# print(nested_list[0][1])
#
#use nested loops in the nested list

# ------------------ Tuple -----------------
#Tuple : is a collection of ordered, immutable (unchangable) elements in python
# we can't modify it after creation, so that we  can't add, removee or change values
# tup = (1,2,3)
# print(tup)
# #It can also contain different datatypes
# tupl = (1,"hello", 3.5)

# #A single tuple must have a comma, if not , it does not consider as a tuple 
# tuple = (4, )
# print(tuple)

#Accessing tuple elements 
# t = (1,2,3)
# print(t[0]) #index

#Tuple unpacking
# t= (4,5,6)
# a,b,c = t
# print(a, b, c)

#Tuple methods 
# t = (1,2,3,4,4)
# print(t.count(4)) #Returns the number of times , the number appears
# print(t.index(3)) #Returns the first index of the value

# ---------------- Dictionaries -------------------
# Dictionary is an unordered, mutable and indexed collection of key- value pairs
# my_dict = {
#     "name": "Sai",
#     "age" : 24,
#     "role" : "Developer"
# }
# Values can be of any datatype
# Basic operations with Dictioanries
# person = {
#     "name" : "Sai",
#     "age" : 24,
#     "role" : "Developer"
# }
# print(person["name"])
# print(person.get("name")) # This also works the same way
# #adding new key-pair value 
# person["location"] = "Hyderabad"
# print(person)

# #Updating a value 
# person["age"] = 25

# print(person)
# #Deleting a key-pair value
# del person["location"]
# print(person)

# #checking if a key exists :
# if "name" in person :
#     print("Name exists")

# #Looping through dictionary
# for i, j in person.items():
#     print(f"{i}: {j}")

#Dictionary methods : 
# person = {
#     "name" : "Sai",
#     "age" : 24,
#     "role" : "Developer"
# }
# print(person.keys()) # returns keys
# print(person.values()) # returns values
# print(person.items()) # returns a key-values as tuples
# print(person.get("name")) #Returns value of key, if the key does not exist , it returns none 
# person.pop("age") # removes the specified key
# print(person) 
# person.clear() #Removes all items

# Nested Dictionaries : means a dictionary inside another dictionary 
# These are helpful when representing complex data structures like group of students or multiple records 
# students = {
#     "student1": {
#         "name": "Ravi",
#         "age": 22, 
#         "marks": [80, 85, 90]
#         },
#     "student2": {
#         "name": "Priya",
#         "age": 21,
#         "marks": [70, 75, 80]
#         },
#     "student3": {
#         "name": "Kiran",
#         "age": 23, 
#         "marks": [60, 65, 70]
#         }
# }


# ---------------------------Sets ------------------------
# Set is an unordered, unindexed and mutable collection of unique items (similar to mathematical sets)
# it is mainly used to store non-duplicate values and perform operations like union, intersection, difference etc
# fruits = {'apple','apple', 'banana', 'mango'}
# nums = set([1,2,4,5]) # using set constructor 
# #sets automatically removes duplicates and we cannot access elements by index
# print(fruits)
# s= {1,2,3,4}
# s.add(5) #adds 5 to set
# print(s)

# s.remove(2) #removes 2 from set
# print(s)

# s.pop() #removes random item
# print(s)

# s.clear() #empties the set
# print(s)

# #set operations like in math 
# a = {1,2,3,5}
# b = {4,5,6}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b))
# #membership testing
# if 3 in a:
#     print("3 is in the set")

#Set comprehension
# sq = {x*x for x in range(1,6)}
# print(sq)


# --------------------- Function -------------------------------------
# A Function is a block of reusable code that performs a specific task when called.
# Why use funtions : Avoid repetition, improve readability, easy to test and debug
# We can pass data into a function, known as parameters
#Types of Functions : 
#   Built in functions : Predefined (len(), print(), sum())
#   User defined functions : Functions we define using def
#   Lambda functions : Anonymous , one-line functions 
#ex : 
# def function_name(parameters):
#       {code}
#       return result
# def greet(name):
#     print(f"Hello, {name}")
# greet("Sai")

# # Function with return value 
# def add(a, b):
#     return a + b
# result = add(3,4)
# print(result)

# Functions with default parameters 
# A default parameter is a value that is used if no argument is provided, when the function is called
# def greet(name="Guest"):
#     print(f"Hello {name}")
# greet("sai")

#Functions with return values and conditions 
# A function can process data and return a result using the return keyword, we can also include logic like if conditions inside 
# def check_pass(marks): 
#     if marks >= 40 :
#         return "Pass"
#     else:
#         return "Fail"
# result = check_pass(85)
# print(result)

#Keyword Arguments : 
# This lets you specify arguments by name, so the order does not matter
# def student_info(name, age, branch):
#     print(f"Name is {name}")
#     print(f"Age is {age}")
#     print(f"Branch is {branch}")
# student_info(branch="Mechanical", age=23, name="Sai")

#Arbitrary Arguments : 
#There are two types : *args and **kwargs
# * args is multiple positional arguments 
# def add_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
# print(add_nums(12,23,12))

# **kwargs : This lets you pass any number of keyword arguments(like a dictionary)
# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# student_info(Name="Ravi", Age=22, Course="Python")

#Returing multiple values from a function
# def calculate(a,b):
#     sum_val = a + b
#     diff_val = a - b
#     return sum_val, diff_val
# x, y = calculate(7,3)
# print(f"Sum : {x}")
# print(f"Diff : {y}")

# -------------------- Lambda Functions / Anonymous functions ----------------------
# Lambda functions are small, one-expression functions that do not need a name
# ex : lambda arguments: expression
# square = lambda x: x*x
# print(square(5))

# --------------------- Map Function -----------------
# The map() function applies a given function to all items in an iterable (like a list or tuple ) and returns a list of result
# sy : map(function, iterable)
# nums = [1,2,3,4]
# sq = map(lambda x:x*x, nums)
# print(list(sq))

# --------------------- Filter function ----------------
# It filters out elements from an iterable based on a condition and return a filter object 
# filter(function, iterable)
# nums = [1,2,3,4,5,6]
# evens = filter(lambda x: x%2==0, nums)
# print(list(evens))

# ------------------ Reduce funtions -----------------
#The Reduce function from the functools module reduces an iterable to a single value by applying a binary functional cumulatively
#It basically reduces list to a single value
# from functools import reduce
# reduce(function, iterable)
# from functools import reduce
# nums = [1,2,3,4]
# result = reduce(lambda x,y:x+y, nums)
# print(result)





# ------------------------- List Comprehension -------------------------------
# List comprehension is a compact way to generate a new list by applying an expression to each item in an iterable.
# sy : new_list = [expression for item in iterable if condition]
# sq = [x**2 for x in range(1, 6)]
# print(sq)

#evens for list 
# nums = [1, 2, 3, 4, 5, 6]
# evens = [x for x in nums if x % 2 ==0]
# print(nums)

#nested list comprehension
# matrix = [[1, 2], [3, 4]]
# flat = [num for row in matrix for num in row]
# print(flat)

# -------------------------------File handling --------------------------- 
# to open a file and read : file = open("filename", "r")  r-read
#Reading from a file :
#   content = file.read()   read()- reads full content
#   print(content)          .readline() - reads line by line
#   file.close()            .readlines() - returns a list of lines
#Write to a file: 
#   file = open("fileName", 'w')
#   file.write("Hello, this is a test")
#   file.close()
#Appending to a file : Replace 'w' with 'a' , if we want a new line add \n during write line

#------------------------------ Exception Handling --------------------------
#In python when a error occur during execution, it raises an exception, we can use 
# Try and except to catch and handle these executions instead of crashing the program
#syn:
#   try:
#       #code that may cause an error
#   except SomeError:
#       #Code to handle the error
# try: 
#     a=10/0
# except ZeroDivisionError:
#     print("Cannot divide by Zero")


# ----------------------------- Regular Expression (regex) -----------------------
# A Regular expression is a sequence of characters that defines a search pattern. It's primarily used for string matching and manipulation
#Allowing us to search, extract and replace patterns within a string
# Special Characters in Regex:
# .: Matches any character except a newline.
# ^: Matches the start of a string.
# $: Matches the end of a string.
# *: Matches 0 or more occurrences of the preceding element.
# +: Matches 1 or more occurrences of the preceding element.
# ?: Matches 0 or 1 occurrence of the preceding element.
# []: Matches any one of the characters inside the brackets.
# |: OR operator, used to match either the left or the right side pattern.
# (): Groups expressions together for operations.

# Basic Functions in the re module:
# re.match(): Checks for a match only at the beginning of the string.
# re.search(): Searches the entire string for a match.
# re.findall(): Returns a list of all matches in the string.
# re.sub(): Replaces occurrences of a pattern in the string.
# import re
# pattern = r"^Hello"
# text = "Hello world"
# result = re.match(pattern, text)
# if result:
#     print("Pattern Matched")
# else:
#     print("No Match")

# pattern = r"world"
# result = re.search(pattern, text)
# if result:
#     print("Found : ", result.group())
# else:
#     print("Not Found")

# #Finding all occurences of a pattern
# pattern =  r"\d+"
# nums = re.findall(pattern, "I have 2 apples and 5 bananas")
# print("Numbers found : ", nums )

# #Replacing Text using Regex
# pattern = r"apples"
# result = re.sub(pattern, "Bananas", "I have 2 apples and 5 oranges")
# print(result)


# ---------------------- JSON Handling ----------------------
# JavaScript Object Notation is a light-weight data interchange format thats eay 
# for humans to read and write and easy for machines to parse and generate 
# Function     | Purpose
# json.dumps() | Convert Python object → JSON string
# json.loads() | Convert JSON string → Python object
# json.dump()  | Write JSON to a file
# json.load()  | Read JSON from a file

# check tasks.py for operations on JSON


# --------------------- Working with dates and times --------------
# from datetime import datetime
# now = datetime.now()
# print("Current Date and Time : ", now) #Current Data and Time
# print(now.year) # prints specific part

# #Formatting dates 
# formatted = now.strftime("%d-%m-%Y %H:%M:%S")
# print(formatted)

# #Creating a Specific Date
# from datetime import date
# d = date(2023,2,12)
# print("Fuck this Date : ", d)

# #Date Arithmetic 
# from datetime import timedelta
# yesterday = now - timedelta(days=1)
# tomorrow = now + timedelta(days=1)
# print(yesterday)
# print(tomorrow)


# ---------------- Virtual Environment and Package Management -----------------
# Virtual Environment is an isolated Environment that allows you to manage dependencies for a
# Python project separately from other projects

#Creating and Using a Virtual Environment : 
#       python -m venv myenv : creates a virtual environment with the name myenv
#Activate the virtual Environment: 
#       myenv/Scripts/activate
#Install Packages with pip:
#       pip install requests
#Freeze Installed Packages:
#       pip freeze > requirements.txt
#Install Packages from requiement.txt
#       pip install -r requirements.txt
#Deactivate the environment
#   deactivate

#---Python package management
#Check Version : pip --version
#List installed Packages : pip list
#Uninstall a package : pip unistall requests