# Python qs from sheet

#Find the smallest element in an array
# arr = {2,5,1,3,7}
# converted = list(arr)
# print(converted[0])

#Positive or negative 
# num = int(input("Enter the number : "))
# print("Positive" if num > 0 else "Negative" if num <0 else "Zero")

#even or odd
# num1 = int(input("Enter the Number : "))
# print("Even" if num1 %2 ==0 else "Odd") 

#sum of first N natural numbers 
# n = int(input("Enter the Number : "))
# sum = 0
# for i in range(1,n+1):
#     sum +=i
# print(sum)

# sum of numbers between range 
# num1 = (int(input("Enter the initial range : ")))
# num2 = (int(input("Enter the end range : ")))
# sum = 0
# for i in range(num1, num2+1):
#     sum +=i
# print(sum)

#Greatest of two numbers 
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# # if num1>num2 :
# #     print(f"{num1} is greater")
# # else: 
# #     print(f"{num2} is greater")

# greater = max(num1, num2)
# print(greater)

#Greatest of three
# a,b,c = 1,2,3
# d = max(a,b,c)
# print(d)
# if a >b and a>c :
#     print(f"{a} is greatest")
# elif b >a and b>c:
#     print(f"{b} is greatest")
# else:
#     print(f"{c} is greatest")


#sum of digits of a number
# num = input("enter : ")
# sum = 0
# for i in num:
#     sum+=int(i)
# print(sum) 

#Frequency counter : Write a function that takes a string and returns a dictionary containing the frequency of each character (excluding spaces and special characters).
# def str1():
#     counter = {}
#     str1 = input("Enter a string : ")
#     for i in str1:
#         #print(i)
#         if i not in counter:
#             counter[i] = 1
#             print(f"{i} : {counter[i]}") 
#         else:
#             counter[i]+=1
#             print(f"{i} : {counter[i]}")
# str1()

#Words Stat : Take a paragraph input and print:
# Number of words
# Longest word
# All unique words (use a set)
# para = "Former American entertainment wrestler Ric Flair has seen it all in professional wrestling, but even he couldn’t look away from the chaos that unfolded at WrestleMania 41. On Sunday night, John Cena defeated Cody Rhodes to win his record-breaking 17th world championship, eclipsing Ric’s long-standing record. While fans flooded social media with reactions, they waited for one man to weigh in. Ric didn’t disappoint."
# words = para.split()
# print(f"Number of Words : {len(words)}")
# longest_word = max(words, key=len)
# print(longest_word)
# unique = set(words)
# print(unique)

# Given a list of student dictionaries with name, marks, and passed keys:
# Filter all students who passed.
# Calculate average marks of passed students.
# students = [
#     {"name": "Alice", "marks": 85, "passed": True},
#     {"name": "Bob", "marks": 45, "passed": False},
#     {"name": "Charlie", "marks": 92, "passed": True}
# ]
# Passed_Students = {}
# for i in students:
#     for j in i:
#         if [i][j]["Passed"] == True:
#             Passed_Students.add([i][j]["passed": True])
# print(Passed_Students)

#Palindrome finder
# list = ["madam", "racecar", "hello", "level", "world"]
# for i in list:
#     if i == i[::-1]:
#         print(i)
   

#List Comprehension :Given a list of numbers, return a new list using list comprehension: Square all even numbers and add 10 to them.
# list = [1, 2, 3, 4, 5]
# comp = [(x*x)+10 for x in list if x % 2 ==0 ]
# print(comp)

#Safe Divide Function : Create a function that divides two numbers and handles: ZeroDivisionError,ValueError (if input isn't a number)
# def actions():
#     try:
#         a = int(input("Enter first number : "))
#         b = int(input("Enter Second number : "))
#         c = a/b
#         print(c)
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except ValueError:
#         print("Invalid Input, Please enter numbers")
# actions()

#Contact Extractor : 
import re 
text = "Call me at 987-654-3210 or email me at hello@example.com"
phonePat = r"\d{3}-\d{3}-\d{4}"
emailPat = r"[\w\.-]+@[\w\.-]+\.\w+"
phones = re.findall(phonePat, text)
emails = re.findall(emailPat, text)
print("Phone Numbers :", phones)
print("Emails: ", emails)
# Mini Json Converter 
# import json
# employee = {"name": "Sai", "age": 25, "dept": "IT"}
# json_con = json.dumps(employee)
# print(json_con)

#Birthday countdown
from datetime import datetime
birthday = datetime(2025, 8, 21)
now = datetime.now()
if birthday < now:
    birthday = birthday.replace(year = now.year + 1)
print(f"Days left until birthday : {(birthday - now).days }")

#Tuple reverser 
tup = (1, 2, 3, 4)
tup_rev = list(tup[::-1])
tup_mod = list()
for i in tup_rev:
    j = i*i
    if j not in tup_mod:
        tup_mod.append(j)
print(tuple(tup_mod))
