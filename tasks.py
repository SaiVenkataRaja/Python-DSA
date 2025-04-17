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
lst = []
uniqlist = []
while True:
    entry = input("Enter a number ('stop' to finish) : ")
    if entry == 'stop'.lower():
        break
    num = int(entry)
    if num < 0 :
        continue
    else:
        lst.append(num)
    if num not in uniqlist:
            uniqlist.append(num)
print(lst)
print(uniqlist)
