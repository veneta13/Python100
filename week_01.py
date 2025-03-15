# Variables

my_name = "John Doe"       # string
my_age = 27                # integer
price_of_chocolate = 3.20  # float
has_cat = True             # boolean

print(type(my_age))

my_age_as_string = str(my_age)

print(type(my_age_as_string))

# Implicit conversion
6 + 1.3

# Explicit conversion
int(1.1) + 2


# Operators

print(5 + 3)
print(5 / 3)
print(5 // 3) 
print(5 % 3) # remainder

print(2 ** 3) # the same as 2 * 2 * 2

print(3 <= 5)

print(True and False)
print(True or False)
print(not True)

print(not None)
print(True and None)

price_of_chocolate = 3.20
print(price_of_chocolate + 3)

# print(5 + "waffles")

print("5 " + "waffles")

x = [5]
y = x
print(x is y)

a = [5]
b = [5]
print(a is b)

print(None is None)
print(False is None)


# Block structure

def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")


# Conditional statements

x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")


# Loops

fruits = ["apples", "lemons", "pineapples"]

for fruit in fruits:
    print("I have some " + fruit)

for my_number in range(3):
    print(f"my number is {my_number}")

for my_number in range(1, 4):
    print(f"my number is {my_number}")

for my_number in range(-5, 15, 5):
    print(f"my number is {my_number}")

countdown_seconds = 5
while countdown_seconds > 0:
    countdown_seconds -= 1    # no countdown_seconds-- in Python!
    print(countdown_seconds, " seconds left")

positive_number = 5
while True:
    positive_number -= 1
    if positive_number < 1:
        break
    print(positive_number)

odd_number = 0
while odd_number < 10:
    odd_number += 1
    if odd_number % 2 == 0:
        continue
    print(odd_number)

vegetables = ["tomatoes", "onions", "potatoes"]
for vegetable in vegetables:
    if vegetable == "onions":
        continue
    print("I have some " + vegetable)


# Functions

def greet(user):
    print(f"Hello, {user}!")
    print("Nice to meet you!")
greet("Alice")

def ask_question(user):
    return f"How are you {user}?"
print(ask_question("Alice"))

def speak_about_pets(cat_count=2):
    return "I have " + str(cat_count) + " cats!"
print(speak_about_pets())
print(speak_about_pets(3))

def introduce_yourself_args(*args):
    introduction = "My name is "
    for name in args:
        introduction += name + " "
    return introduction
print(introduce_yourself_args("John", "Stephen", "Doe"))

def introduce_yourself_kwargs(**kwargs):
    introduction = "My name is " + kwargs["first_name"] + " " + kwargs["last_name"]
    return introduction
print(introduce_yourself_kwargs(first_name="John", middle_name="Stephen", last_name="Doe"))


# Scope

my_favorite_number = 7

def set_to_5():
    my_favorite_number = 5

set_to_5()
print(my_favorite_number)

def set_to_3(my_favorite_number):
    my_favorite_number = 3

set_to_3(my_favorite_number)
print(my_favorite_number)


# Exceptions

try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Exiting.")

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return True

try:
    check_age(16)
except ValueError as e:
    print(e)


# Debugging 

import logging # we put imports at the top of the file
logging.basicConfig(level=logging.DEBUG)

def multiply(a, b):
    logging.debug(f"Multiplying {a} and {b}")
    result = a * b
    logging.info(f"Result is: {result}")
    return result

multiply(3, 5)


# Strings

s = "hello"
# s[0] = "H"  # Raises an error

print("Hi " * 3)

print("Hello".upper())
print("Hello".lower())
print("    Hello  ".strip())

print(len("hello"))

print("hello world".split())
print(" ".join(["hello", "world"]))

print(s[1:4])
print(s[0])
print(s[::2])

print("he" in "hey")
print("ha" in "hey")
