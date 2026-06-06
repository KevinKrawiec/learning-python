# 1. Write a function that returns the second largest number in a list.
numbers = [1, 2, 4, 5, 6, 12, 21, 100]

def second_bigger(list_numbers):
    list_numbers = sorted(list_numbers)
    return list_numbers[-2]

print(second_bigger(numbers))

# 2. Remove all duplicates from a list, keeping the order of first occurrences.
names = ["Alice", "Tom", "Alice", "John", "Tom", "Josh", "Alice"]
names_without_duplicates = []

for name in names:
    if name not in names_without_duplicates:
        names_without_duplicates.append(name)

print(names_without_duplicates)

# 3. Given a list of numbers, return a new list containing only those divisible by 3 and greater than 10.
numbers = [1, 2, 4, 5, 6, 12, 21, 100]
new_numbers = []

for number in numbers:
    if number > 10 and number % 3 == 0:
        new_numbers.append(number)

print(new_numbers)

# 4. Flatten a nested list, e.g. [[1,2],[3,4],[5]] -> [1,2,3,4,5].
list_of_numbers = [[1,2],[3,4],[5]]
fixed_list_of_numbers = [item for sublist in list_of_numbers for item in sublist]
print(fixed_list_of_numbers)

# 5. Split a list into two: even numbers and odd numbers.
numbers = [1, 2, 4, 5, 6, 12, 21, 100]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(f"even_numbers = {even_numbers}")
print(f"odd_numbers = {odd_numbers}")

# 6. Given a list of (name, age) tuples, sort it by age in descending order.
list_of_tuples = [
    ("John", 30),
    ("Alice", 18),
    ("Josh", 72),
    ("Kevin", 22)
]

sort_age_asc_list_of_tuples = sorted(list_of_tuples, key=lambda person: person[1], reverse=True)
print(sort_age_asc_list_of_tuples)

# 7. Unpack a tuple (1, 2, 3) into three separate variables.
t = (1, 2, 3)
a, b, c = t
print(a, b, c)

# 8. Write a function that accepts any number of arguments (*args) and returns a tuple (min, max, sum).
def minimum_maximum_sum(*args):
    return min(args), max(args), sum(args)

print(minimum_maximum_sum(5, 6, 7))

# 9. From a list of tuples [(1,'a'), (2,'b'), (3,'c')], create two separate lists: [1,2,3] and ['a','b','c'].
t_list = [(1,'a'), (2,'b'), (3,'c')]
numbers = [pair[0] for pair in t_list]
letters = [pair[1] for pair in t_list]

print(numbers, letters)

# 10. Count how many times each word appears in a sentence and return a dictionary.
dict_word = {}
sentence = ("The study notes that the deer consumed by the python in the clip was 66.9% of the snake's mass. "
            "Summer is the best time of year to see a Burmese python. "
            "The pythons do try to make the most of their abilities though."
            " Since that time, more than 2,500 pythons have been killed by hunters.")

words = sentence.split()

for word in words:
    if word not in dict_word:
        dict_word[word] = 1
    else:
        dict_word[word] += 1

print(dict_word)

# 11. Reverse a dictionary - swap keys with values ({'a':1} -> {1:'a'}).
# I used dict for the last exercise (dict_word)
reverse_dict_word = {}

for key, value in dict_word.items():
    if value not in reverse_dict_word:
        reverse_dict_word[value] = [key]
    else:
        reverse_dict_word[value].append(key)

print(reverse_dict_word)

# 12. Given two dictionaries, merge them into one; for shared keys, sum the values.
first_dict = {1: "a", 2: "b", 3: "c"}
second_dict = {3: "c", 4: "d", 5: "f"}

one_dict = {}

for key, value in first_dict.items():
    one_dict[key] = value

for key, value in second_dict.items():
    if key in one_dict:
        one_dict[key] += value
    else:
        one_dict[key] = value

print(one_dict)

# 13. Find the key with the largest value in a dictionary.
the_biggest_key = max(one_dict, key=one_dict.get)
print(the_biggest_key)

# 14. Given a grades dictionary {'Ania': 5, 'Bartek': 3, 'Celina': 4}, return a list of names of people with a grade >= 4.
grades = {'Ania': 5, 'Bartek': 3, 'Celina': 4}
names = []

for k, v in grades.items():
    if v >= 4:
        names.append(k)

print(f"Students with a grade 4 or higher: {names}")

# 15. Write a function that checks whether a word is a palindrome.
def if_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(if_palindrome("cat"))
print(if_palindrome("tat"))

# 16. Write a function that calculates a factorial (using a loop, not recursion).
def factorial(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result

print(factorial(5))

# 17. Write a function with a default argument: it calculates the area of a rectangle, but if only one side is given, treat it as a square.
def field(a, b=None):
    if b is None:
        return a*a
    else:
        return a*b

print(field(2))
print(field(4, 5))

# 18. Write a function that takes a function as an argument and applies it to each element of a list (your own equivalent of map).
def my_map(func, items):
    result = []
    for item in items:
        result.append(func(item))

    return result
