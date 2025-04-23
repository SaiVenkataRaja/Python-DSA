#Task 1 :
# name = input("Enter your name : ")
# age = int(input("Enter your age :"))
# college = input("Enter your college name :")
# fee = int(input("Enter the fee : "))

# print("--- Event Registration ---")
# print(f"Name     : {name}")
# print(f"Age      : {age}")
# print(f"College  : {college}")
# print(f"Fee Paid : Rs.{fee}")
# print("---------------------------")

#Task 2 on order of instruction / sequence of execution 

# item_name = "Burger"
# Qu = 2
# price_per_item = 150
# total = Qu * price_per_item
# print(" -- Order Summary -- ")
# print(f" Item        : {item_name}")
# print(f" Quantity    : {Qu}")
# print(f" Unit Price  : {price_per_item}")
# print(f" Total Price : {total}")
# print(" --------------------")

#Task 3 : Bodmas

# assignment_score = 20
# quiz_score = 10
# exam_score = 70
# final_score = (assignment_score * 0.2) + (quiz_score * 0.3) + (exam_score * 0.5)

# print(" --- Final Score Calculation --- ")
# print(f" Assignment Score : {assignment_score}")
# print(f" Quiz Score       : {quiz_score}")
# print(f" Exam Score       : {exam_score}")
# print(f" Final Score      : {final_score}")
# print(" --------------------------------")

#Task 4 : Playing with strings

# first_name = input("Enter your First name : ")
# last_name = input("Enter your Last Name : ")
# full_name = first_name  + " " + last_name
# short_name = first_name[0] + "."+ last_name
# stars = "*" * len(full_name)

# print(f"Full Name  : {full_name}")
# print(f"Short Name : {short_name}")
# print(f"Nameplate  : {stars} ")
# print(f"             {full_name}")
# print(f"             {stars} ")
 

#Task 5 : Type conversion

# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# print(f" --- Calculation Result ---")
# print(f"Addition       : {num1+num2}")
# print(f"Subtraction    : {num1-num2}")
# print(f"Multiplication : {num1*num2}")
# print(f"Division       : {round(num1/num2, 2)}")
# print(" ---------------------------")

#Task 6 : Logical task
# age = int(input("Enter your age : "))
# id = input("Do you have an Id (Yes / No)")
# if id.lower() == "yes" and (age >=18 ):
#     print("Access Granted")
# else:
#     print("Access Denied")

#Task 7 : Password Checker
# correct_password = str(1234)
# entered_password = str(input("Enter the Password"))
# while correct_pass == entered_password:
#     print("Access Unlocked")

# else :
#     print("Incorrect Password, Try again ")


# correct_password = str(1234)
# entered_password = ""
# while entered_password != correct_password:
#         entered_password = input("Enter the Password : ")
#         if entered_password != correct_password:
#                  print("Incorrect Password, Try again")      
# else:
#         print("Access unlocked")
        
#Task 8 :
# Asks the user to enter 5 task names one by one using a for loop
# Then prints them as a bullet list
# tasks = []
# for i in range(1,6):
#         task = input(f"Enter the task {i} : ")
#         tasks.append(task)
# print(f" --- Daily Tasks ---")
# for t in tasks: 
#         print(f" - {t}")
# print(f" -------------------")

#Task 9 :
# tasks = []
# no_tasks = int(input("Enter the number of tasks : "))
# for i in range(1,no_tasks+1):
#     task = input(f"Enter the task {i} : ")
#     tasks.append(task)
# print("--- Tasks List ---")
# for idx, j in enumerate(tasks, start=1):
#     print(f"{idx}. {j}")
# print("-------------------")

#Task 10 
#There are 3 classes, and each class has 2 students.
# You need to:
# Loop through each class.
# For each class, loop through each student.
# Ask for the student's name and if they’re Present/Absent.
# Store the data properly.

# #Task 10.1
# name = input("Enter your full name : ")
# print(f"Removed Spaces : {name.strip()}")
# print(f"Lower cased name : {name.lower()}")
# print(f"underscored name : {name.replace(" ", "_")}")

#Task 10.2
# email = input("Enter the email : ")
# if email[0].isalpha():
#     print("Starts with letter ? Yes")
# else:
#     print("Starts with letter ? No")
# if email.endswith(".com"):
#     print("Ends with .com? Yes")
# else : 
#     print("Ends with .com? No")

