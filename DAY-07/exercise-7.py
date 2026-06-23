# DAY-7 exercise-7 

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("it_companies:", it_companies)
A = {19, 22, 24, 20, 25, 26}
print("Set A:", A)
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("Set B:", B)
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Age list:", age , '\n')

# Level 1
# 1. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies), '\n')

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("it_companies after adding Twitter:", it_companies, '\n')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Snapchat', 'TikTok'])
print("it_companies after adding multiple companies:", it_companies, '\n')

# 4. Remove one of the companies from the set it_companies
it_companies.pop()
print("it_companies after popping an item:", it_companies, '\n')

# 5. What is the difference between remove and discard
print("Difference between remove and discard:")
print("remove() will raise a KeyError if the item is not found in the set, while discard() will not raise an error if the item is not found.", '\n')

# Level 2
# 1. Join A and B
print("Union of A and B:", A.union(B), '\n')

# 2. Find A intersection B
print("Intersection of A and B:", A.intersection(B), '\n')

# 3. Is A subset of B
print("Is A a subset of B?", A.issubset(B), '\n')

# 4. Are A and B disjoint sets
print("Are A and B disjoint sets?", A.isdisjoint(B), '\n')

# 5. Join A with B and B with A
print("Union of A and B:", A.union(B))
print("Union of B and A:", B.union(A), '\n')

# 6. What is the symmetric difference between A and B
print("Symmetric difference between A and B:", A.symmetric_difference(B), '\n')

# 7. Delete the sets completely
del A
del B
try:
    print(A)
except NameError:
    print("Set A has been deleted and is no longer defined.")
try:
    print(B)
except NameError:
    print("Set B has been deleted and is no longer defined.", '\n')

# level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Length of age list:", len(age))
print("Length of age set:", len(age_set))
if len(age) > len(age_set):
    print("The age list is bigger than the age set.\n")
elif len(age) < len(age_set):
    print("The age set is bigger than the age list.\n")
else:
    print("The age list and age set are of the same length.\n")

# 2. Explain the difference between the following data types: string, list, tuple and set
print("Difference between string, list, tuple and set:")
print("String: A string is a sequence of characters enclosed in quotes. It is immutable, meaning it cannot be changed after it is created.")
print("List: A list is an ordered collection of items that can be of different types. It is mutable, meaning it can be changed after it is created.")
print("Tuple: A tuple is an ordered collection of items that can be of different types. It is immutable, meaning it cannot be changed after it is created.")
print("Set: A set is an unordered collection of unique items. It is mutable, meaning it can be changed after it is created, but it does not allow duplicate items.", '\n')

# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
print("Words in the sentence:", words)
unique_words = set(words)
print("Unique words in the sentence:", unique_words)
print("Number of unique words in the sentence:", len(unique_words), '\n')