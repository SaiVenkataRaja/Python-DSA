# # Challenge 1 : 
# class Person:
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def greet(self):
#         print(f"Hello, my name is {self.name}, i am {self.age} years old and i live in {self.city}")

# my_details = Person("Sai Venkata Raja", 24, "Hyderabad")
# my_details.greet()

# #Challange 2 : area and perimeter of rectangle 
# class Rectangle:
#     def __init__(self, length :float, width :float):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width #print(f"The Area of Rectangle is {self.length * self.width}")
#     def perimeter(self):
#         return 2 *(self.length + self.width) #print(f"The Perimeter of Rectangle is {2 *(self.length + self.width)}")

# rect = Rectangle(10, 20)
# print(f"Area : {rect.area()}")
# print(f"Perimeter : {rect.perimeter()}")
    
# # Challange 3 : 
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance+=amount
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return "Withdrawal successful"
#         else: 
#             return "Insufficient Balance"
        
# my_acc = BankAccount("Sai", 7000)
# my_acc.deposit(400)
# print(my_acc.balance)
# print(my_acc.withdraw(2000))
# print(f"Current Balance : {my_acc.balance}")

# #Challenge 4 : Track Students Using Class & Instance Variables
# class Student:
#     total_students = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age 
#         Student.total_students += 1
#     def display_info(self):
#         print(f"Name : {self.name}, Age : {self.age}")

# Student1 = Student("Sai", 24)
# Student2 = Student("Ravi", 22)
# Student3 = Student("Priya", 25)

# Student1.display_info()
# Student2.display_info()
# Student3.display_info()
# print(f"Total Students : {Student.total_students}")

# Challenge 5 : Creating a secure wallet system
# class DigitalWallet:
#     def __init__(self, owner_name, balance):
#         self.owner_name = owner_name
#         self.__balance = balance
#     def add_money(self, amount):
#         if 0 < amount:
#             self.__balance += amount
#             return "Money added"
#         else:
#             return "Negative deposits are not allowed"
#     def  spend_money(self, amount):
#         if amount <=0:
#             return "Invalid amount"
#         elif amount > self.__balance:
#             return "Not enough money"
#         else:
#             self.__balance -= amount
#             return f"Spent ₹{amount} successfully"
#     def get_balance(self):
#         return self.__balance
    
# my_wallet = DigitalWallet("Sai", 500)
# print(my_wallet.add_money(200))
# print(f"The Current balance is {my_wallet.get_balance()}")
# print(my_wallet.spend_money(1000))
# print(f"The Current balance is {my_wallet.get_balance()}")


# Challenge 6 : Inheritence 

# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#     def show_info(self):
#         print(f"Brand : {self.brand} , Color : {self.color}, Type : {self.car_type}")

# class Car(Vehicle):
#     def __init__(self, brand, color, car_type):
#         super().__init__(brand, color)
#         self.car_type = car_type
#     def show_info(self):
#         super().show_info()
#         #print(f"Type : {self.car_type}")

# veh = Car("Toyota", "Red", "SUV")
# veh.show_info()
         
# Challenge 6.2 : Employee Manger relationship

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def show_details(self):
#         print(f"Employee Name : {self.name}\nSalary : {self.salary}")
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#          super().__init__(name, salary)
#          self.department = department
#     def show_details(self):
#         super().show_details()
#         print(f"Department : {self.department}")

# emp = Employee("Ravi", 50000)
# mgr = Manager("Sai", 80000, "IT")
# print("---Employee---")
# emp.show_details()
# print("---Manager----")
# mgr.show_details()

# Challenge 6.3 : Book & Library 
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year 
    def display_info(self):
        print(f"Title : {self.title} \nAuthor : {self.author} \nYear : {self.year}")
class library_id(Book):
    