# position = email.find("@")
# if position != -1:
#     print(f"@ Symbol Position : {position}")
# else : 
#     print("Symbol not found")

#Task 10.3
# fullName = input("Enter your full name : ")
# split = fullName.split()
# intials = []
# for i in split:
#     intials.append(i[0])
# print(".".join(intials).upper())

#Task 10.4
# fullName = input("Enter your full name : ")
# rever = fullName.split()
# rever.reverse()
# reversed_name = ' '.join(rever)
# print(reversed_name.title())

#Task 11 : Solid box

# for i in range(5):
#     for j in range(5):
#         print(" * ", end="")
#     print()

# Right angled triangle
# for i in range(5):
#     for j in range(5):
#         if j <= i :
#             print(" * ", end="")
#     print()

#Right aligned triangle
# for i in range(5):
#     for j in range(5 -i -1):
#         print("   ", end='')
#     for k in range(i +1):
#         print(" * ", end='')
#     print()
# inverted Right aligned triangle
# for i in range(5):
#     for j in range(5): 
#         if i > j :
#             print("   ", end="")
#         else : 
#             print(" * ", end="")
#     print()

#Number triangle 
# for i in range(1,5):
#     for j in range(1,5):
#         if i >= j: 
#             print( j , end=' ')
#         else:
#             print(" ", end='')
#     print()

#Reversed number triangle 
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#             print(j, end=' ')
            
#     print()

#Task 12: loop control statements
# nums = []
# for i in range(1,6):
#     num = int(input(f"Enter the number {i}: "))
#     if num < 0:
#         continue
#     if num == 0:
#         break
#     else:
#         nums.append(num)
# print(nums)

#Task 13 : String comparision
# name1 = input("Enter Name 1 : ")
# name2 = input("Enter Name 2 : ")
# if name1 == name2 :
#     print("They are exactly same")
# elif name1.lower() == name2.lower() : 
#     print("Both Names are same but Case sensitive")
# else:
#     if name1 < name2:
#         print(f"{name1} comes alphabetically first")
#     else: 
#         print(f"{name2} comes alphabetically first")

#Task 14 : List
# Write a program where the user can:
# Enter a list of numbers (take input until the user enters "stop").
# Calculate the sum, average, and highest number.
# Remove any negative numbers and display the cleaned list.

# lst = []
# while True:
#     entry = input("Enter a number ('stop' to finish ): ")
#     if entry == 'stop'.lower():
#         break
#     num = int(entry)
#     if num < 0:
#         continue
#     else:
#         lst.append(num)
# print(lst)
# sum = 0
# for i in lst:
#     sum+=i
# print(f"The sum of the integers is {sum}")
# highest = 0 
# for i in lst:
#     if i > highest:
#         highest = i
# print(f"The Average of the list is {sum/(len(lst))}")
# print(f"The highest number in the list is {highest}")

# Task 15 : List : removing duplicates
# lst = []
# uniqlist = []
# while True:
#     entry = input("Enter a number ('stop' to finish) : ")
#     if entry == 'stop'.lower():
#         break
#     num = int(entry)
#     if num < 0 :
#         continue
#     else:
#         lst.append(num)
#     if num not in uniqlist:
#             uniqlist.append(num)
# print(lst)
# print(uniqlist)

#Task 15.1 
# n = int(input("Enter a number for count : "))
# nums = []
# evens = []
# odds = []
# for i in range(n):
#     num = int(input("Enter the number : "))
#     nums.append(num)
# print(nums)
# for i in nums :
#     if i % 2 == 0 and i not in evens:
#         evens.append(i)
#     else:
#         if i not in odds:
#             odds.append(i)
# print(f"Evens are {evens}")
# print(f"Odds are {odds}")

#Task 15.2 : nested lists
# nested_list = []
# while True:
#     entry = input("Enter a number ('stop' to exit) : ")
#     if entry == 'stop'.lower():
#         break
#     num = int(entry)
#     for i in nested_list:
#         nested_list.append(i)
# print(nested_list)

# nested_list = [[1,2,3], [4,5,6],[7,8,9]]
# # print(nested_list[0][0])
# # print(nested_list[0][1])
# # print(nested_list[0][2])
# # print(nested_list[1][0])
# # print(nested_list[1][1])
# # print(nested_list[1][2])
# # print(nested_list[2][0])
# # print(nested_list[2][1])
# # print(nested_list[2][2])
# for i in nested_list:
#     for j in i:
#         print(j)

