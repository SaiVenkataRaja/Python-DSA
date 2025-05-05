# DSA - Data Structures and Algorithm
# Basic Data structure basics are Arrays/List, Tuple, set and dict (Check Python Notes)

# Basic Algorithm : Linear search, Binary search, bubble sort, selection sort, Insertion sort, Recursion basics 
# -------------------------------------------Linear search -------------------------------------------
# Linear Search : it basically goes through each element one by one in a list / array until we find the target
# Concept : 
#       - goes from start to end
#       - compares each element with the target 
#       - if found , returns index true
#       - if not, returns -1 (false)

# ex : 
# arr = [1,2,3,4]
# target = 4
# for i in range(len(arr)):
#     if arr[i] == target:
#         print(i)

# ------------------------------------------ Binary Search --------------------------------------------
# Binary search is an efficient way to search for an element in a sorted list / array.
# It works repeatedly by dividing the search interval in half
#ex: 
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return f"Found {target} at index {mid}"
#         elif arr[mid] <target:
#             low = mid + 1
#         else:
#             high = mid -1
#     return f"{target} is not found in the list" 

# arr = [1,2,3,4,5,6,7]
# target = 3
# print(binary_search(arr, target))

#--------------------------------------- Bubble sort --------------------------------------------------
# Bubble sort compares with the adjacent element in the list / array 
# def bubble_sort(arr):
#     n = len(arr)
   
#     for i in range(n):
        
#         for j in range(0, n - i - 1):
            
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# numbers = [5, 1, 4, 2, 8]
# print("Before Sorting:", numbers)
# sorted_numbers = bubble_sort(numbers)
# print("After Sorting:", sorted_numbers)


# ------------------------------------- Selection Sort ----------------------------------------------
# Selection sort finds the smallest element in a unsorted list and puts it at the beginning 
# This reduces number of swaps than bubble sort
# ex : 
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index],  arr[i]
#     return arr
# arr = [5,2,1,4,6]
# print(selection_sort(arr))

# -------------------------------------- Insertion Sort ----------------------------------------------
# Insertion sort, picks the elemnt from list and places it in a newly sorted array 
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i -1 

#         while j >=0 and arr[j] > key:
#             arr[ j+ 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key
#     return arr
# arr = [3,4,2,1,5]
# print(insertion_sort(arr))

# ---------------------------------------- Recursion ---------------------------------------------------
# Recursion is a function calling itself 
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))


# -------------------------------------Time and Space Complexity ----------------------------------------
# Basics : 
# Time complexity is a way to express how the runtime of an algorithm grows as the size of input grows
# Time Complexity is a measure of the amount of time an algorithm takes to run as a function of the size of its input
# We use Big O notation to describe this growth 

#Key Terms : 
# -> Best Case : The minimum time taken by an algorithm (Best Possible scenario)
# -> Worst Case : The maximum time taken by an algorithm (The worst possible Scenario)
# -> Average Case : The average time taken by an algorithm for different inputs 

# Big O Notation expresses the upper bound of the time complexity.
# It focuses on how the execution time of an algorithm increases as the size of the input grows.

# O(1): Constant time - The algorithm takes same time regardless of the input size 
#                       ex : Acessing an element in an array by index
# O(2): Linear time - The execution time growss linearly with th input size
#                       ex : Finding an element in an unsorted list by scanning each element
# O(n^2): Quadratic time - The execution time grows quadratically as the input size increases 
#                       ex : Bubble sort / selection sort, where each element is comapred with   every other element
# O(log n): Logarithmic time - The execution time grows logarithmically. This is often the case with algorithms that repeatedly divide the input in half
#                       ex : Binary search
# O(n log n) : Linearthmic time - A mix of linear and logarithmic growth. Many efficient sorting algorithms like MErge sort, Quick sort have this complexity 
#                       ex : Merge Sort

#Time Complexity Examples : 
# O(1):
# def check_first_element(arr):
#     print(arr[0])
# check_first_element([1,2,3,4,5])

