# DAY-3 EXERCISE-3

from cmath import sqrt
import math

# 1. Declaring Age and Height variables
age = 21
height = 5.8

# 2. Declaring a Variable to store the complex number
complex_number = 2 + 3j

# 3. Area of triangle
print('Area of triangle')
base = input('Enter the base of the triangle: ')
height = input('Enter the height of the triangle: ')
area = 0.5 * float(base) * float(height)
print('The area of the triangle is: ', area,'\n')

# 4. Perimeter of triangle
print('Perimeter of triangle')
side1 = input('Enter the length of side 1: ')
side2 = input('Enter the length of side 2: ')
side3 = input('Enter the length of side 3: ')
perimeter = float(side1) + float(side2) + float(side3)
print('The perimeter of the triangle is: ', perimeter, '\n')

# 5. Area and Perimeter of rectangle
print('Area and Perimeter of rectangle')
length = input('Enter the length of the rectangle: ')
width = input('Enter the width of the rectangle: ')
area_rectangle = float(length) * float(width)
perimeter_rectangle = 2 * (float(length) + float(width))
print('The area of the rectangle is: ', area_rectangle, '\n')
print('The perimeter of the rectangle is: ', perimeter_rectangle, '\n')

# 6. Area and Circumference of circle
print('Area and Circumference of circle')
radius = input('Enter the radius of the circle: ')
area_circle = 3.14 * float(radius) ** 2
circumference_circle = 2 * 3.14 * float(radius)
print('The area of the circle is: ', area_circle, '\n')
print('The circumference of the circle is: ', circumference_circle, '\n')

# 7. Slope of a line , Calculate slope, x intercept and y intercept of Y = 2x - 2
print('Calculate slope, x intercept and y intercept of Y = 2x - 2')
slope = int(input('Enter the slope of the line: '))
y_intercept = int(input('Enter the y-intercept of the line: '))
x_intercept = -y_intercept / slope
print('The slope of the line is: ', slope, '\n')
print('The y-intercept of the line is: ', y_intercept, '\n')
print('The x-intercept of the line is: ', x_intercept, '\n')

# 8. Slope between two points and Euclidean distance between two points
print('Slope between two points and Euclidean distance between two points')
x1, y1 = input('Enter the coordinates of point 1 (x1, y1): ').split(',')
x2, y2 = input('Enter the coordinates of point 2 (x2, y2): ').split(',')

m = (float(y2) - float(y1)) / (float(x2) - float(x1))
distance = math.sqrt((float(x2) - float(x1)) ** 2 + (float(y2) - float(y1)) ** 2)
print('The slope of the line is: ', m, '\n')
print('The Euclidean distance between the two points is: ', distance, '\n')

# 9. Compare the slopes in tasks 7 and 8
print('Compare the slopes in tasks 7 and 8')
if slope == m:
    print('The slopes are equal.\n')
else:
    print('The slopes are not equal.\n')

# 10. Calculate the value of y (y = x^2 + 6x + 9). Try to use different values of x and figure out at what value of x the y is going to be 0.
print('Calculate the value of y (y = x^2 + 6x + 9)')
x = input('Enter the value of x: ')
y = float(x) ** 2 + 6 * float(x) + 9
print('The value of y is: ', y, '\n')

# 11. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print('Find the length of "python" and "dragon" and make a falsy comparison statement.')
text1 = input('Enter the first text: ')
text2 = input('Enter the second text: ')
text1_length = len(text1)
text2_length = len(text2)
print('Length of "python": ', text1_length, '\n')
print('Length of "dragon": ', text2_length, '\n')
if text1_length > text2_length:
    print(f'The length of "{text1}" is greater than "dragon".\n')
elif text1_length < text2_length:
    print(f'The length of "{text1}" is less than "dragon".\n')
else:
    print(f'The length of "{text1}" is equal to "dragon".\n')

# 12. Use the is operator to check if 'on' is found in both 'python' and 'dragon'
print('Use the is operator to check if "on" is found in both "python" and "dragon"')
substring = input('Enter the substring to check: ')
if substring in 'python' and substring in 'dragon':
    print(f'"{substring}" is found in both "python" and "dragon".\n')
else:
    print(f'"{substring}" is not found in both "python" and "dragon".\n')

# 13. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('Use in operator to check if "jargon" is in the sentence.')
sentence = input('Enter a sentence: ')
if 'jargon' in sentence:
    print('"jargon" is found in the sentence.\n')
else:
    print('"jargon" is not found in the sentence.\n')

# 14. Find the length of the text python and convert the value to float and convert it to string
print('Find the length of the text "python" and convert the value to float and convert it to string')
variable = input('Enter a text: ')
length_variable = len(variable)
length_variable_float = float(length_variable)
length_variable_string = str(length_variable_float)
print('The length of the text is: ', length_variable, '\n')
print('The length of the text as float is: ', length_variable_float, '\n')
print('The length of the text as string is: ', length_variable_string, '\n')

# 15. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
print('Check if a number is even or not using python')
number = int(input('Enter a number: '))
if number % 2 == 0:
    print(f'{number} is an even number.\n')
else:
    print(f'{number} is not an even number.\n')

# 16. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print('Check if the floor division of 7 by 3 is equal to the int converted value of 2.7')
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
floor_division = num1 // num2
int_value = int(2.7)
if floor_division == int_value:
    print('The floor division of 7 by 3 is equal to the int converted value of 2.7.\n')
else:
    print('The floor division of 7 by 3 is not equal to the int converted value of 2.7.\n')

# 17. Check if the type of '10' is equal to the type of 10
print('Check if the type of "10" is equal to the type of 10')
text1 = input('Enter the first text: ')
text2 = input('Enter the second text: ')
if type(text1) == type(text2):
    print(f'The type of "{text1}" is equal to the type of "{text2}".\n')
else:
    print(f'The type of "{text1}" is not equal to the type of "{text2}".\n')

# 18. Check if int('9.8') is equal to 10
print('Check if int("9.8") is equal to 10')
number = input('Enter a number: ')
if int(float(number)) == 10:
    print('int("9.8") is equal to 10.\n')
else:
    print('int("9.8") is not equal to 10.\n')

# 19. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
print('Calculate pay of the person')
hours = input('Enter hours: ')
rate_per_hour = input('Enter rate per hour: ')
pay = float(hours) * float(rate_per_hour)
print('The pay of the person is: ', pay , '\n')

# 20. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print('Calculate the number of seconds a person can live')
years = input('Enter number of years: ')
seconds_in_year = 365 * 24 * 60 * 60
total_seconds = float(years) * seconds_in_year
print('The number of seconds a person can live is: ', total_seconds, '\n')

# 21. Write a Python script that displays the following table
print('Display the following table')
print('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125\n')
print('Using for loop to display the following table\n')
for a in range(1, 6):
    print(a, a**0, a**1, a**2, a**3)