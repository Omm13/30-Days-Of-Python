# DAY-12 exercise-12

# Level 1
# 1. Write a function which generates a six digit/character random_user_id.
def generate_random_user_id():
    import random
    import string
    characters = string.ascii_letters + string.digits
    random_user_id = ''.join(random.choice(characters) for _ in range(6))
    return random_user_id
print(generate_random_user_id(), "is a random user ID.\n")

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def user_id_gen_by_user():
    import random
    import string
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    characters = string.ascii_letters + string.digits
    user_ids = [''.join(random.choice(characters) for _ in range(num_chars)) for _ in range(num_ids)]
    return user_ids
print(user_id_gen_by_user(), "are the generated user IDs.\n")

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    import random
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'rgb({r}, {g}, {b})'
print(rgb_color_gen(), "is a random RGB color.\n")

# Level 2
# 1. write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num_colors):
    import random
    hex_colors = []
    for _ in range(num_colors):
        color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
        hex_colors.append(color)
    return hex_colors
n = int(input("Enter the number of hexadecimal colors to generate: "))
print(list_of_hexa_colors(n), "are the generated hexadecimal colors.\n")

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    import random
    rgb_colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f'rgb({r}, {g}, {b})')
    return rgb_colors
n = int(input("Enter the number of RGB colors to generate: "))
print(list_of_rgb_colors(n), "are the generated RGB colors.\n")

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(color_type, num_colors):
    import random
    if color_type == 'hexa':
        hex_colors = []
        for _ in range(num_colors):
            color = '#' + ''.join(random.choice('0123456789abcdef') for _ in range(6))
            hex_colors.append(color)
        return hex_colors
    elif color_type == 'rgb':
        rgb_colors = []
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb_colors.append(f'rgb({r}, {g}, {b})')
        return rgb_colors
    else:
        return "Invalid color type. Please choose 'hexa' or 'rgb'."
n = int(input("Enter the number of colors to generate: "))
color_type = input("Enter the color type ('hexa' or 'rgb'): ")
print(generate_colors(color_type, n), "are the generated colors.\n")

# Level 3
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(input_list):
    import random
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list
n = int(input("Enter the number of elements in the list: "))
input_list = []
for _ in range(n):
    element = input("Enter an element: ")
    input_list.append(element)
print("Original list:", input_list)
print("Shuffled list:", shuffle_list(input_list), "\n")

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique_random_numbers():
    import random
    return random.sample(range(10), 7)
n = unique_random_numbers()
print("Array of seven unique random numbers in the range 0-9:", n, "\n")