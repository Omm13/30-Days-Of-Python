# DAY-8 Practice-8.py

# Dictionaries
# Creating a dictionary
my_dict = {
    "firstname": "Omm",
    "lastname": "Miriyala",
    "age": 21,
    "city": "Mumbai",
    "hobbies": ["coding", "traveling", "cooking"]
}
print("Dictionary:", my_dict, '\n')

# Dictionary Length
print("Length of the dictionary:", len(my_dict), '\n')

# Accessing values in a dictionary
print("First Name:", my_dict["firstname"])
print("Last Name:", my_dict["lastname"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])
print("Hobbies:", my_dict["hobbies"], '\n')

# Modifying values in a dictionary
my_dict["age"] = 22
print("Updated Age:", my_dict["age"], '\n')

# Adding new key-value pairs to a dictionary
my_dict["profession"] = "Software Engineer"
print("Updated Dictionary:", my_dict, '\n')

# Checking if a key exists in a dictionary
if "firstname" in my_dict:
    print("Key 'firstname' exists in the dictionary.\n") 
else:
    print("Key 'firstname' does not exist in the dictionary.\n")

# Removing key-value pairs from a dictionary
del my_dict["city"]
print("Dictionary after removing 'city':", my_dict, '\n')

# Changing Dictionary to a List
my_list = list(my_dict.items())
print("Dictionary converted to a list of tuples:", my_list, '\n')

# Changing List to a Dictionary
new_dict = dict(my_list)
print("List converted back to a dictionary:", new_dict, '\n')

# Copying a dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict, '\n')

# Getting all keys and values from a dictionary
print("Keys:", my_dict.keys())
print("Values:", my_dict.values(), '\n')

# Deleting a dictionary
del my_dict
del my_list
del new_dict
del copied_dict
print("All dictionaries and lists have been deleted.")