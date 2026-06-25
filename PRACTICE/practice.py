# DAY-1 practice-1

# # 1. Program to Print Integer Numbers Entered by the User:
# n = int(input("Enter a number: "))
# print("The number you entered is:", n)

# # 2.Write a Program to Find the Size of int, float, double, and char on Your Computer: 
# import sys
# print("Size of int:", sys.getsizeof(int()))
# print("Size of float:", sys.getsizeof(float()))
# print("Size of double:", sys.getsizeof(float()))  
# print("Size of char:", sys.getsizeof(str()), '\n')

# # 3. Program to Find the Larger Number Among Two Numbers:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# if a > b:
#     print("The larger number is:", a, '\n')
# elif b > a:
#     print("The larger number is:", b, '\n')
# else:
#     print("Both numbers are equal.\n")

# # DAY-2 practice-2

# # 1. Program to Check whether a no. is Even or Odd:
# n = int(input("Enter a number: "))
# if n % 2 == 0:
#     print(n, "is an Even number.\n")
# elif n % 2 != 0:
#     print(n, "is an Odd number.\n")
# else:
#     print("Invalid input.\n")

# # 2. Program to Check Whether the Number is Divisible by 5:
# n = int(input("enter your Number: "))
# if n % 5 == 0:
#     print(n, "is divisible by 5.\n")
# else:
#     print(n, "is not divisible by 5.\n")

# # 3. Program to Check Whether the Number is a Multiple of 7:
# n = int(input("Enter a number: "))
# if n % 7 == 0:
#     print(n, "is a multiple of 7.\n")
# else:
#     print(n, "is not a multiple of 7.\n")

# # DAY-3 practice-3
# # 1. Program to Calculate the Sqaure and cube of a Number:
# n = int(input("Enter a number: "))
# square = n ** 2
# cube = n ** 3
# print("The square of", n, "is:", square)
# print("The cube of", n, "is:", cube, '\n')

# # 2. Program to Calculate the Area of a Circle and Triangle:
# n = float(input("Enter the radius of the circle: "))
# area_circle = 3.14 * n ** 2
# print("The area of the circle is:", area_circle, '\n')
# a = float(input("Enter the base of the triangle: "))
# b = float(input("Enter the height of the triangle: "))
# area_triangle = 0.5 * a * b
# print("The area of the triangle is:", area_triangle, '\n')

# # 3. Write a Program to Find the Quotient and Remainder of Two Integers:
# a = int(input("Enter the Dividend integer: "))
# b = int(input("Enter the divisor integer: "))
# quotient = a // b
# remainder = a % b
# print("The quotient of", a, "and", b, "is:", quotient)
# print("The remainder of", a, "and", b, "is:", remainder, '\n')

