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

# Python Closures
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
closure_function = outer_function(x)
result = closure_function(y)
print(f'Result: {result}\n')

def coffee_maker(flavor):
    def brew():
        print(f"brewing {flavor} coffee...")
    return brew
flavor = input("Enter coffee flavor: ")
brew_function = coffee_maker(flavor)
brew_function()  