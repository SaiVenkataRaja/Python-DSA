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
my_list = [1,2,4,4]
print(my_list[0]) #indexing
print(my_list)
my_list[2] = 10 #modifying
print(my_list)
my_list.append("Thala for a reason") #adds at the end
print(my_list)
my_list.insert(2, 7) #inserts at specific index position
print(my_list)
my_list.remove(7) # removes the number (item)
print(my_list)
my_list.pop(0) # removes by index
print(my_list)
print(my_list[1:4]) # slicing
print(len(my_list)) # length of list
