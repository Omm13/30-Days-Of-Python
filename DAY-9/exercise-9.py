# DAY-9 exercise-9

# Level 1
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. 
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.\n")
else:
    years_to_wait = 18 - age
    print(f"You need to wait {years_to_wait} more years to drive.\n")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
myage = int(input("Enter my age: "))
yourage = int(input("Enter your age: "))
if myage > yourage:
    print("I am older than you.\n")
elif myage < yourage:
    print("You are older than me.\n")
else:
    print("We are the same age.\n")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
if a > b:
    print("a is greater than b.\n")
elif a < b:
    print("a is smaller than b.\n")
else:
    print("a is equal to b.\n")


# Level 2
# 1. Write a code which gives grade to students according to theirs scores:
''' 90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F '''

score = float(input("Enter the student's score: "))
if 90 <= score <= 100:
    print("Grade: A\n")
elif 80 <= score < 90:
    print("Grade: B\n")
elif 70 <= score < 80:
    print("Grade: C\n")
elif 60 <= score < 70:
    print("Grade: D\n")
elif 0 <= score < 60:
    print("Grade: F\n")
else:
    print("Invalid score. Please enter a score between 0 and 100.\n")

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring. June, July or August, the season is Summer.
month = input("Enter the month: ").strip().capitalize()
if month == "September" or month == "October" or month == "November":
    print("The season is Autumn.\n")
elif month == "December" or month == "January" or month == "February":
    print("The season is Winter.\n")
elif month == "March" or month == "April" or month == "May":
    print("The season is Spring.\n")
elif month == "June" or month == "July" or month == "August":
    print("The season is Summer.\n")
else:
    print("Invalid month. Please enter a valid month name.\n")

# 3. The following list contains some fruits: fruits = ['banana', 'orange', 'mango', 'lemon']. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists in the list print('That fruit already exists in the list').
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()
if fruit in fruits:
    print("That fruit already exists in the list.\n")
else:
    fruits.append(fruit)
    print("Modified list of fruits:", fruits, "\n")

# Level 3
# 1. Here we have a person dictionary.
person = {
    'first_name': 'Omm',
    'last_name': 'Miriyala',
    'age': 21,
    'country': 'India',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'GCC Road',
        'zipcode': '401107'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("The middle skill is:", skills[middle_index], "\n")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("The person has Python skill.\n")
    else:
        print("The person does not have Python skill.\n")

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, print('He is a fullstack developer'), else print('unknown title').
skills = person.get('skills', [])
if set(skills) == {'JavaScript', 'React'}:
    print("He is a front end developer.\n")
elif set(skills) == {'Node', 'Python', 'MongoDB'}:
    print("He is a backend developer.\n")
elif set(skills) == {'React', 'Node', 'MongoDB'}:
    print("He is a fullstack developer.\n")
else:
    print("Unknown title.\n")

# If the person is married and if he lives in India, print the information in the following format: 'Omm Miriyala lives in India. He is not married.'.
if person.get('is_married') is False and person.get('country') == 'India':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married.\n")
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.\n")

print("End of exercise-9.\n")