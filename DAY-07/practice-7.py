# DAY-7 practice-7.py

# Sets
# Creating a set
# Empty set
my_set = set()
print("Empty set:", my_set)
# Set with elements
my_set = {1, 2, 3, 4, 5}
print("Set with elements:", my_set, '\n')

# Getting the length of a set
print("Length of the set:", len(my_set), '\n')

# Checking for An item in a set
print("Is 3 in the set?", 3 in my_set)
print("Is 6 in the set?", 6 in my_set, '\n')

# Adding an item to a set
my_set.add(6)
print("Set after adding 6:", my_set)

my_set.update([7, 8, 9])
print("Set after adding multiple items:", my_set, '\n')

# Removing an item from a set
my_set.remove(9)
print("Set after removing 9:", my_set)

# Discarding an item from a set
my_set.discard(10)  # This will not raise an error if the item is not found
print("Set after discarding 10 (not present):", my_set, '\n')

# Using Pop to remove and return an arbitrary item from the set
popped_item = my_set.pop()
print("Popped item:", popped_item)
print("Set after popping an item:", my_set, '\n')

# Clearing a set
my_set.clear()
print("Set after clearing:", my_set, '\n')

# Deleting a set
del my_set
try:
    print(my_set)
except NameError:
    print("my_set has been deleted and is no longer defined.\n")

# Converting a list to a set and Set to list
my_list = [1,3,5,7,9,1,3,5]
my_set = set(my_list)
print("Original list:", my_list)
print("Set created from the list:", my_set)

# Converting a set back to a list
my_list_from_set = list(my_set)
print("List created from the set:", my_list_from_set, '\n')

# Joining two sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item3', 'item4', 'item5'}
# Using union() method
st3 = st1.union(st2)
print(f'st3 (using union()): {st3}')
# using update() method
st1.update(st2)
print(f'st1 (after update()): {st1}\n')

# Intersection of two sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item3', 'item4', 'item5'}
# Using intersection() method
st3 = st1.intersection(st2)
print(f'st3 (using intersection()): {st3}')
# Using & operator
st3 = st1 & st2
print(f'st3 (using & operator): {st3}\n')

# Checking Subset and Superset
st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}
# Using issubset() method
print(f'Is st1 a subset of st2? {st1.issubset(st2)}')
# Using issuperset() method
print(f'Is st1 a superset of st2? {st1.issuperset(st2)}\n')

# Difference of two sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item3', 'item4', 'item5'}
# Using difference() method
st3 = st1.difference(st2)
print(f'st3 (using difference()): {st3}')
# Using - operator
st3 = st1 - st2
print(f'st3 (using - operator): {st3}\n')

# Symmetric Difference of two sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item3', 'item4', 'item5'}
print(f'st1: {st1}')
print(f'st2: {st2}')
# Using symmetric_difference() method
st3 = st1.symmetric_difference(st2)
print(f'st3 (using symmetric_difference()): {st3}')
# Using ^ operator
st3 = st1 ^ st2
print(f'st3 (using ^ operator): {st3}\n')

# Disjoint Sets
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
print(f'st1: {st1}')
print(f'st2: {st2}')
# Using isdisjoint() method
print(f'Are st1 and st2 disjoint? {st1.isdisjoint(st2)}')
print(f'Are st2 and st1 disjoint? {st2.isdisjoint(st1)}\n')