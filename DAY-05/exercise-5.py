# DAY-5 Exercise-5
# Level 1

# 1. Create an empty list
lst = list()
print(f'list : {lst} \n')  # Output: []

# 2. Create a list with more than 5 items
lst = [1, 2, 3, 4, 5, 6]
print(f'list : {lst} \n')  # Output: [1, 2, 3, 4, 5, 6] 

# 3. Find the length of your list
length = len(lst)
print(f'length of list : {length} \n')  # Output: 6

# 4. Get the first item, the middle item and the last item of the list
lst = [1, 2, 3, 4, 5, 6]
first_item = lst[0]
middle_item = lst[length // 2]  # Using integer division to find the middle index
last_item = lst[-1]
print(f'first item : {first_item}')  # Output: 1
print(f'middle item : {middle_item}')  # Output: 4
print(f'last item : {last_item}\n')  # Output: 6

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_Data_types = ['Omm', 21, 5.9, 89, 'No', 'Mumbai']
print(f'mixed_data_types : {mixed_Data_types} \n')  # Output: ['Omm', 21, 5.9, 89, 'No', 'Mumbai']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'it_companies : {it_companies} \n')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 8. Print the number of companies in the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
number_of_companies = len(it_companies)
print(f'number of companies : {number_of_companies} \n')  # Output: 7

# 9. Print the first, middle and last company
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
first_company = it_companies[0]
middle_company = it_companies[number_of_companies // 2]  # Using integer division
last_company = it_companies[-1]
print(f'first company : {first_company}')  # Output: Facebook
print(f'middle company : {middle_company}')  # Output: Apple
print(f'last company : {last_company}\n')  # Output: Amazon

# 10. Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0] = 'Meta'
print(f'modified it_companies : {it_companies} \n')  # Output: ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 11. Add an IT company to it_companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('Tesla')
print(f'it_companies after adding Tesla : {it_companies} \n')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Tesla']

# 12. Insert an IT company in the middle of the companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Tesla')
print(f'it_companies after inserting Tesla in the middle : {it_companies} \n')  # Output: ['Facebook', 'Google', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 13. Change one of the IT companies names to uppercase (IBM excluded)
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0] = it_companies[0].upper()  # Changing 'Facebook' to uppercase
print(f'it_companies after changing Facebook to uppercase : {it_companies} \n')  # Output: ['FACEBOOK', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 14. Join the it_companies with a string '#;  '
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
joined_string = '#;  '.join(it_companies) + ' #;  '  # Adding the separator at the end as well
print(f'joined string : {joined_string} \n')  # Output: Facebook#;  Google#;  Microsoft#;  Apple#;  IBM#;  Oracle#;  Amazon

# 15. Check if a certain company exists in the it_companies list.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
company_to_check = 'Google'
if company_to_check in it_companies:
    print(f'{company_to_check} exists in the it_companies list.\n')  # Output: Google exists in the it_companies list.  
else:
    print(f'{company_to_check} does not exist in the it_companies list.\n')

# 16. Sort the list using sort() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(f'sorted it_companies : {it_companies} \n')  # Output: ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle']

# 17. Reverse the list in descending order using reverse() method
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort(reverse=True)  # Sorting in descending order
print(f'it_companies in descending order : {it_companies} \n')  # Output: ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

# 18. Slice out the first 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
first_three_companies = it_companies[:3]
print(f'first three companies : {first_three_companies} \n')  # Output: ['Facebook', 'Google', 'Microsoft']

# 19. Slice out the last 3 companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
last_three_companies = it_companies[-3:]
print(f'last three companies : {last_three_companies} \n')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple']

# 20. Slice out the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
middle_index = len(it_companies) // 2
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
if len(it_companies) % 2 == 0:  # If the number of companies is even
    middle_companies = it_companies[middle_index - 1:middle_index + 1]
else:  # If the number of companies is odd
    middle_companies = it_companies[middle_index]
print(f'middle company or companies : {middle_companies} \n')  # Output: Microsoft

# 21. Remove the first IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
it_companies.pop(0)  # Removing the first company
print(f'it_companies after removing the first company : {it_companies} \n')  # Output: ['Google', 'Microsoft', 'Apple', 'IBM']

# 22. Remove the middle IT company or companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:  # If the number of companies is even
    it_companies.pop(middle_index - 1)  # Removing the first middle company
    it_companies.pop(middle_index - 1)  # Removing the second middle company (after the first one is removed)
else:  # If the number of companies is odd
    it_companies.pop(middle_index)  # Removing the middle company
print(f'it_companies after removing the middle company or companies : {it_companies} \n')  # Output: ['Facebook', 'Google', 'Apple', 'IBM']

# 23. Remove the last IT company from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
it_companies.pop()  # Removing the last company
print(f'it_companies after removing the last company : {it_companies} \n')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple']

# 24. Remove all IT companies from the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
it_companies.clear()  # Removing all companies from the list
print(f'it_companies after removing all companies : {it_companies} \n')  # Output: []

# 25. Destroy the IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
print(f'original it_companies : {it_companies}')  # Output: ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
del it_companies  # Destroying the list
try:
    print(it_companies)  # This will raise an error since the list has been destroyed
except NameError:
    print('it_companies list has been destroyed and cannot be accessed.\n')  # Output: it_companies list has been destroyed and cannot be accessed.

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(f'full_stack : {full_stack} \n')  # Output: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
print(f'original full_stack : {full_stack}')  # Output: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'Python')  # Inserting Python after Redux
full_stack.insert(6, 'SQL')  # Inserting SQL after Python
print(f'full_stack after inserting Python and SQL : {full_stack} \n')

# Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
print(f'original ages : {ages}')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'sorted ages : {ages}')  # Output: [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
min_age = ages[0]
max_age = ages[-1]
print(f'min age : {min_age}')  # Output: 19
print(f'max age : {max_age} \n')  # Output: 26

