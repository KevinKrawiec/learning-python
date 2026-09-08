# 1. Create a list of five programming languages and print the third language using its index.
programming_languages = ["Python", "C++", "C#", "JavaScript", "PHP"]
print(programming_languages[2])

# 2. Create a dictionary representing a user with "username" and "level" keys, then print the value of "level".
user = {"username": "Alice", "level": 20}
print(user["level"])

# 3. Write an if-else statement that checks whether a number is even or odd using the modulo operator.
number = 2

if number % 2 == 0:
    print(f"Number {number} is even")
else:
    print(f"Number {number} is odd")

# 4. Define a function called greet_user() that accepts a name parameter and prints a personalized greeting.
def greet_user(name):
    print(f"Hello {name}!")

greet_user("Tom")

# 5. Create a variable containing a string with extra spaces at both ends and print the cleaned version using strip().
unclean = "  My name is Tom  "
clean = unclean.strip(" ")
print(clean)

# 6. Use a for loop with range() to print the numbers from 1 to 5.
for i in range(1, 6):
    print(i)

# 7. Create a class called Dog with an __init__() method that stores a dog's name, then create one instance of the class.
class Dog:
    def __init__(self, name):
        self.name = name

snowflake = Dog("Snowflake")

print(snowflake.name)

# 8. Ask the user to enter their age using input(), convert the value to an integer, and print whether they are at least 18 years old.
user_age = input("Enter your age: ")
user_age = int(user_age)

if user_age >= 18:
    print("Legal age")
else:
    print("You have to be at least 18 years old")

# 9. Write a try-except block that attempts to divide 20 by a variable and handles a possible ZeroDivisionError.
number = 0

try:
    print(20 / number)
except ZeroDivisionError:
    print("don't divide by zero")

# 10. Create a list of numbers from 1 to 10 using a list comprehension, but include only the numbers greater than 5.
numbers = [x for x in range(1,11) if x > 5]
print(numbers)

# 11. Create a dictionary describing a game with the keys "title", "genre", and "rating".
# Then change the value of the "rating" key.
gta = {
    "title": "GTA VI",
    "genre": "action-adventure",
    "rating": 10}

gta["rating"] = 11

for k, v in gta.items():
    print(f"{k} : {v}")

# 12. Create a list containing several names.
# Use a for loop to print each name in uppercase using upper().
names = ["Tim", "Steve", "Alice", "Tom", "John"]
for name in names:
    print(name.upper())

# 13. Write a function called calculate_price() that takes two parameters:
# price and quantity. The function should return their product.
def calculate_price(price, quantity):
    return price * quantity

banana = calculate_price(10, 11)
print(banana)

# 14. Create an empty dictionary.
# Add three key-value pairs representing countries and their capitals.
empty = {}
empty["Poland"] = "Warsaw"
empty["Germany"] = "Berlin"

for k, v in empty.items():
    print(f"{v} is capital of {k}")

# 15. Create a list containing several numbers, including some repeated values.
# Use a while loop to remove all occurrences of one chosen number.
numbers = [1, 1, 2, 3, 4, 5, 4, 6, 8, 8]
numbers_clean = []

while numbers:
    for number in numbers:
        if number not in numbers_clean:
            numbers_clean.append(number)
            numbers.remove(number)
        else:
            numbers.remove(number)

numbers_clean.sort()
print(numbers)
print(numbers_clean)

# 16. Create a Car class with the attributes brand and mileage.
# Add a drive() method that increases mileage by a given number of kilometers.
class Car:
    def __init__(self, brand, mileage):
        self.brand = brand
        self.mileage = mileage

    def drive(self, number):
        self.mileage += number

miata = Car("Mazda", 1000)
print(miata.mileage)
miata.drive(2000)
print(miata.mileage)

# 17. Create a dictionary with several programming languages and their creators.
# Use a loop to print each key and value in one sentence.

# 18. Ask the user to enter a number.
# Use an if-elif-else statement to check whether the number is positive, negative, or equal to zero.

# 19. Create a list of numbers from 1 to 20 using range().
# Then use a list comprehension to create a new list containing only numbers divisible by 3.

# 20. Create a user dictionary containing the key "username", but without the key "email".
# Try to get "email" using the get() method and provide your own default value.