# ============================================================
# PCEP-30-02 Practice Exercises
# ============================================================

# ============================================================
# SECTION 1:
# ============================================================

# Exercise 1: Write a program that prints "Hello, Python!" to the screen.
# Use proper indentation and add a comment describing what the program does.
print("Hello, Python!")
# The program prints a string to the console


# Exercise 2: Declare variables storing: a decimal integer (e.g. 255),
# the same number in hexadecimal and octal, a float in scientific notation,
# a boolean True, and a string "Python". Print all variables.
number = 255
number2 = hex(255)
number3 = oct(255)
is_True = True
word = "Python"

print(f"number = {number}, number2 = {number2}, number3 = {number3}, scientific notation = {number:e}")
print(is_True)
print(word)


# Exercise 3: Compute and print results of: integer division, modulo,
# exponentiation, boolean expressions with 'and'/'not', and bitwise OR/AND.
print(17 // 3)
print(17 % 3)
print(2 ** 3)
print(3 > 2 and 10 != 5)
print(not (5 == 5))
print(0b1010 | 0b0110)
print(0b1010 & 0b0110)


# Exercise 4: Declare x = 10. Using shortcut operators (+=, -=, *=, //=),
# add 5, subtract 3, multiply by 2, then floor-divide by 3. Print after each step.
x = 10
x += 5
x -= 3
x *= 2
x //= 3
print(x)


# Exercise 5: Type casting — read two numbers from the user as strings,
# cast them to float, sum them, and print the result.
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

sum_number = float(first_number) + float(second_number)

print(sum_number)


# Exercise 6: Read the user's name and greet them as "Hi, [name]!".
# Print three values separated by "-" using sep=.
# Print two lines without a newline between them using end=.
name = input("Enter your name: ")
print(f"Hi, {name}")
print(3, 4, 5, sep='-')
print("A", end=" ")
print("B")

# ============================================================
# SECTION 2:
# ============================================================

# Exercise 7: Read an integer from the user. Print "positive", "negative",
# or "zero" depending on its value. Use if-elif-else.
number = int(input("Enter a number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")


# Exercise 8: Read a score (0–100). Print the corresponding letter grade:
# >= 90 → "A", >= 80 → "B", >= 70 → "C", >= 60 → "D", below → "F".
score = int(input("Score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Exercise 9: Use a while loop to print numbers 1 to 10.
# Then use for + range() to print even numbers from 2 to 20.
i = 1

while i <= 10:
    print(i)
    i += 1

for i in range(2, 21):
    if i % 2 == 0:
        print(i)


# Exercise 10: Iterate through [1..10]. Use break to stop when you hit a
# number divisible by 7. Use continue to skip even numbers (print only odd).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 7 == 0:
        break

    if number % 2 == 0:
        continue

    print(number)


# Exercise 11: Use for-else: iterate 2–20, check if a number is prime,
# break on the first prime above 10. Use the else block for the "not found" case.
for n in range(2, 21):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        if n > 10:
            print(f"First prime number is: {n}")
            break
else:
    print("No prime number > 10 was found")


# Exercise 12: Nested loops — print a multiplication table (1–5 × 1–5)
# formatted as a grid.
for i in range(1, 6):
    print(" ")
    for j in range(1, 6):
        print(f"{i} * {j} = {i*j}")


# ============================================================
# SECTION 3:
# ============================================================

# Exercise 13: Create a list of 5 numbers. Append one element, insert at
# index 2, print the last element, slice [1:4], sort and print, delete index 0.
numbers = [1, 3, 2, 5, 7]
numbers.append(4)
numbers.insert(2, 3)
print(numbers[-1])
print(numbers[1:4])
numbers.sort()
print(numbers)
del numbers[0]
print(numbers)


# Exercise 14: Build a list of squares of 1–10 using list comprehension.
# Then create a second list with only even squares, also via comprehension.
squares = [i ** 2 for i in range(1, 11)]
even_squares = [i for i in squares if i % 2 == 0]
print(even_squares)


# Exercise 15: Create a 3×3 matrix (list of lists) and print its diagonal elements.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0], matrix[1][1], matrix[2][2])
