# Exercise 1: Cinema management system
# 1. Create a list called 'spectators' containing dictionaries.
#    Each dictionary represents a person with keys: 'name', 'age', and 'have_ticket' (boolean).
# 2. Use a 'for' loop to iterate through the list:
#    - If the person has a ticket, print: "Welcome to the screening, [name]!"
#    - If not, print: "[name], you need to go to the box office."
# 3. Add an 'if' condition to check the age: if the person is under 13,
#    add a note: "(Guardian's consent required for films rated 13+)".
# 4. Finally, print the total number of people in the list using the len() function.

spectators = [
    {'name': 'Tim', 'age': 18, 'have ticket': True},
    {'name': 'Alice', 'age': 12, 'have ticket': True},
    {'name': 'Tom', 'age': 18, 'have ticket': False}
]

for spectator in spectators:
    if spectator['have ticket'] == True:
        print(f"{spectator['name']}, we invite you to the screening")
    else:
        print(f"{spectator['name']}, you have to buy a ticket!")

    if spectator['age'] < 13:
        print("Guardian's consent required for films from 13 years of age")

def count_spectators(spectators_list):
    count = 0
    for spectator in spectators_list:
        count += 1

    return count

print(f"Spectators amount: {count_spectators(spectators)}")

#----------------
# Exercise 2: Inventory Management System:
# 1. Store products in a dictionary where the key is the product name
#    and the value is its price (e.g., inventory = {'apple': 2.5}).
# 2. Define a function 'add_product()' that takes the inventory dictionary,
#    asks the user for a name and price, and adds them to the dictionary.
# 3. Define a function 'show_inventory()' that prints all products
#    and their prices using a loop.
# 4. Use a 'while' loop to keep the program running until the user types 'quit'.
#    Provide options to "add", "show", or "quit".

inventory = {
    'apple': 2.5,
    'banana': 3.5,
    'bread': 4.0
}

def add_product(inventory_dictionary):
    item_name = input("Enter the product name: ")
    item_price = float(input("Enter the product price: "))

    inventory_dictionary[item_name] = item_price

def show_inventory(inventory_dictionary):
    for k, v in inventory_dictionary.items():
        print(f"{k.title()} costs: {v}$")

while True:
    print("Select one of the options: \nadd \nshow \nquit")
    option = input("Your option: ").lower()

    if option == 'add':
        add_product(inventory)
    elif option == 'show':
        show_inventory(inventory)
    elif option == 'quit':
        break
    else:
        print("You can't select this option, please try again")

#----------------
# Exercise 3: Library Management System
# 1. Define a 'Book' class:
#    - '__init__' method should take 'title' and 'author'.
#    - Add an attribute 'is_borrowed' with a default value of False.
#    - Add a method 'borrow_book()' that sets 'is_borrowed' to True
#      and prints a confirmation message.
#    - Add a method 'return_book()' that sets 'is_borrowed' to False
#      and prints a return message.
# 2. Create a 'library' list and populate it with three 'Book' instances.
# 3. Use a 'for' loop to display the title and author of each book.
# 4. Call 'borrow_book()' and 'return_book()' on one of the instances to test the logic.

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        self.is_borrowed = True
        print(f"{self.title} was borrowed")

    def return_book(self):
        self.is_borrowed = False
        print(f"{self.title} was returned")

it = Book('It', 'Stephen King')
python = Book('Python Crash Course', 'Eric Matthes')
english = Book('English Grammar in Use', 'Raymond Murphy')

library = [it, python, english]

for book in library:
    print(f"{book.title}: {book.author}")

it.borrow_book()
it.return_book()

#----------------
# Exercise 4: Smart Home Manager
# 1. Define a 'Device' class:
#    - '__init__' takes 'name' and sets 'is_on' to False by default.
#    - Add 'turn_on()' and 'turn_off()' methods that change the state and print a message.
# 2. Define a 'SmartLight' class that inherits from 'Device':
#    - Add a 'brightness' attribute with a default value of 100.
#    - Add a 'set_brightness(level)' method to update and print the brightness.
# 3. Create a list called 'home_devices' and add one 'Device' and two 'SmartLight' instances.
# 4. Use a loop to iterate through 'home_devices':
#    - Call 'turn_on()' for every device.
#    - Check if the device is an instance of 'SmartLight' (using isinstance()).
#    - If it is, call 'set_brightness(50)' on it.

class Device:
    def __init__(self, name, is_on=False):
        self.name = name
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is on now")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is off now")

class SmartLight(Device):
    def __init__(self, name, brightness=100, is_on=False):
        super().__init__(name, is_on)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = level
        print(f"Brightness of {self.name} set to {level}")

bathroom_lamp = Device('Bathroom Lamp')
livingroom_lamp = SmartLight('Livingroom Lamp')
garage_light = SmartLight('Garage Light')

home_devices = [bathroom_lamp, livingroom_lamp, garage_light]

for light in home_devices:
    light.turn_on()

    if isinstance(light, SmartLight):
        light.set_brightness(50)

