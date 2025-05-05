#Challenge 1 : Write a function that takes a list of names and a target name. 
#Use linear search to check if the name exists. If it exists, return "Found at position X", otherwise "Not found".

# def search(names, TName):
#     for i in range(len(names)):
#         if names[i] == TName:
#             #return f"Found at Positiom {i}"
#             return True    
#     #return "Not Found"
#     return False     

# print(search(["sai", "venkata", "raja"], "sai"))
# print(search(["sai", "venkata", "raja"], "John cena"))

# Challenge 2 : selection sort 
# Sort the following list using Selection Sort manually (write the list after each full outer loop):
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]  
#         print(f"After swapping index {i} and {min_index}: {arr}")
#     return arr

# arr = [8, 3, 5, 1, 4]
# print(selection_sort(arr))

# Challenge 3 : Fibonacci series : Recursion
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n ==1 :
#         return 1 
#     else: 
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(10))

# Challenge 3.2 : Recursion 
# Write a recursive function that takes an integer and returns the sum of its digits.
# def fibo(n):
#     if n == 0:
#         return 0 
#     else: 
#         return (n % 10) + fibo(n // 10)
# print(fibo(1234))

# Challenge 3.3 : Write a recursive function that takes an integer and returns the reversed number.
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]
# print(reverse_string("sai"))


# Challenge 4 : Time complexity 
# def something(arr):
#     for i in arr:
#         print(i)
#         print()
#     for j in arr:
#         for k in arr:
#             for l in arr:
#                 print(j, k, l)
#         print()
   
# something([1,2,3,4,5])

# Linked List Practice : 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None 
    
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def print(self) : 
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")
# ll = LinkedList()
# ll.insert_at_beginning(10)
# ll.insert_at_beginning(20)
# ll.insert_at_beginning(30)
# ll.print()

# Challenge 5 : Linked List 
# Write a function to reverse a singly linked list.
# After reversing, the head of the list should point to the last node, 
# and all the nodes should point to their previous node. 

# class Node:
#     def __init__(self, data):
#         self.data =data 
#         self.next = None 
    
# def print_list(head):
#     while head:
#         print(head.data, end=" -> ")
#         head = head.next
#     print("None")

# def reversed_lst(head):
#     prev = None
#     curr = head 

#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node
#     return prev 

# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)

# print("Original List : ")
# print_list(head)
# reversed_head = reversed_lst(head)
# print("Reversed List : ")
# print_list(reversed_head)

# Insertion at the beginning 
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
