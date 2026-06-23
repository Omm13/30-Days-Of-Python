# DAY-9 practice-9

# Conditionals 
# if Condition
a = 10
if a > 5:
    print("a is greater than 5\n")

# if-else Condition
b = 3
if b % 2 == 0:
    print("b is even\n")
else:
    print("b is odd\n")

# if-elif-else Condition
c = 15
if c < 10:
    print("c is less than 10\n")
elif c == 10:
    print("c is equal to 10\n")
else:
    print("c is greater than 10\n")

# Short Hand If-Else
d = 7
print("d is even\n") if d % 2 == 0 else print("d is odd\n")

# Nested If
e = 20 
if e > 10:
    if e % 2 == 0:
        print("e is greater than 10 and even\n")
    else:
        print("e is greater than 10 and odd\n")

# Logical Operators
f = 5
if f > 0 and f < 10:
    print("f is a positive single-digit number\n")
else:
    print("f is either negative, zero, or greater than 9\n")

g = 12
if g < 0 or g > 10:
    print("g is either negative or greater than 10\n")
else:
    print("g is between 0 and 10\n")