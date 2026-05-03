from pathlib import Path

# Exercise A: Reading the entire content of a file.
# Description: Open 'file.txt' and print its full content to the console at once.
with open('file.txt') as f:
    contents = f.read()
    print(contents)

# Exercise B: Writing user input to a file using the Path module.
# Description: Get user input, write it to 'file.txt' using Path.write_text, and display the result.
color = input("Your favorite color: ")

path = Path('file.txt')
path.write_text(color)

with open('file.txt') as f:
    contents = f.read()
    print(contents)

# Exercise C: Handling common mathematical and input errors.
# Description: Use try-except blocks to catch ZeroDivisionError and ValueError during division.
try:
    number = int(input("Please select number: "))
    print(10 / number)
except ZeroDivisionError:
    print("Don't divide by 0!")
except ValueError:
    print("That's not a number at all!")

# Exercise D: Simple string replacement.
# Description: Demonstrate how to use the .replace() method to modify text data.
message = "I like C++"
new_message = message.replace('C++', 'Python')
print(new_message)

# Exercise E: Writing formatted strings to a file.
# Description: Using f-strings to write a custom greeting into a text file.
name = input("What is your name: ")

path = Path('file.txt')
path.write_text(f"Welcome {name}")

with open('file.txt') as f:
    contents = f.read()
    print(contents)

# Exercise F: Creating a Guest Book with continuous input.
# Description: Use a while loop to append names to 'file.txt' and then read them line by line.
while True:
    name = input("Please give name: ")

    if name == 'q':
        break

    with open('file.txt', 'a') as f:
        f.write(name + '\n')
    print(f"Add {name} to guest_list.")

with open('file.txt', 'r') as f:
    for line in f:
        print(f"Guest: {line.strip()}")

# Exercise 1: Comparing three methods of reading a file.
# Description: Demonstrate reading a file as a whole, iterating via a loop, and using readlines().
with open('pi_digits.txt') as f:
    contents = f.read()
    print(contents)

with open('pi_digits.txt') as f:
    for line in f:
        print(line.rstrip())

with open('pi_digits.txt') as f:
    lines = f.readlines()

for line in lines:
    print(f"Line: {line.strip()}")

# Exercise 2: Searching and modifying file content on the fly.
# Description: Read 'programming.txt' and replace specific words within the output.
with open('programming.txt') as f:
    contents = f.read()
    print(contents.replace('love', 'hate'))

# Exercise 3: Working with large data (The Pi Birthday Challenge).
# Description: Search for a specific date (birthday) within a text file containing 1,000,000 digits of Pi.
with open('pi_million_digits.txt') as f:
    contents = f.read()

text_contents = str(contents.strip())

birthday = input("Enter your birthday date: ")

if birthday in text_contents:
    print("Your birthday date is in PI number")
else:
    print("Sorry, your birthday date isn't in PI number")

# Exercise 4: Word counter with explicit error reporting.
# Description: A function that counts words in multiple files and warns the user if a file is missing.
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, File {filename} not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"File {filename} contain about {num_words} word.")

filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt', 'abc.txt']

for filename in filenames:
    count_words(filename)

# Exercise 5: Advanced text analysis and silent failure.
# Description: Functions to count total words (silently failing on error) and specific word occurrences.
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        return len(words)

def count_select_word(filename, select_word):
    number = 0
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        words = contents.split()
        for word in words:
            if word.title() == select_word.title():
                number += 1

    return number

print(f"Alice in the Wonderland has: {count_words('alice.txt')} words.")
print(f"{count_select_word('alice.txt', 'alice')}")


# Exercise 6: Safe calculator with results logging.
# Description: Handle input errors and append the successful results of an addition to a file.
try:
    number_one = int(input("Please select the number: "))
    number_two = int(input("Please select the other number: "))
except ValueError:
    print("You have to select a NUMBER!")
else:
    sum_add = number_one + number_two
    sum_add = str(sum_add)
    with open('file.txt', 'a') as f:
        f.write(sum_add + "\n")

with open('file.txt') as f:
    contents = f.read()
    print(contents)
