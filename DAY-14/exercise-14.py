# Level 1

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Difference between map, filter, and reduce.
print("1. Map() : Applies a function to all the items in an input list.\n 2. Filter() : Creates a list of elements for which a function returns true.\n 3. Reduce() : Applies a rolling computation to sequential pairs of values in a list.\n")

# 2. Difference between higher-order functions, closures, and decorators.
print("1. Higher-order functions are functions that can take other functions as arguments or return functions as results.\n 2. Closures are functions are basically nested functions that remebers the parent behavior / Functions.\n 3. Decorators are functions that take another function as an argument and extend its behavior without explicitly modifying it.\n")

# 3. Define a call function before map, filter or reduce, see examples.
from functools import reduce

def square(x):
    return x * x
def is_even(x):
    return x % 2 == 0
def add(x, y):
    return x + y
numbers_squared = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))
sum_of_numbers = reduce(add, numbers)
print("Numbers Squared:", numbers_squared)
print("Even Numbers:", even_numbers)
print("Sum of Numbers:", sum_of_numbers, '\n')

# 4. Use for loop to print each country in the countries list.
for country in countries:
    print(country, end=", ")
print('\n')

# 5. Use for loop to print each name in the names list.
for name in names:
    print(name, end=", ")
print('\n')

# 6. Use for loop to print each number in the numbers list.
for number in numbers:
    print(number, end=", ")
print('\n')

# Level 2
# 1. Use map to create a new list by changing each country to uppercase in the countries list
countries_uppercase = list(map(lambda country: country.upper(), countries))
print("Countries in Uppercase:", countries_uppercase, '\n')

# 2. Use map to create a new list by changing each number to its square in the numbers list
numbers_squared = list(map(lambda number: number ** 2, numbers))
print("Numbers Squared:", numbers_squared, '\n')

# 3. Use map to change each name to uppercase in the names list
names_uppercase = list(map(lambda name: name.upper(), names))
print("Names in Uppercase:", names_uppercase, '\n')

# 4. use filter to filter out countries containing 'land'
countries_with_land = list(filter(lambda country: 'land' in country.lower(), countries))
print("Countries containing 'land':", countries_with_land, '\n')

# 5. use filter to filter out countries having exactly six characters
countries_with_six_chars = list(filter(lambda country: len(country) == 6, countries))
print("Countries with exactly six characters:", countries_with_six_chars, '\n')

# 6. use filter to filter out countries containing six letters and more in the country list
countries_with_six_or_more_chars = list(filter(lambda country: len(country) >= 6, countries))
print("Countries with six letters or more:", countries_with_six_or_more_chars, '\n')

# 7. use filter to filter out countries starting with 'E'
e = filter(lambda country: country.lower().startswith('e'), countries)
print("Countries starting with 'E':", list(e), '\n')

# 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce
numbers_squared = list(map(lambda number: number ** 2, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers_squared))
sum_of_even_numbers = reduce(lambda x, y: x + y, even_numbers)
print("Numbers Squared:", numbers_squared)
print("Even Numbers after Squaring:", even_numbers)
print("Sum of Even Numbers after Squaring:", sum_of_even_numbers, '\n')

# 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(input_list):
    return list(filter(lambda item: isinstance(item, str), input_list))
numbers_and_strings = [1, 'hello', 2, 'world', 3, 'python', 4, 'programming']
string_list = get_string_lists(numbers_and_strings)
print("List containing only string items:", string_list, '\n')

# 10. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
sum = reduce(lambda x, y: x + y, numbers)
print(f'sum: {sum} \n')