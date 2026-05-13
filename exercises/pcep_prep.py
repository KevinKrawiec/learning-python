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
