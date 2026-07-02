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

# # DAY-4 practice-4
# # Print the Multiplication Table of a Given Number:
# n = int(input("Enter a number to print its multiplication table: "))
# print(f"Multiplication table of {n}:")
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# # 2. Write a Program to Make a Simple Calculator Using a Switch Case:
# n1 = float(input("Enter first number: "))
# n2 = float(input("Enter second number: "))
# print("Select operation:")
# switch = input("Enter + for addition, - for subtraction, * for multiplication, / for division: ")
# if switch == '+':
#     result = n1 + n2
#     print(f"The result of {n1} + {n2} is: {result}\n")
# elif switch == '-':
#     result = n1 - n2
#     print(f"The result of {n1} - {n2} is: {result}\n")
# elif switch == '*':
#     result = n1 * n2
#     print(f"The result of {n1} * {n2} is: {result}\n")
# elif switch == '/':
#     if n2 != 0:
#         result = n1 / n2
#         print(f"The result of {n1} / {n2} is: {result}\n")
#     else:
#         print("Error: Division by zero is not allowed.  \n")
# else:
#     print("Invalid operation selected.\n")

# # 3. Print a Number in Reverse Order:
# n = int(input("Enter a number to print it in reverse order: "))
# reverse = 0
# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n //= 10
# print("The number in reverse order is:", reverse, '\n')

# # DAY-5 practice-5
# # 1. Calculate the Sum of Digits of a Given Number:
# n = int(input("Enter a number to calculate the sum of its digits: "))
# sum_of_digits = 0
# while n > 0:
#     digit = n % 10
#     sum_of_digits += digit
#     n //= 10
# print("The sum of the digits is:", sum_of_digits, '\n')

# # 2. Write a Program to Check Whether a Character is a Vowel or Consonant:
# char = input("Enter a character: ").lower()
# if char in 'aeiou':
#     print(f"{char} is a vowel.\n")
# elif char.isalpha() and len(char) == 1:
#     print(f"{char} is a consonant.\n")
# else:
#     print("Invalid input. Please enter a single alphabet character.\n")

# # 3. Write a Program to Find the ASCII Value of a Character:
# char = input("Enter a character to find its ASCII value: ")
# ascii_value = ord(char)
# print(f"The ASCII value of '{char}' is: {ascii_value}\n")

# # DAY-6 practice-6
# # 1. Print Sqaure pattern: 
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()
# print("\n")

# # 2. Print Right Angle Triangle pattern:
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()
# print("\n")

# # 3. Print Hallow Rectangle
# for i in range(5):
#     for j in range(10):
#         if i == 0 or i == 4 or j == 0 or j == 9:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# print("\n")

# # DAY-7 practice-7
# # 1. Print Inverted Right Angle Triangle pattern:
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # 2. Print Triangle pattern:
# rows = 5
# for i in range(rows):
#     print(" " * (rows - i - 1) + "* " * (i + 1))

# # 3. Print inverted Triangle pattern:
# rows = 5
# for i in range(rows, 0, -1):
#     print(" " * (rows - i) + "* " * i)
# print("\n")

# # DAY-8 practice-8
# # 1. print : 1 1 2 1 2 3 1 2 3 4 1 2 3 4 5
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
# print("\n")

# # 2. print : 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
# for i in range(1, 6):
#     for j in range(i):
#         print(i, end=" ")
# print("\n")

# # 3. print : 1 2 3 4 5 1 2 3 4 1 2 3 1 2 1
# for i in range(5, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
# print("\n")

# # DAY-9 practice-9
# """
# 1. print : 
# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1
# """
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     for k in range(1, (5 - i) * 2):
#         print(" ", end=" ")
#     for l in range(i, 0, -1):
#         print(l, end=" ")
#     print()
# print("\n")

# # 2. print : A\nA B\nA B C\nA B C D\nA B C D E
# for i in range(5):
#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")
#     print()
# print("\n")

# # 3. print : A B C D E\n  A B C D\n   A B C\n    A B\n     A
# for i in range(5):
#     for j in range(5 - i):
#         print(chr(65 + j), end=" ")
#     print()
# print("\n")

# # DAY-10 practice-10
# # 1. pattern : A\n B B\n C C C\n D D D D\n E E E E E
# for i in range(5):
#     for j in range(i + 1):
#         print(chr(65 + i), end=" ")
#     print()
# print("\n")

# # 2. Pattern char pyramid :
# """
#       A
#     A B A
#   A B C B A
# A B C D C B A
# """
# rows = 4
# for i in range(rows):
#     for j in range(rows - i - 1):
#         print(" ", end=" ")
#     for k in range(i + 1):
#         print(chr(65 + k), end=" ")
#     for l in range(i - 1, -1, -1):
#         print(chr(65 + l), end=" ")
#     print()
# print("\n")

# # 3. Write a program to swap two numbers entered by the user
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# swap = a
# a = b
# b = swap
# print(f"After swapping: first number = {a}, second number = {b}\n")

# # DAY-11 practice-11
# # 1. Write a Program to Find the Largest Number Among Three Numbers:
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a == b == c:
#     print("All three numbers are equal.\n")
# elif a >= b and a >= c:
#     print(f"The largest number is: {a}\n")
# elif b >= a and b >= c:
#     print(f"The largest number is: {b}\n")
# else:
#     print(f"The largest number is: {c}\n")

