# DAY-2 PRACTICE-2

# Variables in Python
first_name = 'Omm'
last_name = 'Miryala'
country = 'India'
city = 'Mumbai'
age = 21
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Omm',
   'lastname':'Miryala',
   'country':'India',
   'city':'Mumbai'
   }

# Printing the values stored in the variables and also the length of the values in the variables
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
print('\n')

# Declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Omm', 'Miryala', 'India', 21, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('\n')

# Different python data types
# Let's declare variables with various data types

first_name = 'Omm'         # str
last_name = 'Miryala'      # str
country = 'India'          # str
city= 'Mumbai'             # str
age = 21                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Omm'))               # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Omm'}))      # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
print('\n')

# Casting or converting data types
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0
print('\n')

# float to int
gravity = 9.81
print(int(gravity))             # 9
print('\n')

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'
print('\n')

# str to int or float
num_str = '10.6'
num_float = float(num_str)       # Convert the string to a float first
num_int = int(num_float)         # Then convert the float to an integer

print('num_int', num_int)        # 10
print('num_float', num_float)    # 10.6
print('num_int', num_int)        # 10
print('\n')

# str to list
first_name = 'Omm'
print(first_name)               # 'Omm'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['O', 'm', 'm']