# Add the min age and the max age again to the list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'original ages : {ages}')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.append(min_age)
ages.append(max_age)
print(f'ages after adding min age and max age again : {ages} \n')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]

# Find the median age (one middle item or two middle items divided by two)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'original ages : {ages}')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'sorted ages : {ages}')  # Output: [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
length = len(ages)
if length % 2 == 0:  # If the number of ages is even
    median_age = (ages[length // 2 - 1] + ages[length // 2]) / 2
else:  # If the number of ages is odd
    median_age = ages[length // 2]
print(f'median age : {median_age} \n')  # Output: 24.0

# Find the average age (sum of all items divided by their number)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'original ages : {ages}')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
average_age = sum(ages) / len(ages)
print(f'average age : {average_age} \n')  # Output: 22.8

# Find the range of the ages (max minus min)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'original ages : {ages}')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'sorted ages : {ages}')  # Output: [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
min_age = ages[0]
max_age = ages[-1]
age_range = max_age - min_age
print(f'range of ages : {age_range} \n')  # Output: 7

# Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(f'original ages : {ages}')  # Output: [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'sorted ages : {ages}')  # Output: [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
min_age = ages[0]
max_age = ages[-1]
average_age = sum(ages) / len(ages)
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print(f'abs(min - average) : {min_diff:.2f}')  # Output: 3.80
print(f'abs(max - average) : {max_diff:.2f} \n')  # Output: 3.20

# 2. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]
len_countries = len(countries)
print(f'length of countries list : {len_countries}')  # Output: 195
middle_index = len(countries) // 2
if len(countries) % 2 == 0:  # If the number of countries
    middle_countries = countries[middle_index - 1:middle_index + 1] # Output: [Lesotho]
else:  # If the number of countries is odd
    middle_countries = countries[middle_index]
print(f'middle country(ies) : {middle_countries} \n')  # Output: ['Malawi', 'Malaysia']

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
len_countries = len(countries)
if len_countries % 2 == 0:  # If the number of countries is even
    first_half = countries[:len_countries // 2]
    second_half = countries[len_countries // 2:]
else:  # If the number of countries is odd
    first_half = countries[:len_countries // 2 + 1]
    second_half = countries[len_countries // 2 + 1:]
print(f'first half of countries : {first_half} \n')  # Output: ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi']
print(f'second half of countries : {second_half} \n')  # Output: ['Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea']

# 3. Unpack the first three countries and the rest as scandic countries.
lst = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = lst
print(f'first country : {first_country}')  # Output: China
print(f'second country : {second_country}')  # Output: Russia
print(f'third country : {third_country}')  # Output: USA
print(f'scandic countries : {scandic_countries}')  # Output: ['Finland', 'Sweden', 'Norway', 'Denmark']