#----------------
# Exercise 5: Simple Grade Calculator
# 1. Define a function 'check_grades()' that accepts a dictionary of student names and scores.
# 2. Iterate through the dictionary and print if each student passed (>= 50) or failed (< 50).
# 3. Call the function with a sample dictionary to test the logic.

students = {
    "John": 85,
    "Anna": 45,
    "Kevin": 100
            }
def check_grades(people_data):
    for person in people_data:
        if people_data[person] >= 50:
            print(f"{person} passed!")
        else:
            print(f"{person} failed")

check_grades(students)

#----------------
# Task 6: Employee Search
# 1. Create a nested dictionary of employees with ID, name, and department.
# 2. Implement a function to filter employees by department name.
# 3. Return a list of names and print it to verify the logic.

employees = {
    1: {'name': 'Tom Conor', 'department': 'Sales'},
    2: {'name': 'Tim Mona', 'department': 'IT'}
}

def get_dept_members(dept_name):
    list_names = []
    for v in employees.values():
        if v['department'] == dept_name:
            list_names.append(v['name'])

    return list_names

print(get_dept_members('IT'))

#----------------
# Task 7: Sandwich Toppings
# 1. Define a function 'make_sandwich()' that uses *args to accept any number of toppings.
# 2. Print a summary of the order by iterating through the toppings.
# 3. Test the function with multiple calls containing different amounts of arguments.

def make_sandwich(*args):
    print("Your sandwich contains: ")
    for topping in args:
        print(topping)

sandwich_student = make_sandwich('bread')
sandwich_tomato = make_sandwich('bread', 'tomato')
sandwich_vegetables = make_sandwich('bread', 'tomato', 'avocado', 'olive')

#----------------
# Task 8: Filter and Square
# 1. Start with a list of numbers from 1 to 10.
# 2. Use a list comprehension to find even numbers and calculate their squares.
# 3. Store the result in a new list and print it.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number ** 2 for number in numbers if number % 2 ==0]

print(squares)

#----------------
# Task 9: User Profile Builder
# 1. Define 'build_profile()' using mandatory arguments and **kwargs.
# 2. Build and return a dictionary containing all provided user information.
# 3. Test with various keyword arguments and print the final profile.

def build_profile(first_name, last_name, **kwargs):
    user_info = {}
    user_info['First name'] = first_name
    user_info['Last name'] = last_name

    for k, v in kwargs.items():
        user_info[k] = v

    return user_info

robert = build_profile('Robert', 'Lewandowski', Age=40)
print(robert)

#----------------
# Task 10: Task Mover
# 1. Start with a list of 'todo' tasks and an empty list of 'finished' tasks.
# 2. Use a 'while' loop to move tasks from 'todo' to 'finished' using pop() and append().
# 3. Print the status of both lists after the process is complete.

todo_tasks = ['email client', 'buy milk', 'code python']
finished_tasks = []

while todo_tasks:
    current_task = todo_tasks.pop()
    print(f"Finished task: {current_task}")
    finished_tasks.append(current_task)

print(f"todo_tasks: {todo_tasks}")
print(f"finished_tasks: {finished_tasks}")

#----------------
# Task 11: Voting Poll
# 1. Create an empty dictionary to store names and favorite programming languages.
# 2. Use a while loop to collect user data via input().
# 3. Include a way for the user to quit the loop (using a flag or break).
# 4. Print the final dictionary of responses.

responses = {}

while True:
    user_name = input("Enter your name: ")
    user_language = input("Enter your favorite programming language: ")
    responses[user_name] = user_language

    flag = input("Does anyone else want to answer: ")
    if flag != 'yes':
        break

print("Thank you for participating in the survey!")
print("Results:")
for k, v in responses.items():
    print(f"{k.title()} likes: {v.title()}")

#----------------
# Task 12: Bank Account Manager
# 1. Create a BankAccount class with an owner and a balance starting at 0.
# 2. Implement deposit(amount) and withdraw(amount) methods.
# 3. Add logic to withdraw() to prevent overdrafts.
# 4. Test transactions and print the balance after each step.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}$. New balance: {self.balance}$")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}$. New balance: {self.balance}$")

tom = BankAccount("Tom Holland", 1000)
tom.deposit(100)
tom.withdraw(100)
tom.withdraw(20000)

#----------------
# Task 13: Smart Shopping Cart
# 1. Use a dictionary to store items and their quantities.
# 2. Define add_item() to handle both new and existing items (incrementing quantity).
# 3. Define show_cart() to neatly display the current contents.
# 4. Test by adding the same item multiple times.

cart = {}

def add_item(cart, item_name, quantity):
    if item_name in cart:
        cart[item_name] += quantity
    else:
        cart[item_name] = quantity

def show_cart(cart):
    for k, v in cart.items():
        print(f"{k} : {v} quantity")

add_item(cart, 'butter', 10)
add_item(cart, 'butter', 1)

show_cart(cart)

#----------------
# Task 14: The Uncrashable Calculator (Try-Except)
# 1. Ask the user for two numbers and perform division.
# 2. Use try-except to handle ZeroDivisionError and ValueError.
# 3. Use a while loop with an else block to ensure the program only exits on successful calculation.