#sum of all elements in a list 
# nested_list = [[1, 2], [3, 4], [5, 6]]
# sum = 0 
# for i in nested_list:
#     for j in i:
#         sum = sum + j
# print(f"The sum of all the elements in the list : {sum}")

#Find the largest
# nested_list = [[12, 5], [7, 20], [3, 18]]
# max = 0
# for i in nested_list:
#     for j in i:
#         if j > max:
#             max = j
# print(max)

#Task 16 : Tuples
# Create a tuple with numbers from 1 to 10 and print: The first 3 elements, The last 2 elements, The middle element
# tup = (1,2,3,4,5,6,7,8,9,10)
# print(tup[:3])
# print(tup[-2:])
# length = len(tup)
# print(tup[length // 2])

# info = ("Sai", 24, "Developer", "Hyderabad")
# name, age, role, location = info
# print(f"Name is {name}")
# print(f"Age is {age}")
# print(f"Role is {role}")
# print(f"Location is {location}")

# #Write a program to count how many times the number 5 appears in this tuple:
# nums = (5, 1, 5, 3, 5, 7, 8, 5)
# print(nums.count(5))

# #Convert it into a list, add 60, then convert it back to a tuple and print.
# sample = (10, 20, 30, 40, 50)
# list_sample = list(sample)
# print(list_sample)
# list_sample.append(60)
# print(list_sample)
# sample = tuple(list_sample)
# print(sample)

#Task 17 : 
#Create a dictionary called student with these keys: "name": your name, "id": any 4-digit number ,"branch": any string, "marks": a list of 3 integers
#Then, do the following:Print the student's name and branch. Print the average of the marks.
# Add a new key "result" with value "Pass" if average >= 40, else "Fail".Print the full dictionary.
# student = {
#     "name" : "Sai Venkata Raja",
#     "id" : 4017,
#     "branch" : "Mechanical Engineering",
#     "marks" : [75,25,60]
# }
# print(f"The Student's name is {student["name"]}")
# print(f"The branch is {student["branch"]}")

# sum = 0
# for i in student["marks"]:
#     sum = sum + i
# print("The Total marks are ", sum)
# avg = sum / len(student["marks"])
# average = round(avg, 2)
# if average >= 40:
#     student["Result"] = "Pass"
# else:
#     student["Result"] = "Fail"

# print(student)

#Task 17.2 
# Print only the keys
# Print only the values
# Print each key-value pair
# Get a value using .get()
# Add a new key "college": "IIT" using .update()
# student = {
#     "name": "Ravi",
#     "age": 22,
#     "course": "B.Tech",
#     "grades": [85, 90, 92]
# }
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("course"))
# student.update({"college": "IIT"})
# print(student)

#Task 17.3 : Nested Dictionaries 
#Print the name and age of each student, Print the total marks of each student,Add a key "result": "Pass" to each student if their average is >= 40.
# #Print the updated dictionary.
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
# for i in students:
#     print(f"Details of {i} : ")
#     print("Name : ", students[i]["name"])
#     print("Age : ", students[i]["age"])
# for i in students:
#     total = sum(students[i]["marks"])
#     print(f"The Total marks of {i} : {total}")
#     avg = total / len(students[i]["marks"])
#     students[i]["Result"] = 'Pass' if avg >= 40 else "Fail"
# print(students)



# for i in students:
#     print(f"Details of {i} : ")
#     print("Name : ", students[i]["name"])
#     print("Age : ", students[i]["age"])

# for i in students: 
#     sum = 0
#     for j in students[i]["marks"]: 
#             sum = sum +j 
#     print(f"The Total marks of {i} : {sum}")
#     if (sum / len(students[i]["marks"])) >= 40:
#             students[i]["Result"] = "Pass"
#     else:
#             students[i]["Result"] = "Fail"
# print(students)
            
