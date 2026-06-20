# LEVEL 1
print("Level 1")
# PYTHON VERSIONS
import sys
print ("Python Version : " + sys.version)

# OPERANDS USING 3 AND 4
print(3 + 4) # Addition(+)
print(4 - 3) # Subtraction(-)
print(3 * 4) # Multiplication(*)
print(4 / 3) # Division(/)
print(4 // 3) # Floor Division Operator(//)
print(4 % 3) # Modulus(%)
print(3 ** 4) # Exponentiation(**)

# STRINGS EXAMPLES
your_name = "Omm Miryala"
print("Hello, " + your_name + "!") # Concatenation

your_family_name = "Miryala"
print("Hello, Your family Name is " + your_family_name + "!") # Concatenation

your_country = "India"
print("Hello, Your country is " + your_country + "!") # Concatenation

# CHECKING DATA TYPES
print(type(10)) 
print(type(9.8))
print(type(3.14))
print(type(4 -4j)) 
print(type(['Omm', 'Miryala', 'Python']))
print(type(your_name)) 
print(type(your_family_name)) 
print(type(your_country)) 

# LEVEL 2
print("Level 2")

# Euclidean distance between (2, 3) and (10, 8)
import math
point1 = (2, 3)
point2 = (10, 8)
distance = round(math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2))
print("The Euclidean distance between", point1, "and", point2, "is:", distance)