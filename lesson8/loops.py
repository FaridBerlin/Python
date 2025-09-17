# loops

value = 1

while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to" + str(value))


# list of names

# for x in names:
#     print(x)

# for x in "Mississippi":
    
#     print(x)

# for x in names:
#     if x == "Charlie":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# 
for x in range(5, 101, 5):
    print(x)
# else: 
#     print("Glad that\'s over!")
names = ["Bob", "Sara", "David"]
actions = ["code", "gym",  "sleep"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + "s")

for action in actions:
    for name in names:
        print(name + " " + action + "s")

# Additional Examples of For Loops and Nested For Loops

# Example 1: Simple for loop with list of numbers
print("\nExample 1: Calculating squares")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    square = num ** 2
    print(f"{num} squared is {square}")

# Example 2: For loop with dictionary
print("\nExample 2: Student grades")
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
for student, grade in student_grades.items():
    if grade >= 90:
        print(f"{student} got an A with {grade}%")
    elif grade >= 80:
        print(f"{student} got a B with {grade}%")
    else:
        print(f"{student} got a C with {grade}%")

# Example 3: Nested for loop - Multiplication table
print("\nExample 3: 3x3 Multiplication Table")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}", end="  ")
    print()  # New line after each row

# Example 4: Nested for loop - Creating a pattern
print("\nExample 4: Star pattern")
for row in range(1, 5):
    for star in range(row):
        print("*", end="")
    print()  # New line after each row

# Example 5: Nested for loop with lists - Creating combinations
print("\nExample 5: Food combinations")
fruits = ["apple", "banana", "orange"]
toppings = ["chocolate", "caramel", "nuts"]
for fruit in fruits:
    for topping in toppings:
        print(f"{fruit} with {topping}")

# 