#Task 17.4 : Nested Dictionaries
# college = {
#     "CSE": {
#         "s101": {
#             "name": "Arjun",
#             "year": 2, 
#             "marks": [88, 76, 92]
#             },
#         "s102": {
#             "name": "Meena",
#             "year": 1, 
#             "marks": [67, 72, 70]
#             }
#     },
#     "ECE": {
#         "s201": {
#             "name": "Ravi",
#             "year": 3,
#             "marks": [50, 65, 80]
#             },
#         "s202": {
#             "name": "Divya", 
#             "year": 2, 
#             "marks": [90, 85, 95]
#             }
#     }
# }
# for dept in college:
#     print("The Department is ", dept)
#     for id in college[dept]:
#         student = college[dept][id]
#         print("Name is ", student["name"])
#         print("Year is ", student["year"])
#         total = sum(student["marks"])
#         print("The Total marks are ", total)
#         avg = total / len(student["marks"])
#         student["Result"] = "Pass" if avg >= 40 else "Fail"
# print(college)

#Task 17.5 : Topper Finder 
college = {
    "CSE": {
        101: {"name": "Alice", "year": 2, "marks": [88, 92, 79]}, #259
        102: {"name": "Bob", "year": 2, "marks": [90, 85, 93]} #268
    },
    "ECE": {
        201: {"name": "Charlie", "year": 3, "marks": [65, 70, 72]}, #207
        202: {"name": "David", "year": 3, "marks": [80, 88, 91]} #259
    }
}


#Minor issues in the code
# for dept in college:
#     print(f"The Department : {dept}")
#     for sid in college[dept]:
#         student = college[dept][sid]
#         #print(student["marks"])
#         total = sum(student["marks"])
#         #print(f"The Total marks of {student["name"]} are {total}")
#         highest = 0 
#         if sum(student["marks"]) > highest:
#             highest = student["name"]
#     print(f"The Topper is : {highest}")
#     print(f"The Department is : ", [dept])
#     print(f"The Id is {college[dept]}")
#     avg = total / len(student["marks"])
#     print(f"The Average is {round(avg, 2)}")

#efficient one 

# topper_name = ""
# topper_avg = 0
# topper_dept = ""
# topper_id = 0
# for dept in college:
#     for id in college[dept]:
#         student = college[dept][id]
#         #print(student)
#         total = sum(college[dept][id]["marks"])
#         avg = total / len(student["marks"])
#         print(f"Student : {student['name']}, Total : {total}, Average : {round(avg, 2)}")
#         if avg > topper_avg:
#             topper_avg = avg
#             topper_name = student["name"]
#             topper_dept = dept
#             topper_id = id 
# print()
# print(f"Name : {topper_name}")
# print(f"ID : {topper_id}")
# print(f"Department : {topper_dept}")
# print(f"Average : {round(topper_avg, 2)}")

#Task 18 : Sets 
# Unique Vowels : Take a string input and print all the unique vowels present in it using a set.
# alphs = set(input("Enter a word : ").lower())
# vowels = {'a', 'e', 'i','o', 'u'}
# filtred = set()
# for i in alphs:
#     if i in vowels:
#         filtred.add(i)
# print(filtred)

#Task 18.2 Removing duplicates 
#Take a list of numbers with duplicates and print a new list with all duplicates removed using sets.
# lst = [1,2,3,2,1,2,3,2,1,2,2,3,3,2,1]
# new_lst = set()
# for i in lst:
#     if i not in new_lst:
#         new_lst.add(i)
# print(new_lst)

# Task 18.3 : Common elements between two lists 
#Take two lists and print the common elements (intersection) using set operations. 
# lst1 = set([1,2,3,4,5])
# lst2 = set([2,3,4,5,6])
# print(lst1.intersection(lst2))

#Task 18.4 : Studenets who attended both events 
# Find students who attended both events.
# Find students who attended only one of the events.
# Find students who attended at least one event.
# event1 = {"Alice", "Bob", "Charlie"}
# event2 = {"David", "Charlie", "Alice"}
# print(f"Students who attended both events : {event1.intersection(event2)}")
# print(f"Students who attended who only attended one event : {event1.difference(event2)}")
# print(f"students who attended at least one event : {event1.union(event2)}")

#Task 18.5 : count unique words 
# line = "Take two lists and print the common elements intersection using set operations "
# words = line.lower().split()
# unique_words = set(words)
# print(unique_words)
# print(len(unique_words))

