# DAY-12: Practice 12

# Importing a module
import mymodule
print(mymodule.generate_full_name('Omm', 'Miriyala'), '\n') # Omm Miriyala

# Import Functions from a Module
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Omm', 'Miriyala'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'], '\n')

# Import Functions from a Module and Renaming
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Omm', 'Miriyala'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'], '\n')

# Importing Built-in Modules
# Importing Random Module
from random import random, randint, choice, shuffle
print(random()) # Generates a random float number between 0 and 1
print(randint(1, 100)) # Generates a random integer between 1 and 100
print(choice(['Omm', 'Miriyala', 'Python', 'JavaScript'])) # Randomly selects an item from a list
print(shuffle(['Omm', 'Miriyala', 'Python', 'JavaScript'])) # Randomly shuffles a list

# Importing Math Module
from math import *
print(pi) # 3.141592653589793
print(sqrt(16)) # 4.0
print(pow(2, 3)) # 8.0
print(floor(9.81)) # 9
print(ceil(9.81), '\n') # 10

# Importing Statistics Module
from statistics import *
print(mean([1, 2, 3, 4, 5])) # 3
print(median([1, 2, 3, 4, 5])) # 3
print(mode([1, 2, 3, 4, 5, 5])) # 5
print(stdev([1, 2, 3, 4, 5])) # 1.5811388300841898
print(variance([1, 2, 3, 4, 5]), '\n') # 2.5

# Importing OS Module
import os
print(os.name) # posix
print(os.getcwd()) # /home/username
print(os.listdir()) # ['file1.txt', 'file2.txt', 'file3.txt']
print(os.path.join('folder1', 'folder2', 'file.txt')) # folder1/folder2/file.txt
print(os.path.exists('file1.txt')) # True
print(os.path.isfile('file1.txt')) # True
print(os.path.isdir('folder1'), '\n') # True

# Importing Sys Module
import sys
print(sys.version) # 3.8.5 (default, Jul 28 2020, 12:59:40)
print(sys.platform) # linux
print(sys.path) # ['/home/username', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages']
print(sys.argv) # ['practice-12.py']
print(sys.getsizeof(1)) # 28
print(sys.getsizeof('Omm')) # 53
print(sys.getsizeof([1, 2, 3])) # 64
print(sys.maxsize) # 9223372036854775807
print(sys.exit()) # Exits the program