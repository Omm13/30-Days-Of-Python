# DAY-4 Practice-4
# Strings
# Create a string variable and assign it a value. Print the string and its length.
letter = 'o'
print(letter)
print(len(letter), '\n')

word = 'omm'
print(word)
print(len(word), '\n')

# Multiline string
multiline_string = '''This is a multiline string.
It can span multiple lines. It is useful for long texts.'''
print(multiline_string, '\n')

# String concatenation
first_name = 'Omm'
last_name = 'Miriyala'
full_name = first_name + ' ' + last_name
print('Full name: ', full_name, '\n')

# Escape Sequences
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# String formatting
# Old style string formatting using % operator
# Strings Only Using %s
firstname = 'Omm'
lastname = 'Miriyala'
print('My name is %s %s' % (firstname, lastname), '\n')

# Strings and Numbers Using %s and %d
firstname = 'Omm'
lastname = 'Miriyala'
age = 21
print('My name is %s %s and I am %d years old' % (firstname, lastname, age), '\n')

# Floating point numbers using %f
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.2f' % (radius, area), '\n')

# New style string formatting using format() method
# Strings Only Using {}
a = 'Omm'
b = 'Miriyala'
print('My name is {} {}'.format(a, b), '\n')

# Numbers Only Using {}
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {:.2f}'.format(radius, area), '\n')

# Strings and Numbers Using {} and {}
a = 'Omm'
b = 'Miriyala'
age = 21
print('My name is {} {} and I am {} years old'.format(a, b, age), '\n')

# F-strings (formatted string literals)
# String only
firstname = 'Omm'
lastname = 'Miriyala'
print(f'My name is {firstname} {lastname} \n')

# Numbers only
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.2f} \n')

# Strings and numbers
firstname = 'Omm'
lastname = 'Miriyala'
age = 21
print(f'My name is {firstname} {lastname} and I am {age} years old \n')

# Python Strings as Sequence of Characters
# Unpacking characters 
language = 'Python'
a, b, c, d, e, f = language
print('Unpacking characters: ', a, b, c, d, e, f, '\n')

# Accessing characters in a string using indexing
language = 'Python'
first_character = language[0]
print('First character: ', first_character, '\n')
last_character = len(language) - 1
print('Last character: ', language[last_character], '\n')
last_character_negative_index = language[-1]
print('Last character using negative index: ', last_character_negative_index, '\n')

# Slicing strings
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Reverse a string
name = 'Omm Miriyala'
reverse_name = name[::-1]
print('Reverse name: ', reverse_name, '\n') # alayiriM mmO

# Skip Characters While Slicing
language = 'Python'
skip_second_character = language[0:6:2] # skip every second character
print('Skip every second character: ', skip_second_character, '\n') # Pto

# String Methods
# Capitalize 
language = 'python'
print('Capitalize: ', language.capitalize(), '\n') # Python

# Count
language = 'Thirty Days Of Python'
print('Count: ', language.count('y'), '\n') # 3

# Endswith
language = 'Thirty Days Of Python'
print('Endswith: ', language.endswith('on'), '\n') # True

# Expandtabs
text = 'Hello\tWorld'
print('Expandtabs: ', text.expandtabs(4), '\n') # Hello   World

# find
language = 'Thirty Days Of Python'
print('Find: ', language.find('y'), '\n') # 6

# rfind
language = 'Thirty Days Of Python'
print('rfind: ', language.rfind('y'), '\n') # 15

# format
language = 'Python'
print('Format: ', 'I am learning {}.'.format(language), '\n') # I am learning Python.

# index
language = 'Thirty Days Of Python'
print('Index: ', language.index('y'), '\n') # 6

# rindex
language = 'Thirty Days Of Python'
print('Rindex: ', language.rindex('y'), '\n') # 15

# isalnum
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True
challenge = '30DaysPython'
print(challenge.isalnum()) # True
challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character
challenge = 'thirty days of python 2019'
print(challenge.isalnum(), '\n') # False

# isalpha
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha(), '\n')      # False

# isdecimal
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True 
challenge = '12 3'
print(challenge.isdecimal(), '\n')  # False, space not allowed

# isdigit
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit(), '\n')   # True

# isnumeric
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric(), '\n') # False

# isidentifier
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier(), '\n') # True

# islower
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower(), '\n') # False

# isupper
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper(), '\n') # True

# join
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result, '\n') # 'HTML CSS JavaScript React'

# strip
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'), '\n') # 'irty days of py'

# replace
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding'), '\n') # 'thirty days of coding'

# split
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', '), '\n') # ['thirty', 'days', 'of', 'python']

# swapcase
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase(), '\n')  # tHIRTY dAYS oF pYTHON

# startswith
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase(), '\n')  # tHIRTY dAYS oF pYTHON