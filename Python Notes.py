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
fruits = {'apple','apple', 'banana', 'mango'}
nums = set([1,2,4,5]) # using set constructor 
#sets automatically removes duplicates and we cannot access elements by index
print(fruits)
s= {1,2,3,4}
s.add(5) #adds 5 to set
print(s)

s.remove(2) #removes 2 from set
print(s)

s.pop() #removes random item
print(s)

s.clear() #empties the set
print(s)

#set operations like in math 
a = {1,2,3,5}
b = {4,5,6}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
#membership testing
if 3 in a:
    print("3 is in the set")