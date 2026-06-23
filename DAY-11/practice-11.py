# DAY-11 practice-11

# Functions
# Defining a function, Declaring a function, Calling a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!\n")
greet_user()

# function without parameter
def add_numbers():
    """Add two numbers."""
    num1 = 5
    num2 = 10
    total = num1 + num2
    print("The sum is:", total, '\n')
add_numbers()

# Function Returning a Value - Part 1
def generate_fullname():
    firstname = 'Omm'
    lastname = 'Miriyala'
    fullname = firstname + ' ' + lastname
    return fullname
print("Fullname is:", generate_fullname(), '\n')

# Function with Parameter
def add_numbers(num1, num2):
    """Add two numbers."""
    total = num1 + num2
    return total
print("The sum is:", add_numbers(5, 10), '\n')

# Passing Arguments with key and value
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(f'Addition : {add_two_numbers(num2 = 3, num1 = 2)} \n') # Order does not matter

# Function Returning a Value - Part 2
def generate_fullname(firstname, lastname):
    fullname = firstname + ' ' + lastname
    return fullname
print("Fullname is:", generate_fullname('Omm', 'Miriyala'), '\n')

# Function with Default Parameters
def greetings (name = 'User'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Omm'), '\n')

# Arbitrary Number of Arguments
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total
print("The sum is:", add_numbers(1, 2, 3, 4, 5), '\n')

# Default and Arbitrary Number of Parameters in Functions
def add_numbers(num1, num2=0, *args):
    total = num1 + num2
    for num in args:
        total += num
    return total
print("The sum is:", add_numbers(1, 2, 3, 4, 5), '\n')

# Dictionary Unpacking
def display_info(name, age):
    print(f'hi {name}, your age is {age}\n')
user_info = {'name': 'Omm', 'age': 25}
display_info(**user_info)

# Arbitrary Number of Named Arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')
display_info(name='Omm', age=21, city='Mumbai', country='India')

# Function as a Parameter of Another Function
def greet_user(name):
    return f'Hello {name}!'
def display_message(func, name):
    message = func(name)
    print(message)  
print(display_message(greet_user, 'Omm'))