while True:
    try:
        a_number = float(input("Enter first number: "))
        b_number = float(input("Enter second number: "))
        print(a_number/b_number)
        break
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Please enter valid numbers!")

#----------------
# Task 15: Advanced Gradebook (Classes & Exceptions)
# 1. Create a Student class with a list for grades.
# 2. Implement add_grade() with error handling for non-numeric inputs.
# 3. Implement get_average() with ZeroDivisionError handling for empty lists.
# 4. Test both error scenarios to ensure the program remains stable.

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        if grades == None:
            self.grades = []
        else:
            self.grades = grades

    def add_grade(self, grade):
        try:
            value = float(grade)
            self.grades.append(value)
        except ValueError:
            print("Error: Grade must be a number!")

    def get_average(self):
        try:
            print(sum(self.grades)/len(self.grades))
        except ZeroDivisionError:
            print("No grades to calculate average")

mati = Student('Matheo')
mati.add_grade(5)
mati.add_grade(3)
mati.get_average()

ana = Student('Ana')
ana.add_grade('k')
ana.get_average()

#----------------
# Task 16: Safe Dictionary Access (KeyError Handling)
# 1. Start with a predefined price dictionary.
# 2. Use try-except to handle KeyError when a user looks up a non-existent item.
# 3. Implement a loop to allow multiple lookups until a 'quit' command is given.

prices = {
    "apple": 2.5,
    "banana": 3.0,
    "orange": 4.5
}

def get_item_price(shop_dict):
    while True:
        item_name = input("Enter the item name: ")

        if item_name == 'quit':
            break

        try:
            price = shop_dict[item_name]
        except KeyError:
            print("Sorry, this item is not in our database")
        else:
            print(f"Price: {price}")

get_item_price(prices)

#----------------
# Task 17: Secure List Access (IndexError)
# 1. Access list elements by user-provided index.
# 2. Handle ValueError for non-integer inputs.
# 3. Handle IndexError for out-of-bounds access.

top_players = ["Mati", "Ana", "Tom"]

while True:
    try:
        number_player = int(input("Enter player number: "))
        print(top_players[number_player])
        break
    except ValueError:
        print("you have to enter a number")
    except IndexError:
        print(f"we have only {len(top_players)} players")

#----------------
# Task 18: Multi-Exception Handling
# 1. Create a function that accesses a list, converts the value, and performs division.
# 2. Handle IndexError, ValueError, and ZeroDivisionError in one block.
# 3. Test with inconsistent data to ensure robustness.

my_data = ["10", "0", "abc"]

def process_data(data_list, index):
    try:
        value = int(data_list[index])
        value = 100/value
        return value
    except IndexError:
        return "IE"
    except ValueError:
        return "VE"
    except ZeroDivisionError:
        return "ZDE"

print(process_data(my_data, 0))
print(process_data(my_data, 1))
print(process_data(my_data, 2))

#----------------
# Task 19: The Resilient Loop
# 1. Iterate through a list containing both valid numbers and invalid strings/zeros.
# 2. Use try-except inside the loop to handle individual errors.
# 3. Ensure that one faulty item doesn't crash the entire processing of the list.

data = ["100", "200", "three hundred", "400", "0", "500"]

for value in data:
    try:
        print(f"1000 : {value} = {1000/int(value)}")
    except ValueError:
        print(f"{value} - isn't a number")
    except ZeroDivisionError:
        print(f"{value} - don't division by zero")

#----------------
# Task 20: Dictionary Search with Finally
# 1. Create a function to fetch values from a dictionary using try-except.
# 2. Handle KeyError if the requested key is missing.
# 3. Use the 'finally' block to execute code regardless of the search outcome.

scores = {"Poland": 3, "Germany": 1, "France": 2}

def get_score(country):
    try:
        country_score = scores[country]
        return country_score
    except KeyError:
        return f"Error: No data for country {country}"
    finally:
        print("Search attempt finished")

print(get_score('Pooland'))
print(get_score('Poland'))

#----------------
# Task 21: Flight Booking System
# 1. Create a Flight class with a specific capacity.
# 2. Implement add_passenger() with a check for available seats.
# 3. Use try-except logic to handle attempts to book a seat on a full flight.

class Flight:
    def __init__(self, flight_number, capacity):
        self.flight_number = flight_number
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) >= self.capacity:
            raise Exception(f"Flight is full! Cannot add {name}")

        self.passengers.append(name)
        print(f"{name} was added to flight passengers")

ryinar = Flight(1, 1)

potential_passengers = ['Philip', 'Thomas']

for person in potential_passengers:
    try:
        ryinar.add_passenger(person)
    except Exception as e:
        print(f"Error occurred: {e}")

#----------------
# Task 22: Secure Data Converter
# 1. Iterate through a dictionary with mixed string values.
# 2. Use try-except to attempt conversion to float.
# 3. Skip invalid data points and collect valid ones in a new dictionary.

raw_data = {
    "temp": "25.5",
    "humidity": "none",
    "pressure": "1013"
}

clean_data = {}

for key, data in raw_data.items():
    try:
        clean_data[key] = float(data)
    except ValueError:
        print(f"Skipped invalid record: {key}")

print(clean_data)
