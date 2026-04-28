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
