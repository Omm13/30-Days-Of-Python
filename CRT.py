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

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter a third number: "))
if a > b and a > c:
    print(f"{a} is the largest number.")
elif b > a and b > c:
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number.")