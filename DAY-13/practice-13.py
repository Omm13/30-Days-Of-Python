# DAY-13 practice-13

# List Comprehension
# Standard way to create a list
language = 'Python'
print(f'Standard way to create a list from string')
lst = list(language)
print(type(lst))
print(lst, '\n')

# List Comprehension way to create a list
language = 'Python'
print(f'List Comprehension way to create a list from string')
lst = [char for char in language]
print(type(lst))
print(lst, '\n')

# We can Do Mathematical Operations in List Comprehension
# List compreshension by generating a list of numbers
print(f'List Comprehension way to create a list of numbers')
lst = [num for num in range(1, 11)]
print(type(lst))
print(lst, '\n')

# It is possible to do mathematical operations during iteration
print(f'List Comprehension way to create a list of squares of numbers')
squares = [i * i for i in range(11)]
print(squares, '\n')                    

# It is also possible to make a list of tuples
print(f'List Comprehension way to create a list of tuples')
numbers = [(i, i * i) for i in range(11)]
print(numbers, '\n')

# List comprehension by generating list with conditional statements
# List compreshension by generating a list of even numbers
print(f'List Comprehension way to create a list of even numbers')
lst = [num for num in range(1, 11) if num % 2 == 0]
print(type(lst))
print(lst, '\n')

# List compreshension by generating a list of odd numbers
print(f'List Comprehension way to create a list of odd numbers')
lst = [num for num in range(1, 11) if num % 2 != 0]
print(type(lst))    
print(lst, '\n')

# Lambda Function
print("Lambda Function: it is a small anonymous function that can take any number of arguments, but can only have one expression.\n")

# Creating a lambda function to add arguments
x = lambda a, b, c: a + b + c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("lambda Function to add arguments:", x(a, b, c), '\n')  

# Creating a lambda function to multiply arguments
y = lambda a, b, c: a * b * c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("lambda Function to multiply arguments:", y(a, b, c), '\n')

# Creating a lambda function to find the maximum of two numbers
z = lambda a, b: a if a > b else b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("lambda Function to find the maximum of two numbers:", z(a, b), '\n')

# Self evoking lambda function
print("Self evoking lambda function: it is a function that is invoked immediately after it is defined.\n")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print((lambda a, b: a + b)(a, b), '\n')  

# Creating a lambda function to find the square of a number
square = lambda x: x * x
n = int(input("Enter a number to find the square: "))
print("lambda Function to find the square of a number:", square(n), '\n')

# Creating a lambda function to find the cube of a number
cube = lambda x: x * x * x
n = int(input("Enter a number to find the cube: "))
print("lambda Function to find the cube of a number:", cube(n), '\n')

# lambda function inside another function
def myfunc(n):
    return lambda a: a * n
print("lambda function inside another function: it is a function that returns a lambda function.\n")
n = int(input("Enter a number to multiply: "))
m = int(input("Enter a number to be multiplied: "))
print(myfunc(n)(m), '\n')  