# # 2. Write a Program to Check Whether a Year Entered by the User is a Leap Year:
# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a leap year.\n")
# else:
#     print(f"{year} is not a leap year.\n")

# # 3. Write a Program to Calculate the Sum of the First N Natural Numbers:
# n = int(input("Enter a natural number: "))
# while n < 1:
#     print("Please enter a natural number (greater than 0).")
#     n = int(input("Enter a natural number: "))
# sum_natural = n * (n + 1) // 2
# print(f"The sum of the first {n} natural numbers is: {sum_natural}\n")    

# # DAY-12 practice-12
# # 1. Write a Program to Find the Factorial of a Number:
# n = int(input("Enter a number to find its factorial: "))
# for i in range(1, n + 1):
#     factorial = 1
#     for j in range(1, i + 1):
#         factorial *= j    
# print(f"The factorial of {i} is: {factorial}\n")

# # 2. Print Fibonacci Series:
# n = int(input("Enter the number of terms for Fibonacci series: "))
# a, b = 0, 1
# print("Fibonacci series:")
# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
# print("\n")

# # 3. Write a Program to Find the GCD or HCF of Two Numbers:
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# hcf = 1
# for i in range(1, min(n1, n2) + 1):
#     if n1 % i == 0 and n2 % i == 0:
#         hcf = i
# print(f"The GCD or HCF of {n1} and {n2} is: {hcf}\n")

# # DAY-13 practice-13
# # 1. Write a Program to Find the LCM of Two Numbers:
# def lcm(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y

#     while True:
#         if greater % x == 0 and greater % y == 0:
#             lcm_value = greater
#             break
#         greater += 1

#     return lcm_value
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# lcm_value = lcm(x, y)
# print(f"The LCM of {x} and {y} is: {lcm_value}\n")

# # 2. Program to calculate the power of number:
# from math import pow
# a = int(input("Enter the base number: "))
# b = int(input("Enter the exponent: "))
# power = pow(a, b)
# print(f"{a} raised to the power of {b} is: {power}\n")

# # 3. Program to Print Integers in Words:
# int_to_word = {
#     0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
#     5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"
# }
# def number_to_words(n):
#     if n in int_to_word:
#         return int_to_word[n]
#     else:
#         return "Number out of range (0-10)"
# n = int(input("Enter an integer between 0 and 10: "))
# word = number_to_words(n)
# print(f"The number {n} in words is: {word}\n")

# # DAY-14 practice-14
# # 1. Print Numbers in Words in Reverse Order Using a Switch Case

# # 2. Write a Program to Display All Factors of a Number:
# def factors(n):
#     factor_list = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factor_list.append(i)
#     return factor_list
# n = int(input("Enter a number to find its factors: "))
# factor_list = factors(n)
# print(f"The factors of {n} are: {factor_list}\n")

# # 3. Amstrong Number or Not:
# n = int(input("Enter a number to check if it is an Armstrong number: "))
# num_str = str(n)
# num_digits = len(num_str)
# sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# if sum_of_powers == n:
#     print(f"{n} is an Armstrong number.")
# else:
#     print(f"{n} is not an Armstrong number.")

# # DAY-15 practice-15
# # 1. Prime Number or Not:
# n = int(input("Enter a number to check if it is prime: "))
# if n > 1:
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             print(f"{n} is not a prime number.\n")
#             break
#     else:
#         print(f"{n} is a prime number.\n")

# # 2. Print Prime Numbers Within a Range
# n1 = int(input("Enter the starting number of the range: "))
# n2 = int(input("Enter the ending number of the range: "))
# print(f"Prime numbers between {n1} and {n2} are:")
# for num in range(n1, n2 + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end=" ")

# # 3. Print Factorial Series:
# n = int(input("\nEnter a number to print its factorial series: "))
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#     print(f"{i}! is: {factorial}")

# DAY-16 practice-16
# # 1. Write a Program to Check Whether a Number is a Palindrome:
# n = input("Enter a number / String to check if it is a palindrome: ")
# original_number = n
# n = str(n)
# if n == n[::-1]:
#     print(f"{original_number} is a palindrome .\n")
# else:
#     print(f"{original_number} is not a palindrome .\n")

# # 2. Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers:
# n = int(input("Enter an integer to check if it can be expressed as the sum of two prime numbers: "))
# if n < 2:
#     print(f"{n} cannot be expressed as the sum of two prime numbers.\n")
# else:
#     found = False
#     for i in range(2, n):
#         if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
#             if all((n - i) % j != 0 for j in range(2, int((n - i)**0.5) + 1)):
#                 print(f"{n} can be expressed as the sum of two prime numbers: {i} + {n - i}\n")
#                 found = True
#                 break
#     if not found:
#         print(f"{n} cannot be expressed as the sum of two prime numbers.\n")

# # 3. Print All Digits and Alphabets Using a For Loop:
# from re import ASCII
# for i in range(0, 10):  # Digits 0-9
#     print(i, end=" ")
# print()  # New line after digits
# for i in range(65, 91):  # Uppercase A-Z
#     print(chr(i), end=" ")
# print()  # New line after uppercase letters
# for i in range(97, 123):  # Lowercase a-z
#     print(chr(i), end=" ")
# print()  # New line after lowercase letters

# DAY-17 practice-17