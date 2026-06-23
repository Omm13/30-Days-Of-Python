# DAY-11 Exercise-11
# Level 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum
print("The sum is:", add_two_numbers(5, 10), '\n')

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    return area
print("Area of circle is:", round(area_of_circle(5)), '\n')

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "Error: All arguments must be numbers."
    return total
print("The sum is:", add_all_nums(1, 2, 3, '4', 5), '\n')

# 4. Write a function called convert_celsius_to_fahrenheit. It takes celsius as a parameter and it returns fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print("Fahrenheit is:", convert_celsius_to_fahrenheit(25), '\n')

# 5. Write a function called check_season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.lower()
    if month in ['september', 'october', 'november']:
        return "Autumn"
    elif month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    else:
        return "Invalid month"
print("Season is:", check_season('March'), '\n')

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope
print("Slope is:", calculate_slope(1, 2, 3, 4), '\n')

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "No real roots"
print("Roots are:", solve_quadratic_eqn(1, -3, 2), '\n')  # Roots are: (2.0, 1.0)

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(my_list):
    for item in my_list:
        print(item, end=' ')
print_list([1, 2, 3, 4, 5])

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(my_list):
    reversed_list = []
    for item in my_list:
        reversed_list.insert(0, item)
    return reversed_list
print("\n\nReversed list is:", reverse_list([1, 2, 3, 4, 5]))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(my_list):
    capitalized_list = []
    for item in my_list:
        if isinstance(item, str):
            capitalized_list.append(item.capitalize())
        else:
            capitalized_list.append(item)
    return capitalized_list
print("\nCapitalized list is:", capitalize_list_items(['hello', 'world', 123, 'python']))

# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(my_list, item):
    my_list.append(item)
    return my_list
print("List: ", [1, 2, 3])
print("List after adding item:", add_item([1, 2, 3], 4), '\n')

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list
print("List: ", [1, 2, 3, 4])
print("List after removing item:", remove_item([1, 2, 3, 4], 3), '\n')

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    if n < 0:
        return "Error: Input must be a non-negative integer."
    total = 0
    for i in range(n + 1):
        total += i
    return total
n = int(input("Enter a non-negative integer: "))
print("Sum of numbers is:", sum_of_numbers(n), '\n')

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    if n < 0:
        return "Error: Input must be a non-negative integer."
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total
n = int(input("Enter a non-negative integer: "))
print("Sum of odd numbers is:", sum_of_odds(n), '\n')

# 15. Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(n):
    if n < 0:
        return "Error: Input must be a non-negative integer."
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total
n = int(input("Enter a non-negative integer: "))
print("Sum of even numbers is:", sum_of_evens(n), '\n')

# Level 2
# 1. Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts the number of evens and odds in the number.
def evens_and_odds(n):
    if n < 0:
        return "Error: Input must be a non-negative integer."
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of evens is {evens}. The number of odds is {odds}."
n = int(input("Enter a positive integer: "))
print(evens_and_odds(n), '\n')

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n < 0:
        return "Error: Input must be a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
n = int(input("Enter a whole number: "))
print("Factorial is:", factorial(n), '\n')

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param == 0 or param == '' or param == [] or param == {}:
        return True
    else:
        return False
print("Is empty:", is_empty([]), '\n')

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers):
    if not numbers:
        return "Error: The list is empty."
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    if not numbers:
        return "Error: The list is empty."
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def calculate_mode(numbers):
    if not numbers:
        return "Error: The list is empty."
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    if len(modes) == len(frequency):
        return "No mode"
    return modes

def calculate_range(numbers):
    if not numbers:
        return "Error: The list is empty."
    return max(numbers) - min(numbers)

def calculate_variance(numbers):
    if not numbers:
        return "Error: The list is empty."
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_std(numbers):
    if not numbers:
        return "Error: The list is empty."
    variance = calculate_variance(numbers)
    return variance ** 0.5

numbers = [1, 2, 3, 4, 5, 5]
print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard Deviation:", calculate_std(numbers), '\n')

# 5. Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name="Guest"):
    return f"Hello, {name}!"
print(greet())
print(greet("Alice"), '\n')

# 6. Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print("Named arguments:",)
show_args(name="Alice", age=30, city="New York")
show_args(country="USA", language="English", profession="Engineer",)

# Level 3
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("\nEnter a number: "))
print(f'Is {n} prime?', is_prime(n), '\n')

# 2. Write a functions which checks if all items are unique in the list.
def are_items_unique(my_list):
    return len(my_list) == len(set(my_list))
print("Are all items unique?", are_items_unique([1, 2, 3, 4, 5]), '\n')

# 3. Write a function which checks if all the items of the list are of the same data type.
def are_items_same_type(my_list):
    if not my_list:
        return True
    first_type = type(my_list[0])
    for item in my_list:
        if type(item) != first_type:
            return False
    return True
print("Are all items of the same type?", are_items_same_type([1, 2, 3, 4, 5]), '\n')

# 4. Write a function which check if provided variable is a valid python variable
def is_valid_variable(var):
    import keyword
    if not var.isidentifier() or keyword.iskeyword(var):
        return False
    return True
n = input("Enter a variable name: ")
print(f'\nIs "{n}" a valid Python variable?', is_valid_variable(n))