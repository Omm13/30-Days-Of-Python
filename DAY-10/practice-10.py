# DAY-10 practice-10

# Loops

# While loop
print("While loop")
count = 0
while count < 5:
    print(count)
    count = count + 1   #prints from 0 to 4

# While loop with else
print("\nWhile loop with else")
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break statement
print("\nBreak statement")
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# Continue statement
print("\nContinue statement")
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

# For loop
print("\nFor loop")
i = 1
for i in range(1, 6):
    print(i)

# For loop with else
print("\nFor loop with else")
for i in range(1, 6):
    print(i)
else:
    print(i)

# Break statement in for loop
print("\nBreak statement in for loop")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

# Continue statement in for loop
print("\nContinue statement in for loop")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# Range function
print("\nRange function")
lst = list(range(5))
print(lst)  # prints [0, 1, 2, 3, 4]
set = set(range(1,5))
print(set)  # prints {1, 2, 3, 4}
tpl = tuple(range(1,12,2))
print(tpl)  # prints (1, 3, 5, 7, 9, 11)

# Nested loops
print("\nNested loops")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# Pass statement
print("\nPass statement")
for i in range(1, 4):
    pass