#Task 18.6 : Vowel counter 
# Takes a sentence as input.
# Extracts all unique vowels present in the sentence using a set.
# Prints the unique vowels and their count.
# senta = "This is a beautiful day to explore code"
# vowels = {'a', 'e', 'i', 'o', 'u'}
# unique_vowels = set()
# for i in senta:
#     if i in vowels and i not in unique_vowels:
#         unique_vowels.add(i)
# print(unique_vowels)
# print(len(unique_vowels))


#Task 19 : Functions 
#Write a function multiply that takes two numbers and returns their product. Then call it with your own values and print the result.
# def multiply(a, b):
#     return a*b
# result = multiply(3,5)
# print(result)

# 19.1
# Write a function that takes a number and returns whether it’s even or odd.
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(even_odd(6))

# 19.2 : Create a function that takes two numbers and an operator (+, -, *, /) and returns the result.
# def calculate(a,b):
#     operator = input("Enter the Operation : ")
#     if operator == '+':
#         return a+b
#     elif operator == '-':
#         return a-b
#     elif operator == '*':
#         return a*b
#     elif operator == '/':
#         return a/b
#     else:
#         return " Invalid "
# print(calculate(2,4))

#19.3 : Write a function that accepts a list of marks and returns total, average, and result (Pass if avg ≥ 40).
# def grading(marks):
    
#     total = 0 
#     for i in marks:
#         total += i
#     print("The Total is ", total)
#     avg = total/len(marks)
#     print(f"The Average score is {round(avg, 2)}")
#     if avg >= 45:
#         print("Pass")
#     else : 
#         print("Fail")
# print(grading([45,65,75]))

#19.4 : Max of three
# def max(nums):
#     base = 0 
#     for i in nums:
#         if i > base:
#             base = i
#     return base
# print(max([13,42,12])) 

#19.5 : Palindrome check 
# def palindrome(word):
#     return word == word[::-1]
# (print(palindrome("madam")))

# Challenge 20 : Lambda functions
# sq = lambda x:x*x 
# print(sq(6))
# 20.1 : adding two numbers
# add = lambda a,b: a+b
# print(add(1,2))

# 20.1 
# lar = lambda a,b : a if a >b else b
# print(lar(10,15))

# #20.2  convert all strings to uppercase.
# words = ["hi", 'laptop', 'mouse']
# upper = list(map(lambda word: word.upper(), words))
# print(list(upper))

# #20.3 Filter numbers divisible by 3 from a list.
# nums = [1, 2, 3, 6, 8, 9, 10, 12]
# div = list(filter(lambda x: x %3 ==0, nums))
# print(div)

#20.4 Double all numbers in a list using map()
# nums = [1,2,3,4]
# add = map(lambda x:x+x, nums)
# print(list(add))

#20.5 Filter names longer than 4 characters using filter()
# lst = ["Sai", "Raja", "Python", "AI"] 
# four = filter(lambda x: len(x) > 4 , lst)
# print(list(four))

# #20.6  Sum all values in a list using reduce()
# from functools import reduce
# lst = [1,2,3,3,2,1,1,21,21]
# add = reduce(lambda x,y:x+y, lst)
# print(add)

# #20.7 Use lambda with map() to convert a list of temperatures from Celsius to Fahrenheit
# celc = [0,10,20]
# fahre = map(lambda x: (x*9/5) +32, celc)
# print(list(fahre)) 

#20.8  Use filter() to extract only palindromes from a list of words
# lst = ["madam", "code", "noon", "apple"] 
# palin = filter(lambda x: x==x[::-1], lst)
# print(list(palin))

#20.9 You’re given a list of numbers. Use filter() and lambda to keep only the squares that are odd.
# lst = [1,2,3,4,5]
# oddSq = map(lambda x:x*x if x % 2 !=0 else None, lst)
# oddSq = filter(lambda x: x is not None, oddSq)
# print(list(oddSq))

#20.10  Given a list of names, use map() to convert the first letter of each name to uppercase and the rest to lowercase.
# lst = ['sai', 'VENKATA', 'raja']
# case = map(lambda x:x.capitalize(), lst)
# print(list(case))

#20.11 Use reduce() to find the product of all even numbers in a list.
# from functools import reduce
# nums = [1, 2, 3, 4, 5, 6]
# evenMul = reduce(lambda x, y: x*y if y%2 ==0 else x, nums)
# print(evenMul)

