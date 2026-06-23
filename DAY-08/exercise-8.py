# DAY-8 exercise-8

# 1. Create an empty dictionary called Dog.
Dog = {}
print("Empty Dictionary:", Dog, '\n')

# 2. Add name, breed, color, and age to the Dog dictionary.
Dog["name"] = "Buddy"
Dog["breed"] = "Golden Retriever"
Dog["color"] = "Golden"
Dog["age"] = 5
print("Dog Dictionary after adding details:", Dog, '\n')

# 3. Create a student dictionary and add names, age, marital status, skills, country, city, and address as keys and their values.
student = {
    "firstname": "Omm",
    "lastname": "Miriyala",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "Excel", "Data Analysis"],
    "city": "Mumbai",
    "country": "India",
    "address": "Mira road, Mumbai"
}
print("Student Dictionary:", student, '\n')

# 4. Get the length of the student dictionary.
print("Length of the student dictionary:", len(student), '\n')

# 5. Get the value of skills and check the data type of skills.
print("Skills:", student["skills"])
print("Data type of skills:", type(student["skills"]), '\n')

# 6. Modify the skills values by adding one or two skills.
student["skills"].append("Machine Learning")
print("Updated Skills:", student["skills"], '\n')

# 7. Get the dictionary keys as a list.
keys_list = list(student.keys())
print("Dictionary Keys as a List:", keys_list, '\n')

# 8. Get the dictionary values as a list.
values_list = list(student.values())
print("Dictionary Values as a List:", values_list, '\n')

# 9. Change the dictionary to a list of tuples using items() method.
items_list = list(student.items())
print("Dictionary converted to a list of tuples:", items_list, '\n')

# 10. Delete one of the items in the dictionary.
del student["marital_status"]
print("Student Dictionary after deleting 'marital_status':", student, '\n')

# 11. Delete the dictionary completely.
del student
print("Student dictionary has been deleted.")