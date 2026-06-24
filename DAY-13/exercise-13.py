# DAY-13 exercise-13

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print(f'Original list: {numbers}')
lst = [num for num in numbers if num <= 0]
print(f'Filtered list (negative and zero): {lst}\n')

# 2. Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'Original list of lists: {list_of_lists}')
flattened_list = [num for sublist in list_of_lists for num in sublist]
print(f'Flattened list: {flattened_list}\n')

# 3. Using list comprehension create the following list of tuples:
lst = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
for item in lst:
    print(f'List of tuples: {item}\n')

# 4. Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for item in countries
    for country, capital in item
]

print(output, '\n')

# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [
    {'country': country.upper(), 'city': capital.upper()}
    for item in countries
    for country, capital in item
]
print(output, '\n')

# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [
    f'{first_name.title()} {last_name.title()}'
    for item in names
    for first_name, last_name in item
]
print(output, '\n')

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x, y, m: y - m * x

m = slope(1, 2, 3, 6)
b = y_intercept(1, 2, m)

print("Slope:", m)
print("Y-Intercept:", b)