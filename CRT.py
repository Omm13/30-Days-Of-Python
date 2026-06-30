# # 1. Print Weird or not based on the given conditions:
# n = int(input("Enter a number: "))
# if n % 2 != 0:
#     print(f"{n} is weird.")
# elif n % 2 == 0 and 2 < n < 5:
#     print(f"{n} is not weird.")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print(f"{n} is weird.")
# elif n % 2 == 0 and n > 20:
#     print(f"{n} is not weird.")
# else:
#     print("Invalid input")

# # 2(A). Find the largest number among three numbers:
# print("Using logic operators")
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter a third number: "))
# if a > b and a > c:
#     print(f"{a} is the largest number.")
# elif b > a and b > c:
#     print(f"{b} is the largest number.")
# else:
#     print(f"{c} is the largest number.")
# print('\n')

# # 2(B). Find the largest number among three numbers:
# print("Using max function")
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter a third number: "))
# print(max(a, b, c))

# # 2(C). Find the largest number among three numbers:
# print("using nested if else statements")
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter a third number: "))
# if a > b:
#     if a > c:
#         print(f"{a} is the largest number.")
#     else:
#         print(f"{c} is the largest number.")
# else:
#     if b > c:
#         print(f"{b} is the largest number.")
#     else:
#         print(f"{c} is the largest number.")
# print('\n')

# # 3. Print unit bill
# unit = int(input("Enter the number of units consumed: "))
# if unit <= 100:
#     print(f'Bill is Free')
# elif unit in range(101, 201):
#     bill = (unit - 100) * 5
#     print(f"Your bill is: {bill}")
# elif unit in range(201, 301):
#     bill = (100 * 5) + (unit - 200) * 7
#     print(f"Your bill is: {bill}")
# elif unit > 300:
#     bill = (100 * 5) + (100 * 7) + (unit - 300) * 10
#     print(f"Your bill is: {bill}")
# else:
#     print("Invalid input")

# # 4. Print Salay based on tax conditions:
# salary = float(input("Enter your salary: "))
# if salary <= 400000:
#     tax = 0
# elif salary in range(400000, 800000):
#     tax = (salary - 400000) * 0.1
# elif salary in range(800000, 1200000):
#     tax = (salary - 800000) * 0.2 + (400000 * 0.1)
# elif salary in range(1200000, 2000000):
#     tax = (salary - 1200000) * 0.3 + (400000 * 0.2) + (400000 * 0.1)
# elif salary > 2000000:
#     tax = (salary - 2000000) * 0.4 + (800000 * 0.3) + (400000 * 0.2) + (400000 * 0.1)
# print(f"Your tax is: {tax}")
# print(f"Your salary after tax is: {salary - tax}")

# # 5. Print Discount based on the given conditions:
# amount = float(input("Enter the amount: "))
# if amount <= 1000:
#     discount = 0
#     print(f"Your Amount is: {amount}")
# elif amount in range(1001, 1500):
#     discount = amount * 0.05
#     amount = amount - discount
#     print(f"Your Amount is: {amount}")
# elif amount in range(1501, 2000):
#     discount = amount * 0.10
#     amount = amount - discount
#     print(f"Your Amount is: {amount}")
# else:
#     discount = amount * 0.15
#     amount = amount - discount
#     print(f"Your Amount is: {amount}")

# # 6(A). Print Day of the week based on the given number: 
# n = int(input("Enter Choice: "))
# if n == 1:
#     print("Monday")
# elif n == 2:
#     print("Tuesday")
# elif n == 3:
#     print("Wednesday")
# elif n == 4:
#     print("Thursday")
# elif n == 5:
#     print("Friday")
# elif n == 6:
#     print("Saturday")
# elif n == 7:
#     print("Sunday")
# else:
#     print("Invalid input")

# # 6(B). Print Day of the week based on the given number:
# arr = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# i = int(input("Enter Choice: "))
# if 0 <= i <= 6:
#     print(arr[i - 1])   
# else:
#     print("Invalid input")

# # 7. Print operation:
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# i = input("Enter Choice (+, -, *, /): ")
# if i == '+':
#     print(f"Addition of {n1} and {n2} is: {n1 + n2}")
# elif i == '-':
#     print(f"Subtraction of {n1} and {n2} is: {n1 - n2}")
# elif i == '*':
#     print(f"Multiplication of {n1} and {n2} is: {n1 * n2}")
# elif i == '/':
#     if n2 != 0:
#         print(f"Division of {n1} and {n2} is: {n1 / n2}")
#     else:
#         print("Error: Division by zero is not allowed.")
# elif i == '%':
#     if n2 != 0:
#         print(f"Modulus of {n1} and {n2} is: {n1 % n2}")
#     else:
#         print("Error: Modulus by zero is not allowed.")
# else:
#     print("Invalid operation")