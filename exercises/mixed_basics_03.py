"""
Task 1: BMI Calculator
- Get weight (kg) and height (m) from user input.
- Calculate BMI using the formula: weight / (height ** 2).
- Print the result formatted to 2 decimal places.
"""
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

bmi = weight / (height ** 2)

print(f"Your BMI: {round(bmi, 2)}")

"""
Task 2: Number Guessing Game
- Generate a random number between 1 and 10.
- Use a while loop to let the user guess the number.
- Provide feedback: "Too high", "Too low", or "Correct!".
"""
import random
searched_number = random.randint(1, 10)

print("Number Guessing Game!")

while True:
    user_number = int(input("Guess number: "))

    if user_number == searched_number:
        print("You win!")
        break
    elif user_number > searched_number:
        print("Too high")
    else:
        print("Too low")

"""
Task 3: Grade List Analysis
- Create a list of student grades.
- Remove the highest and lowest grades using list methods.
- Calculate and print the average of the remaining grades.
"""
student_grades = [2, 3, 3, 4, 4, 5]

student_grades.remove(max(student_grades))
student_grades.remove(min(student_grades))

print(f"Average of the remaining grades: {sum(student_grades)/len(student_grades)}")

"""
Task 4: Word Frequency Counter
- Take a sentence as input from the user.
- Split the sentence into words and use a dictionary to count occurrences of each word.
- Print the dictionary containing word-frequency pairs.
"""
user_words = {}

user_sentence = input("Write a sentence: ")

user_sentence = user_sentence.split()

for word in user_sentence:
    if word not in user_words:
        user_words[word] = 1
    else:
        user_words[word] += 1

for k, v in user_words.items():
    print(f"{k} : {v} occurrences")

"""
Task 5: Temperature Converter Function
- Define a function that converts Celsius to Fahrenheit.
- Use a default parameter value for the function.
- Return the result and call the function with different arguments.
"""
def convert_celsius_to_fahrenheit(celsius=0):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(0))
print(convert_celsius_to_fahrenheit(100))
print(convert_celsius_to_fahrenheit(-10))

"""
Task 6: Safe Division with Exception Handling
- Ask the user for two numbers.
- Implement a try-except block to handle ZeroDivisionError and ValueError.
- Use the 'else' and 'finally' blocks to print additional information.
"""
try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    result = (first_number/second_number)
except ZeroDivisionError:
    print("Error: ZeroDivisionError")
except ValueError:
    print("Error ValueError")
else:
    print(f"Success! The result is {result}")
finally:
    print("thanks for watching")

"""
Task 7: Palindrome Checker
- Take a string input from the user.
- Reverse the string using slicing: [::-1].
- Check if the original string matches the reversed one (case-insensitive).
"""
user_word = input("Enter your word: ").lower()

if user_word == user_word[::-1]:
    print(f"This word {user_word} is palindrome!")
else:
    print(f"This word {user_word} is not palindrome.")

"""
Task 8: List Deduplication and Sorting
- Start with a list containing duplicate names.
- Create a new empty list and use a loop to add names only if they are not already present.
- Sort the final list alphabetically using the .sort() method or sorted() function.
"""
names_list = ['Tom', 'Alex', 'John', 'Donald', 'Tom', 'John', 'Tim']
unique_names = []

for name in names_list:
    if name not in unique_names:
        unique_names.append(name)

unique_names.sort()
print(unique_names)

"""
Task 9: Slicing Mastery
- Create a list of numbers from 1 to 10.
- Use slicing to extract and print the second half of the list.
- Use slicing to print every second element (step).
- Use negative indexing/slicing to reverse the entire list.
"""
numbers = [i for i in range(1, 11)]

print(numbers[5:])
print(numbers[1: 10: 2])
print(numbers[::-1])

"""
Task 10: Working with Modules (math)
- Import the 'math' module.
- Prompt the user for a radius (float).
- Calculate circle area and circumference using math.pi and the power operator (**).
"""
import math
radius = float(input("Enter the radius: "))

print(f"Circle area = {math.pi * radius**2} \n Circumference = {2 * math.pi * radius}")

"""
Task 11: String Cleaning and Methods
- Start with the string: "  python jest SUPER!  "
- Use .strip() to remove whitespace.
- Use .capitalize() to format the string.
- Use .endswith() to check for the exclamation mark.
"""
text = "  python jest SUPER!  "
text = text.strip()
text = text.capitalize()
exclamation = text.endswith("!")
print(text)
print(exclamation)

