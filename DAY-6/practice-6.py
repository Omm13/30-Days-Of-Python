# DAY-6 practice-6.py

# Tuples
# Create a tuple
empty_tuple = ()
print("Tuple is: ", empty_tuple)
empty_tuple = tuple()
print("Tuple is: ", empty_tuple, '\n')

# Tuple with Initial Items
numbers = (1, 2, 3, 4, 5)
print(f'Tuple: {numbers} \n')

# Tuple Length
numbers = (1, 2, 3, 4, 5)
print(f'tuple length: {len(numbers)}\n')

# Accessing Tuple Items
# Positive Indexing
numbers = (1, 2, 3, 4, 5)
print(f'First item: {numbers[0]}')
print(f'Second item: {numbers[1]}')

# Negative Indexing
numbers = (1, 2, 3, 4, 5)
print(f'Last item: {numbers[-1]}')
print(f'Second last item: {numbers[-2]}\n')

# Slicing Tuples
# Slicing with Positive Indices
numbers = (1, 2, 3, 4, 5)
print(f'First three items: {numbers[0:3]}')
print(f'Middle items: {numbers[1:4]}')
print(f'Skipping in slices: {numbers[::2]}\n')

# Slicing with Negative Indices
numbers = (1, 2, 3, 4, 5)
print(f'Last three items: {numbers[-3:]}')
print(f'All but last two items: {numbers[:-2]}')
print(f'Skipping in slices: {numbers[::-1]}\n')

# Changing Tuples to Lists
numbers = (1, 2, 3, 4, 5)
lst_numbers = list(numbers)
print(f'Tuple Converted to List: {lst_numbers}\n')

# Changing Lists to Tuples
lst_numbers = [1, 2, 3, 4, 5]
numbers = tuple(lst_numbers)
print(f'List Converted to Tuple: {numbers}\n')

# Checking if an Item Exists in a Tuple
numbers = (1, 2, 3, 4, 5)
if 3 in numbers:
    print("3 is present in the tuple\n")
else:
    print("3 is not present in the tuple\n")

# Joining Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Using + operator
joined_tuple = tuple1 + tuple2
print(f'Joined Tuple: {joined_tuple}\n')

# Deleting Tuples
tuple1 = (1, 2, 3)
del tuple1
try:
    print(tuple1)
except NameError:
    print("tuple1 is deleted and no longer exists\n")