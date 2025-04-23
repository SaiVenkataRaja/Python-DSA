#------------------------------------------ OOPS -----------------------------------
# OOP Stands for Object Oriented Programming
#       It is a programming paradigm that organizes code using objects -- real-world entities
#       that combines data(attributes) and behavior(methods) into a single unit called class
# Instead of just writing functions and variables, OOP helps us to build reusable ans scalable 
# code using concepts like Encapsulation, Inheritance, Polymorphism and Abstraction

# ---------------------------Classes and Objects ------------------------------------
# Class is like a blueprint or template for creating objects
# # It defines attributes (variables) and methods (functions) that describes the behavior of object 
# class Car:
#     #constructor (Initialization)
#     def __init__(self, brand, color): # __init_ : A method used to initialize the object properties when it' created
#         self.brand = brand            # init automatically gets called when we creaete an object from a classs
#         self.color = color            #Self refers to current object being created or used , without self , we cannot access or set obj's variables
#         print(f"The company is {self.brand} and color is {self.color}")
# #Creating Object Instance 
# my_car=Car("Toyota", "Black")
# print(my_car)

# #------------------------- Instance Variable Vs Class Variable --------------------------
# # Instance Variable : Belongs to the objetc(instance) of a class, which is defined inside the __init__ method using self
# #   Each object has its own separate copy
# class Dog:
#     def __init__(self, name):
#         self.name = name #instance variable 
# dog1 = Dog("Jessy")
# dog2 = Dog("Buddy")
# print(dog1.name)
# print(dog2.name)

# # Class Variable : Belongs to the class itself, shared by all instances.
# #       Defining outside __init__, usually right under the class definition       
# class Dog:
#     species = "Labrador"
#     def __init__(self, name):
#         self.name = name
# dog1 = Dog("Jessy")
# dog2 = Dog("Buddy")
# print(dog1.name)
# print(dog2.name)
# print(dog1.species)
# print(dog2.species)

# # Feature     | Instance Variable       | Class Variable
# ______________|___________________________|__________________
# Belongs to    | Object/Instance           | Class
# Defined in    | __init__() using self.var | Directly under class
# Scope         | Unique per object         | Shared across all objects
# Accessed with | self.variable             | ClassName.variable or self.variable


# -------------------------------- Encapsulation -------------------------------
# Encapsulation is the practice of hiding internal details and only exposing what's necessary
# Why Use Encapsulation : 
#           Prevents accidental data change
#           Control how values are accessed / modified
#           Add validations (eg, only allow positive deposits)

# Type      | Prefix     | Accessible From
#___________|____________|_______________________
# Public    | variable   | Anywhere
# Protected | _variable  | Subclass / Conventionally private
# Private   | __variable | Only inside the class (Name mangling)

# Example : 

# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance #Private variable 
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#     def withdraw(self, amount):
#         if 0< amount <= self.__balance:
#             self.__balance -= amount
#             return "Withdraw Successful"
#         return "Insufficient Balance"

#     def get_balance(self):
#         return self.__balance       
    
# acc = BankAccount("Jack", 1000)
# print(acc.get_balance())
# print(acc.withdraw(1100))
# print(acc._BankAccount__balance)

# ------------------------------------- Inheritence --------------------------------------
# Inheritence lets one class (child) reuse the properties and methods of another class (parent)
# It is like aquiring properties from parent to child 
# It helps in code reuse, extensibility and modeling real world relationships 
# syn :
class Parent:
    def method1(self):
        print("Method of Parent")

class Child(Parent):
    def method2(self):
        print("Method of Child")
    
obj = Child()
obj.method1()
obj.method2()
        
# Example : 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self,name,age, studend_id):
        super().__init__(name, age)   # super keyword is used to call methods from the parent class
        self.student_id = studend_id
    
    def show_id(self):
        print(f"My Student ID is {self.student_id}")
        
obj1 = Student("Sai", 23, 4017)
obj1.show_id()
obj1.greet()
          