"""
Task 12: Variable Scope and 'global'
- Define a global variable 'counter'.
- Inside a function, use the 'global' keyword to modify it.
- Call the function multiple times and print the final value of 'counter'.
"""
counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
increment()
print(counter)

"""
Task 13: Working with Matrices (Nested Lists)
- Create a 2D list: [[1, 2], [3, 4]].
- Access and print the element '4' using indexes.
- Update the first element from 1 to 10 and print the matrix.
"""
matrix = [[1, 2], [3, 4]]
print(matrix[1][1])
matrix[0][0] = 10
print(matrix)

"""
Task 14: Conditional Expressions (Ternary Operator)
- Get user age as an integer.
- Use a single-line if-else expression to set 'status'.
- Print the result (e.g., status = "Adult" if age >= 18 else "Minor").
"""

user_age = int(input("Enter your age: "))

status = "Adult" if user_age >= 18 else "Minor"
print(status)

"""
Task 15: Loop Control (break and continue)
- Iterate through numbers from 1 to 20 using range().
- Use 'continue' to skip odd numbers.
- Use 'break' to stop the loop if the number exceeds 15.
- Print the remaining numbers to the console.
"""
for i in range(1,21):
    if i % 2 != 0:
        continue
    elif i > 15:
        break
    else:
        print(i)

"""
Task 16: List Comprehensions
- Create a list of squares for numbers 1 to 10 in a single line.
- Create another list by filtering the first one to include only values > 50.
- Print both lists to see the result.
"""
squares = [i**2 for i in range(1,11)]
squares_bigger_than_fifty = []

for square in squares:
    if square > 50:
        squares_bigger_than_fifty.append(square)

print(squares)
print(squares_bigger_than_fifty)

"""
Task 17: Dictionary Methods (.get and .items)
- Use the .get() method to safely access a non-existent key with a default value.
- Add a new key-value pair to the existing dictionary.
- Iterate through the dictionary using .items() and print each pair.
"""
inventory = {"apples": 5, "bananas": 10}
print(inventory.get('pears', 0))
inventory['oranges'] = 11

for k, v in inventory.items():
    print(f"{k} : {v}")

"""
Task 18: Basic Lambda Functions
- Create a lambda function that multiplies two numbers.
- Assign the lambda to a variable.
- Call the function with different arguments and print the output.
"""
x = lambda a, b : a * b
print(x(5, 6))

"""
Task 19: Equality vs Identity (== vs is)
- Create two identical lists: list1 and list2.
- Create a third variable list3 that references list1.
- Compare them using '==' (value equality) and 'is' (object identity).
- Print the boolean results to see the difference.
"""
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 is list3)
print(list1 == list3)
print(list2 == list3)
print(len(list1) == len(list2))
print(list1 is list2)
print(list1 == list2)

"""
Task 20: Tuple Immutability and Methods
- Create a tuple with some duplicate numbers.
- Use a try-except block to catch a TypeError when attempting to modify an element.
- Use the .count() method to find how many times a specific value appears.
"""
my_tuple = (1, 2, 3, 3, 4, 2)

try:
    my_tuple[2] = 0
except TypeError:
    print("You can't modify a tuple!")

print(my_tuple.count(2))

"""
Task 21: String Manipulation (join and split)
- Start with a list of words.
- Combine them into a single string using the .join() method.
- Split the string back into a list based on a specific delimiter using .split().
"""
words = ['python', 'java', 'c++', 'php']
sentence = "-".join(words)
print(sentence)
words2 = sentence.split("-")
print(words2)

"""
Task 22: Function Arguments (Positional vs Keyword)
- Define a function with positional, keyword, and default parameters.
- Call the function using only positional arguments.
- Call it using keyword arguments in a mixed order.
- Call it relying on the default parameter value.
"""
def introduce(name, age, country="Poland"):
    message = f"{name}: {age} years old, {country} based."

    return message

print(introduce(age=23, name='Kevin', country='Poland'))
print(introduce('Kevin', 23))
print(introduce('Kevin', 23, 'Poland'))

"""
Task 23: Loop with an 'else' Block
- Create a list of numbers.
- Search for the number 7 using a for loop.
- If found, print a message and 'break' the loop.
- Use the loop's 'else' block to print a message only if the loop finished without hitting 'break'.
"""
numbers = [1, 2, 21, 31, 32, 4, 5, 80, 9432, 432, 1, 7, 8]

