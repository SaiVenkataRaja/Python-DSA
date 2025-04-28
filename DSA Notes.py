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
