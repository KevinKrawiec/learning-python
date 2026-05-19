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


# Exercise 16: Create a 5-element tuple. Check indexing/slicing,
# confirm immutability (try modifying — catch the error), embed tuple in a list.
my_tuple = (4, 3, 5, 6, 7)

print(my_tuple[-1])
print(my_tuple[1:3])

try:
    my_tuple[-1] = 7
except TypeError:
    print("Tuple doesn't support item assignment.")

my_list = [1, 2]
my_list.append(my_tuple)
print(my_list)
my_tuple += (1, 2)
print(my_tuple)


# Exercise 17: Create a dict mapping name → age for 3 people.
# Add and remove an entry, check key existence with 'in',
# iterate through keys(), values(), and items().
people = {
    "Jason": 18,
    "Tom": 20,
    "John": 31
}

people["Tim"] = 17
people.pop("Jason")

print(True if "Kevin" in people else False)

for k, v in people.items():
    print(f"{k} is {v} years old.")

for k in people.keys():
    print(k)

for v in people.values():
    print(v)


# Exercise 18: For s = "Hello, Python World!" — index characters, slice "Python",
# convert case, split into words, check startswith, use escape characters.
s = "Hello, Python World!"

print(f"{s[0]}, {s[7]}, {s[-1]}")
print(s[7:13])
print(s.upper(), s.lower())
words = s.split()
print(s.startswith("Hello"))
print('She said "Python is great!"\n')


# ============================================================
# SECTION 4:
# ============================================================

# Exercise 19: Write a recursive function factorial(n) that computes n!
# using the return keyword. Call it for n = 0, 1, 5, 10.
def factorial(n):
    results = 1

    for i in range(1, n+1):
        results *= i

    return results

print(factorial(5))
print(factorial(0))
print(factorial(1))


# Exercise 20: Write a function that returns None for n < 0, and n² for n >= 0.
# Check the returned value type with type() and 'is None'.
def square_if_positive(n):
    if n >= 0:
        return n ** 2
    else:
        return None

print(square_if_positive(2))
print(type(square_if_positive(-1)))
print((square_if_positive(-1)) is None)


# Exercise 21: Write introduce(name, age, city="Warsaw") that prints person info.
# Call it with positional args, keyword args (different order), and default param.
def introduce(name, age, city="Warsaw"):
    print(f"{name} is {age} years old and lives in {city}")

tim = introduce("Tim", 18, "Berlin")
tom = introduce(city="Paris", name="Tom", age=30)
john = introduce("John", 17)


# Exercise 22: Demonstrate name scope — declare global x = "global",
# create local x inside a function, use the global keyword in another function
# to modify x, then print x after each call.
x = "global"

def local_x():
    x = "local"
    print(x)

def global_x():
    global x
    print(x)

local_x()
global_x()


# Exercise 23: Ask the user for a number, handle ValueError (non-numeric input)
# and ZeroDivisionError (zero input), divide 100 by it, print result,
# and print "done" in a finally block.
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ValueError:
    print("Number must be a number!")
except ZeroDivisionError:
    print("You can't device by zero!")
finally:
    print("done")


# Exercise 24: Build a simple console calculator combining all sections —
# read two numbers and an operator (+, -, *, /, //, **, %), handle bad input
# and ZeroDivisionError, use a function per operation, print result to 2 decimal places.
def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None

def int_division(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None

def exponentiation(a, b):
    return a ** b

def rest_from_division(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None

def calculator():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
    except ValueError:
        print(f"Number must be a valid number!")
        return

    print("+, -, *, /, //, **, %")
    operator = input("Select operator: ")


    if operator == "+":
        result = add(first_number, second_number)
    elif operator == "-":
        result = minus(first_number, second_number)
    elif operator == "*":
        result = multiplication(first_number, second_number)
    elif operator == "/":
        result = division(first_number, second_number)
    elif operator == "//":
        result = int_division(first_number, second_number)
    elif operator == "**":
        result = exponentiation(first_number, second_number)
    elif operator == "%":
        result = rest_from_division(first_number, second_number)
    else:
        print("Error: There is no such operator!")
        return

    if result is not None:
        print(f"Result: {result:.2f}")

calculator()