for number in numbers:
    if number == 7:
        print(f"Number 7 is on {numbers.index(number) + 1} position.")
        break
else:
    print("Number 7 isn't in numbers.")

"""
Task 24: Implicit Return Values (None)
- Define a function that only prints text and has no return statement.
- Call the function and assign its result to a variable.
- Print the variable to verify that it holds 'None'.
"""
def say_hello():
    print("Hello!")

results = say_hello()
print(results)

"""
Task 25: Advanced List Modifications
- Start with a list of 3 strings.
- Insert a new element at a specific index using .insert().
- Remove and return the last element using .pop().
- Delete the first element using the 'del' keyword.
"""
languages = ["Python", "Java", "C++"]

languages.insert(1, "JavaScript")
print(languages)
pop_element = languages.pop()
print(languages)
print(pop_element)
del languages[0]
print(languages)

"""
Task 26: Raising Exceptions
- Define a function that checks if an age argument is valid.
- Use the 'raise' keyword to trigger a ValueError if the age is below 0.
- Call the function inside a try-except block to catch and print the custom error message.
"""
def check_age(age):
    if age < 0:
        raise ValueError("Age can't be less than 0.")
    else:
        return age

try:
    print(check_age(18))
    print(check_age(-1))
except ValueError as VE:
    print(f"Error: {VE}")

"""
Task 27: Floor Division and Modulo with Negative Numbers
- Perform floor division (//) with both positive and negative numbers.
- Perform modulo operations (%) with positive and negative divisors.
- Print results to understand how Python rounds towards minus infinity.
"""
print(5 // 2) #2?
print(-5 // 2) #-2?
print(5 // -2) # -2?
print(5 % 2) #1?
print(5 % -2) #-1?

"""
Task 28: Character to Code and Vice Versa (ord and chr)
- Take a single character input from the user.
- Convert the character to its ASCII/Unicode code using ord().
- Increment the code by 1 and convert it back to a character using chr().
"""
x = ord("a")
print(x)
x += 1
print(x)
x = chr(x)
print(x)

"""
Task 29: Module Import Variants
- Import a full module and access its function via dot notation.
- Import a specific function directly using 'from ... import ...'.
- Import a module with an alias using 'import ... as ...'.
"""
import math
print(math.sin(0))
from math import cos
print(cos(0))
import math as m
print(m.tan(0))

"""
Task 30: Valid and Invalid Variable Names
- Experiment with legal variable names (letters, underscores, digits inside).
- Comment out and label invalid names that cause a SyntaxError (e.g., starting with a digit, using dashes, or reserved keywords).
"""
# 1variable = 10      # Cannot start with a digit
# my-var = 20         # Dash '-' is treated as subtraction
# import = 5          # 'import' is a reserved keyword
# first name = "Tom"  # Spaces are not allowed
# class = "Math"      # 'class' is a reserved keyword

"""
Task 31: Short-circuit Evaluation
- Define a function that prints a message and returns True.
- Test 'False and your_function()' to see if the function execution is skipped.
- Test 'True or your_function()' to observe the same short-circuit behavior.
"""
def is_true():
    print(f"Function was execution")
    return True

print(False and is_true())
print(False or is_true())
print(True or is_true())

"""
Task 32: List Replication and Reference Trap
- Create a nested list using multiplication: [[0]] * 3.
- Modify the sub-list element at matrix[0][0].
- Print the entire matrix to see how shared references affect the output.
"""
matrix = [[0]] * 3
matrix[0][0] = 5
print(matrix)

"""
Task 33: Legacy String Formatting
- Use the old % operator formatting (%s for string, %d for integer).
- Use the .format() method to inject variables into placeholders {}.
- Print both to understand older Python syntax.
"""
name = "Anna"
age = 25
print("%s ma %d lat" % (name, age))
print("{} ma {} lat".format(name, age))

"""
Task 34: Membership Operators (in and not in)
- Check if a character exists within a string using 'in'.
- Test if a number is absent from a list using 'not in'.
- Print the boolean results, noting that string checks are case-sensitive.
"""
word = "Python"
numbers = [1, 2, 3, 4, 5]
print("p" in word.lower())
print(10 not in numbers)
