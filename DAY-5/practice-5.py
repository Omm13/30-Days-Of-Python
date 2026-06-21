# DAY-5 Practice-5

# Lists

# Creating an empty list
'''Two ways to create an empty list.'''
# 1. Using Built-in Fucntion
lst = list()

# 2. Using Square Brackets
lst = []

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print(f'fruits: {fruits}')
print(f'Length of fruits list: {len(fruits)} \n')

# Accessing List Items using Positive Indexing
print(f'First item: {fruits[0]}')
print(f'Second item: {fruits[1]} \n')

# Accessing List Items using Negative Indexing
print(f'Last item: {fruits[-1]}')
print(f'Second last item: {fruits[-2]} \n ')

# Unpacking a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
first, second, third, *rest = fruits
print(f'First: {first}')
print(f'Second: {second}')
print(f'Third: {third}')
print(f'Rest of the items: {rest} \n')

# Slicing a List
# Positive Indexing
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits[0:5]}')  # ['apple', 'banana', 'cherry', 'kiwi']
print(f'fruits: {fruits[1:5]}')  # ['cherry', 'kiwi', 'mango']
print(f'fruits: {fruits[::2]} \n')  # ['apple', 'cherry', 'mango']

# Negative Indexing
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits[-5:]}')  # ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange'  ]
print(f'fruits: {fruits[-5:-1]}')  # ['banana', 'cherry', 'kiwi', 'mango']
print(f'fruits: {fruits[::-1]}\n')  # ['orange', 'mango', 'kiwi', 'cherry', 'banana', 'apple']

# Modifying List Items
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')  # ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
fruits[0] = 'blackcurrant'
print(f'After Modifying fruits: {fruits} \n')  # ['blackcurrant', 'banana', 'cherry', 'kiwi', 'mango', 'orange']

# Checking Items in a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
if 'banana' in fruits:
    print('Yes, banana is in the fruits list \n')
else:
    print('No, banana is not in the fruits list \n')

# Adding Items to a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
# Using append() method
fruits.append('grapes')
print(f'After Adding grapes: {fruits} \n')  # ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'grapes']

# inserting items to a list
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
fruits.insert(1, 'grapes') # Syntax: list.insert(index, element)
print(f'After Inserting grapes: {fruits} \n')  # ['apple', 'grapes', 'banana', 'cherry', 'kiwi', 'mango', 'orange']

# Removing Items from a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
fruits.remove('banana')  # Syntax: list.remove(element)
print(f'After Removing banana: {fruits} \n')  # ['apple', 'cherry', 'kiwi', 'mango', 'orange']  

# Removing Items Using pop() method
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
fruits.pop(1)  # Syntax: list.pop(index)
print(f'After Removing banana using pop(): {fruits} \n')  # ['apple', 'cherry', 'kiwi', 'mango', 'orange']

# Removing Items Using del keyword
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
del fruits[1]  # Syntax: del list[index]
print(f'After Removing banana using del keyword: {fruits} \n')  # ['apple', 'cherry', 'kiwi', 'mango', 'orange']
del fruits  # Syntax: del list

# Clearing a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
fruits.clear()  # Syntax: list.clear()
print(f'After Clearing fruits: {fruits} \n')  # []

# Copying a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
fruits_copy = fruits.copy()  # Syntax: list.copy()
print(f'fruits_copy: {fruits_copy} \n')  # ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']

# Joining Two Lists
# Using + operator
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
vegetables = ['carrot', 'broccoli', 'spinach', 'cauliflower', 'cabbage', 'lettuce']
print(f'fruits: {fruits}')
print(f'vegetables: {vegetables}')
fruits_and_vegetables = fruits + vegetables  # Syntax: list1 + list2
print(f'fruits_and_vegetables: {fruits_and_vegetables} \n')  # ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'carrot', 'broccoli', 'spinach', 'cauliflower', 'cabbage', 'lettuce']

# Using extend() method
fruits = ['apple', 'banana', 'cherry']
vegetables = ['carrot', 'broccoli', 'spinach']
print(f'fruits: {fruits}')
print(f'vegetables: {vegetables}')
fruits.extend(vegetables)  # Syntax: list1.extend(list2)
print(f'fruits after extending with vegetables: {fruits} \n')  # ['apple', 'banana', 'cherry', 'carrot', 'broccoli', 'spinach']

# Counting Items in a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
print(f'Count of banana in fruits: {fruits.count("banana")} \n')  # Syntax: list.count(element)

# Finding Index of an Item in a List
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange']
print(f'fruits: {fruits}')
print(f'Index of banana in fruits: {fruits.index("banana")} \n')  # Syntax: list.index(element)

# Reversing a List
lst = [3, 1, 4, 2, 5]
print(f'lst: {lst}')
lst.reverse()  # Syntax: list.reverse()
print(f'After Reversing lst: {lst} \n')  # [5, 2, 4, 1, 3]

# Sorting a List
lst = [3, 1, 4, 2, 5]
print(f'lst: {lst}')
lst.sort()  # Syntax: list.sort()
print(f'After Sorting lst: {lst}')  # [1, 2, 3, 4, 5]
lst.sort(reverse=True)  # Syntax: list.sort(reverse=True)
print(f'After Sorting lst in descending order: {lst} \n')  # [5, 4, 3, 2, 1]