# Challenge 21 : List comprehension 
# Create a list of squares of odd numbers between 1 to 10
# lst = [1,2,3,4,5,6,7,8,9,10]
# odds = [i for i in lst if i %2 !=0]
# print(odds)

#21.2 : Given a list of words, filter and return only those words with more than 3 characters 
# list = ['sai', 'VENKATA', 'raja']
# updated = [i for i in list if len(i) > 3]
# print(updated)

#21.3 Convert a list of names into lowercase
# list = ['sai', 'VENKATA', 'raja']
# small = [ i.lower() for i in list]
# print(small)

#21.4 From a list of numbers, add 5 only to even numbers 
# nums = [1,2,3,4,5,6,7]
# add = [i+5 for i in nums if i%2==0]
# print(add)

# Challengle 22 : Exception Handling
# def exep(a,b):
#     try:
#         c = a/b
#     except ZeroDivisionError:
#         return "Cannot divide by zero"
# print(exep(2,0))

# #22.2 : Ask the user to input a number. Use try-except to handle ValueError if the input is not a valid integer.
# # try:
# #     val = int(input("Enter Something : "))
# # except ValueError:
# #     print("This is exception is handled")

# #22.3 : Write code to access an element at a given index from a list. Handle IndexError if the index is out of range.
# list = [1,2,3,4,5]
# try:
#     print(list[7])
# except IndexError:
#     print("Indexing is invalid")

# #22.4 : Ask the user to input two numbers and divide them. Handle both ZeroDivisionError and ValueError.
# try:
#     num1 = int(input("Enter the First number : "))
#     num2 = int(input("Enter the Second number: "))
#     res = num1/num2
#     print(res)
# except ZeroDivisionError:
#     print("Cannot divide by Zero")
# except ValueError:
#     print("Value error dude !!")

# #22.5 : Try to open a file (e.g., "data.txt"). Handle the FileNotFoundError.
# try:
#     file = open("file.txt", 'r')
#     print(file)
# except FileNotFoundError:
#     print("The file is not there dude!! ")

# #22.6 : Modify one of the above examples to include a finally block that prints "Execution complete" no matter what happens.
# list = [1,2,3,4,5]
# try:
#     print(list[7])
# except IndexError:
#     print("Indexing is invalid")
# finally:
#     print("Execution completed")



#Challange 23 : Regex 
#Write a regex to check if a string starts with a specific word (e.g., "Python") and ends with a number. 
import re
# pattern = r"^Python"
# endpattern = r"\d+$"
# text = "Python : Module Number 5"
# result = re.match(pattern, text)
# result2 = re.search(endpattern, text)
# if result and result2:
#     print("Pattern and Number matched")
# else:
#     print("No match Found")

#Challenge 23.2 : Write a regex to extract all the email addresses from a given string.
# str = "Contact us at support@example.com or sales@domain.co.in"
# pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
# result = re.findall(pattern, str)
# if result:
#     print("Emails", result)
# else:
#     print("No match found")

#Challenge 23.3 : 
# con = "123-123-1234"
# pattern = r"\d{3}-\d{3}-\d{4}"
# result = re.fullmatch(pattern, con)
# if result:
#     print("Correct Format")
# else:
#     print("Incorrect Format")

# Challenge 24 : JSON
#Convert a Python dictionary into a JSON string
# import json
# data = {
#     "name":"Sai",
#     "age" : 24,
#     "lang" : "Python" }
# json_str = json.dumps(data)
# print(json_str)

# # Convert a JSON string back to a Python dictionary
# json_data = json_str
# py_obj = json.loads(json_data)
# print(py_obj["lang"])


#Challenge 25 : Date and Times
from datetime import datetime
# now = datetime.now()
# formatted = now.strftime("%A, %d %B %Y ")
# print(formatted)

# # Days left until my next birthday
# birthday = datetime(2025, 8, 21)
# if birthday < now:
#     birthday = birthday.replace(year=now.year + 1)
# days_left = (birthday - now).days
# print(days_left)

#Calculate and print the difference in days between two given dates.
# past = datetime(2023, 2, 12)
# now = datetime.now()
# print(past)
# print(now.strftime("%Y-%m-%d"))
# diff = (now - past).days
# print(diff)

#Print the current time only in the format HH:MM:SS AM/PM
# print(now.strftime("%H:%M:%S %p"))