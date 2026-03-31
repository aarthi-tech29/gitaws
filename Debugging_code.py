# 1. Index Error in List Access
# numbers = [10, 20, 30, 40]

# for i in range(len(numbers)):
#     print(numbers[i + 1])
# Task: Identify the error and correct the loop so all elements print properly.
# Focus: Index handling

# Error: 
# IndexError: list index out of range
# 1.	len(numbers) = 4 
# 2.	So loop runs: i = 0, 1, 2, 3

# Output:
from sympy import Range


numbers = [10, 20, 30, 40]

for i in range(len(numbers)):
    print(numbers[i])

# ================================================
# 2. Wrong Arithmetic Logic
# def add(a, b):
#     return a - b

# print(add(5, 3))
# Task: Debug the function so it performs addition correctly.
# Focus: Logical error

# Error:
# •	This is a logical error 
# •	The function is using subtraction (-) instead of addition (+)

# Output:
def add(a, b):
    return a + b

print(add(5, 3))
# =====================================================
# 3. Division by Zero
# num = 10
# den = 0
# result = num / den
# print(result)
# Task: Fix the code to handle invalid division safely.
# Focus: Exception handling

# Error:
# ZeroDivisionError
# To divide by 0, which is not allowed

# Output:
num = 10
den = 0
try:
    result = num / den
    print(result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
# =======================================================
# 4. Variable Not Defined
# total = price * quantity
# print(total)
# Task: Find the issue and correct the program.
# Focus: NameError

# Error:
# •	NameError 
# •	Variables price and quantity are not defined

# Output:
price = 100
quantity = 2

total = price * quantity
print(total)
# =======================================================
# 5. Incorrect Indentation
# age = 20
# if age > 18:
# print("Eligible")
# Task: Correct the indentation and run the program successfully.
# Focus: Syntax and structure

# Error:
# IndentationError
# The print statement is not indented inside the if block

# Output:
age = 20
if age > 18:
    print("Eligible")
# =========================================================
# 6. Type Error in Concatenation
# name = "Alice"
# age = 25
# print("Name: " + name + ", Age: " + age)
# Task: Fix the code so it prints correctly.
# Focus: Type conversion

# Error:
# TypeError
# To join (concatenate) a string and an integer

# Output:
name = "Alice"
age = 25
print("Name: " + name + ", Age: " + str(age))
# ========================================================
# 7. Infinite While Loop
# count = 1
# while count <= 5:
#     print(count)
# Task: Debug the loop so it stops correctly after printing 1 to 5.
# Focus: Loop control

# Error:
# Infinite loop
# The variable count is never updated, so the condition is always true

# Output:
count = 1

while count <= 5:
    print(count)
    count += 1  
# ========================================================
# 8. Wrong Comparison Operator
# x = 10
# if x = 10:
#     print("Matched")
# Task: Correct the condition.
# Focus: Conditional syntax

# Error:
# •	SyntaxError 
# •	Used = instead of ==

# Output:
x = 10
if x == 10:
    print("Matched")
# ========================================================
# 9. List Mutation Mistake
# fruits = ["apple", "banana", "cherry"]
# fruits.append["orange"]
# print(fruits)
# Task: Fix the method usage.
# Focus: Function call syntax

# Error:
# TypeError
# Wrong method usage → using append with square brackets instead of parentheses

# Output:
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  
print(fruits)
# ========================================================
# 10. Tuple Modification Error
# data = (1, 2, 3)
# data[1] = 5
# print(data)
# Task: Explain the issue and rewrite the code correctly.
# Focus: Immutable data types

# Error:
# TypeError
# Tuples are immutable → cannot be changed after creation
# •	tuple = fixed (unchangeable) 
# •	list = flexible (changeable)

# Output:
data = (1, 2, 3)

data = list(data)     
data[1] = 5           
data = tuple(data)    

print(data)
# ========================================================
# 11. Wrong Dictionary Key
# student = {"name": "John", "age": 21}
# print(student["marks"])
# Task: Prevent the error and handle missing keys properly.
# Focus: Dictionary access

# Error:
# KeyError
# To access a key that does not exist

# Output:
student = {"name": "John", "age": 21}

print(student.get("marks", "Marks not available"))

# Another Method:
student = {"name": "John", "age": 21}
try:
    print(student["marks"])
except KeyError:
    print("Marks not available")

# ========================================================
# 12. Incorrect Function Argument Count
# def greet(name, city):
#     print(f"{name} lives in {city}")

# greet("Maya")
# Task: Fix the function call or definition.
# Focus: Function parameters

# Error:
# TypeError
# Function expects 2 arguments, but only 1 is given

# Output:
def greet(name, city):
    print(f"{name} lives in {city}")

greet("Maya", "Chennai")
# ========================================================
# 13. Returning Wrong Variable
# def square(n):
#     result = n * n
#     return output

# print(square(4))
# Task: Correct the function.
# Focus: Variable scope

# Error:
# •	NameError 
# •	Returning a variable that is not defined

# Output:
def square(n):
    result = n * n
    return result

print(square(4))
# ========================================================
# 14. String Method Typo
# text = "python"
# print(text.uppercase())
# Task: Fix the method call.
# Focus: Built-in string methods

# Error:
# AttributeError
# Wrong method name: uppercase() does not exist

# Output:
text = "python"
print(text.upper())
# ========================================================
# 15. Wrong Range Usage
# for i in range(1, 10, 0):
#     print(i)
# Task: Debug the loop.
# Focus: Range function

# Error:
# ValueError
# Step value in range() cannot be 0
# range(start, stop, step)
# Step tells how to move → cannot be 0 (no movement)
# If step = 0 → loop doesn’t know how to increment

# Output:
for i in range(1, 10, 1):
    print(i)
# ========================================================
# 16. Using List as a Function
# items = [1, 2, 3]
# print(items(0))
# Task: Correct the code.
# Focus: Indexing vs function call

# Error:
# •	TypeError 
# •	Using a list like a function 
# () → function call for list 
# [] → indexing for list

# Output:
items = [1, 2, 3]

print(items[0])
# ========================================================
# 17. File Open Mode Issue
# file = open("sample.txt", "r")
# file.write("Hello")
# file.close()
# Task: Fix the file handling issue.
# Focus: File modes

# Error:
# •	UnsupportedOperation (IOError) 
# •	File is opened in read mode ("r"), but trying to write

# Output:
file = open("sample.txt", "w")
file.write("Hello")
file.close()
# ========================================================
# 18. Missing Parenthesis
# print("Welcome to Python"
# Task: Correct the syntax error.
# Focus: Basic syntax

# Error:
# SyntaxError
# Missing closing parenthesis )

# Output:
print("Welcome to Python")
# ========================================================
# 19. Wrong Boolean Logic
# marks = 85
# if marks > 50 or marks > 80:
#     print("Excellent")
# Task: Correct the logic to print "Excellent" only for high scores.
# Focus: Boolean conditions

# Error:
# Logical Error
# Condition is wrong

# Output:
marks = 85

if marks > 80 and marks <= 100:
    print("Excellent")
# ========================================================
# 20. Incorrect List Removal
# numbers = [1, 2, 3, 4]
# numbers.remove(10)
# print(numbers)
# Task: Handle the issue properly.
# Focus: List operations

# Error:
# ValueError
# Trying to remove an element that is not in the list

# Output:
numbers = [1, 2, 3, 4]

if 10 in numbers:
    numbers.remove(10)
else:
    print("Element not found")

print(numbers)
# ========================================================
# 21. Faulty Average Calculation
# nums = [10, 20, 30, 40]
# avg = sum(nums) / len(nums) - 1
# print(avg)
# Task: Correct the average formula.
# Focus: Arithmetic logic

# Error:
# Logical Error
# Wrong formula for average

# Output:
nums = [10, 20, 30, 40]
avg = sum(nums) / len(nums)
print(avg)
# ========================================================
# 22. Wrong Input Type
# age = input("Enter age: ")
# if age > 18:
#     print("Adult")
# Task: Fix the code so the comparison works correctly.
# Focus: Input conversion

# Error:
# TypeError
# input() always returns a string, not a number

# Output:
age = int(input("Enter age: "))

if age > 18:
    print("Adult")
# ========================================================
# 23. Reassigning Built-in Name
# list = [1, 2, 3]
# print(list("abc"))
# Task: Explain and correct the issue.
# Focus: Overwriting built-ins

# Error:
# TypeError
# overwrote a built-in function (list) with a variable
# list() is a built-in function used to convert data into a list

# Output:
numbers = [1, 2, 3]
print(list("abc"))    
# ========================================================
# 24. Faulty Swap Logic
# a = 5
# b = 10
# a = b
# b = a
# print(a, b)
# Task: Debug the swap operation.
# Focus: Assignment logic

# Error:
# Logical Error
# Values are getting overwritten

# Output:
a = 5
b = 10

temp = a
a = b
b = temp

print(a, b)
# ========================================================
# 25. Wrong Membership Check
# colors = ["red", "green", "blue"]
# if "yellow" = in colors:
#     print("Found")
# Task: Correct the statement.
# Focus: Membership operator syntax

# Error:
# SyntaxError
# Wrong operator usage

# Output:
colors = ["red", "green", "blue"]

if "yellow" in colors:
    print("Found")
# ======================================================== 


























