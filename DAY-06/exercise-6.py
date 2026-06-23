# DAY-6 exercise-6

# Level 1
# 1. Create an empty tuple
tpl = ()
print("Empty Tuple: ", tpl, '\n')

# 2. Create a tuples containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Adtiya', 'Karan')
sisters = ('Sana', 'Riya')
print(f'Brothers: {brothers}')
print(f'Sisters: {sisters}\n')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(f'Siblings: {siblings}\n')

# 4. How many siblings do you have?
print(f'Number of siblings: {len(siblings)}\n')

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
lst = list(siblings)
print(f'List of Siblings: {lst}')
lst.append('Gaja')
lst.append('Rani')
print(f'List of Family Members: {lst}')
family_members = tuple(lst)
print(f'Family Members: {family_members}\n')

# Level 2
# 1. Unpack siblings and parents from family_members
siblings, father, mother = family_members[:-2], family_members[-2], family_members[-1]
print(f'Siblings: {siblings}')
print(f'Father: {father}')
print(f'Mother: {mother}\n')

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')
food_stuff_tp = fruits + vegetables + animal_products
print(f'Food Stuff Tuple: {food_stuff_tp}\n')

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(f'Food Stuff List: {food_stuff_lt}\n')

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_tp) // 2
if len(food_stuff_tp) % 2 == 0:
    middle_items = food_stuff_tp[middle_index - 1: middle_index + 1]
else:
    middle_items = food_stuff_tp[middle_index]
print(f'Middle Item(s) from Tuple: {middle_items}')

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(f'First Three Items from List: {first_three_items}')
print(f'Last Three Items from List: {last_three_items}\n')

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("food_stuff_tp tuple has been deleted and is no longer accessible.\n")

# 7. Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia is a Nordic country.\n")
else:
    print("Estonia is not a Nordic country.\n")

# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print("Iceland is a Nordic country.\n")
else:
    print("Iceland is not a Nordic country.\n")

print("End of DAY-6 exercise-6.py\n")