# DAY-14 practice-14

# Higher order functions
# Functions as parameters
def apply_function(func, value):
    return func(value)
def square(n):
    return n * n
def cube(n):
    return n * n * n
n = int(input('Enter a number: '))
print(f'square of {n}: {apply_function(square, n)}')
print(f'cube of {n}: {apply_function(cube, n)}\n')