#O(2)
# def find_element(arr, x):
#     for i in arr:
#         if i == x:
#             return True
        
#     return False

# print(find_element([1,2,3,4,5], 6))

#O(n^2)
# def print_pairs(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             print(arr[i], arr[j])
#         print()

# print_pairs([1,2,3,4])

#O(log n) 
# def binary_search(arr, target):
#     low =0 
#     high = len(arr) -1
#     while low <= high:
#         mid = (low + high) //2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return False
# print(binary_search([1,2,3,4,5], 5))

# -------------------------------------------- Space Complexity ------------------------------------------------
# Space Complexity refers to the amount of memory used by an algoritm as the input size grows 
# O(1): Constant Space - The algorithm uses a fixed amount of space 
# O(n): Linear Search / space - The algorith uses memory proportional to the input size 

# SC Examples 
#O(1)
# def check_first_element(arr):
#     print(arr[0])
# check_first_element([1,2,3,4,5])

#O(n)
# def create_copy(arr):
#     return arr[:]
# create_copy([1,2,3,4,5])

# Ex : Constant Space 
# def print_items(arr):
#     for item in arr:
#         print(item)
# print_items(['apple', 'banana', 'sometjif'])

# Linear Space 
# def copy_list(arr):
#     new_list = []
#     for item in arr:
#         new_list.append(item)
#     print(new_list)

# copy_list([1,2,3,4,5])

# Recursive Space 
# def factorial(n):
#     if n == 0:
#         return 1 
#     return n * factorial(n - 1)

# print(factorial(5))


# ---------------------------------- Analyzing loops in Time Complexity --------------------------------- 
# The time complexity of loops depends on - 
#           How many times the loop runs 
#           Whether there are nested loops
#           Whether the loop is shrinking input ( like divding by 2 ) 

#Single loops (Linear time - O(n))
# def print_all(arr):
#     for i in arr:
#         print(i)
# print_all([1,2,3,4,5])

#Nested loops (Quadratic time - O(n2))
# def print_pairs(arr):
#     for i in arr:
#         for j in arr:
#             print(i, j)
#         print()
# print_pairs([1,2,3,4,5])

# Loop with i *=2 (Logarithmic Time - O(log n))

# def divide_by_two(n):
#     while n > 1 : 
#         n = n //2
#         print(n)
# divide_by_two(4)



# ------------------------------------ Linked List ---------------------------------- 

# Linked List is a linear Data Structure where each element is a separate object. A Linked list is a sequence of nodes where each node contains two parts 
# Data : Actual Values 
# Next : A reference to the next node in the sequence 

# Types of Linked Lists : 

# Single Linked list : A Collection of nodes where each node points to the next node. Focus on operations like insertion, deletion and traversal
# Doubly Linked List : A type of linked list where each node points to both the next and previous nodes , useful for operations where reverse traversal is needed 
# Circular Linked List : A Linked List where the last node points back to the first node , forming a loop.
# Operations to focus on : Insertion (at beginning, middle, end), deletion, searchijng, reversing the list

# Linked list is something like treasure hunting, imagine this, so , instead of having a complete map to the treasure 
# I have a small note that tell me where the second note is and the second note contains the third note , so on to the treasure 
# Each clue / notes is like a box and this box is known as notes 

# Ex : singly linked list is a chain of nodes connected together 
class Node:
    def __init__(self, data):
        self.data = data # This contains the data of the node 
        self.next = None # Link to next node 
class LinkedList:
    def __init__(self):
        self.head = None #Initially the list is empty 

    def insert_at_beginning(self, data):
        new_node = Node(data) # Creates a new node 
        new_node.next = self.head # Makes the new node points to the current head 
        self.head = new_node # Update the head to point to the new node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head: # If the List is empty
            self.head = new_node # The new node is the head 
            return
        last_node = self.head
        while last_node.next: #Traverse to the last node 
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")        

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_beginning(20)
ll.print_list()