# # DAY-14 practice-14

# # Higher Order Functions
# # Fucntion as Parameter
# def sum(a, b):
#     return a + b
# def calculate(func, a, b):
#     return func(a, b)
# result = calculate(sum, 10, 20)
# print(result)  # Output: 30

# # Function as Return Value
# def square(x):
#     return x * x
# def cube(x):
#     return x * x * x
# def get_function(func_type):
#     if func_type == "square":
#         return square
#     elif func_type == "cube":
#         return cube
#     else:
#         return None  
# func = input("Enter function type (square/cube): ")
# selected_function = get_function(func)
# if selected_function:
#     number = int(input("Enter a number: "))
#     result = selected_function(number)
#     print(f"The result is: {result}")
# else:
#     print("Invalid function type.")

# # Python Closures
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a number for y: "))
# closure_function = outer_function(x)
# result = closure_function(y)
# print(f'Result: {result}\n')

# def coffee_maker(flavor):
#     def brew():
#         print(f"brewing {flavor} coffee...")
#     return brew
# flavor = input("Enter coffee flavor: ")
# brew_function = coffee_maker(flavor)
# brew_function()  

# # Python Decorators
# def uppercase_decorator(fucntion):
#     def wrapper():
#         func = fucntion()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
# @uppercase_decorator # Applying decorator to the function
# def say_hi():
#     return 'hello there'

# print(say_hi())  

# def lowercase(function):
#     def wrapper():
#         func = function()
#         make_lowercase = func.lower()
#         return make_lowercase
#     return wrapper
# @lowercase
# def say_hi():
#     return 'HELLO THERE'
# print(say_hi())

# # Built-in Higher Order Functions
# # map() function
# numbers = [1, 2, 3, 4, 5]
# def square(x):
#     return x * x
# numbers_squared = list(map(square, numbers))
# print(numbers_squared)  # Output: [1, 4, 9, 16, 25]

# lst = input("Enter numbers separated by space: ").split()
# def square(x):
#     return x * x
# numbers_squared = list(map(square, map(int, lst)))
# print(numbers_squared)  

# # filter() function
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def even(x):
#     return x % 2 == 0
# even = list(filter(even, num))
# print(even)

# num = input("Enter numbers separated by space: ").split()
# def even(x):
#     return x % 2 == 0
# even = list(filter(even, map(int, num)))
# print(even)

# # Reduce() function
# from functools import reduce
# num = [1, 2, 3, 4, 5]
# def add(x, y):
#     return x + y
# sum = reduce(add, map(int, num))
# print(sum)

# num = input("Enter numbers separated by space: ").split()
# def add(x, y):
#     return x + y
# sum = reduce(add, map(int, num))
# print(sum)