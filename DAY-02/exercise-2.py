# DAY 2: 30 Days of Python programming

# LEVEL 1
# Assigning values to variables
first_name = 'Omm'
last_name = 'Miryala'
full_name = first_name + ' ' + last_name
country = 'India'
city = 'Mumbai'
age = 21
year = 2005
is_married = False
is_true = True
is_light_on = False
first_name, game, hobby = 'Omm', 'Badminton', 'Photography'

# LEVEL 2
# Checking the data types of the variables
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(is_true))     # bool
print(type(is_light_on)) # bool

# Length of the variables
print(len(first_name))  # 3

# Comparing the length of first_name and last_name
if len(first_name) > len(last_name):
    print(f'Your first name, {first_name} is longer than your last name, {last_name}.\n')
else:
    print(f'Your last name, {last_name} is longer than your first name, {first_name}.\n')

# Decalring two variables and assigning values to them
num_one = 5
num_two = 10

total = num_one + num_two
print(f'The sum of {num_one} and {num_two} is {total}.\n')

difference = num_two - num_one
print(f'The difference between {num_two} and {num_one} is {difference}.\n')

product = num_one * num_two
print(f'The product of {num_one} and {num_two} is {product}.\n')

division = num_two / num_one
print(f'The division of {num_two} by {num_one} is {division}.\n')

remainder = num_two % num_one
print(f'The remainder of {num_two} divided by {num_one} is {remainder}.\n')

exponentiation = num_one ** num_two
print(f'The exponentiation of {num_one} to the power of {num_two} is {exponentiation}.\n')

floor_division = num_two // num_one
print(f'The floor division of {num_two} by {num_one} is {floor_division}.\n')

# Circle Problem
r = 30
area_of_circle = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {area_of_circle}.\n')

circum_of_circle = 2 * 3.14 * r
print(f'The circumference of a circle with radius {r} is {circum_of_circle}.\n')

# User input for radius of a circle
radius = int(input('Enter the radius of a circle: '))
area_of_circle = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area_of_circle}.\n')

# User input for first name and last name
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
print(f'Your full name is {first_name} {last_name}.\n')

# Running help('keywords') to see the list of reserved keywords in Python
help('keywords')