########### Problem 1

# You are a librarian, and you need to perform various
# operations on the list of books.

# Initialize the Library.
library = []

# Add the books "Harry Potter", "1984", "The Great Gatsby", "Animal Farm", "Dracula" to the collection.
library.extend(["Harry Potter", "1984", "The Great Gatsby", "Animal Farm", "Dracula"])

# Remove "Harry Potter" from the collection.
library.remove("Harry Potter")

# Sort the books alphabetically.
library.sort()

# Check if "Harry Potter" is in the library.
"Harry Potter" in library

# Check if "Romeo and Juliet" is in the collection.
"Romeo and Juliet" in library

# Count the total number of books.
len(library)

# Insert "Alice in Wonderland" at the appropriate position.
library.insert(1, "Alice in Wonderland")

# Remove and return the last (alphabetically) book.
last_book = library.pop()

# Find the index of "1984".
library.index("1984")

# Add "Wuthering Heights" to the back of the list.
library.append("Wuthering Heights")

# Create a new library, excluding the first book of the current one.
new_library_1 = library[1:]

# Create a new library, including only second and the third book of the current one.
new_library_2 = library[1:3]

# Reverse the order of the books.
library.reverse()

# Remove all books from the collection.
library.clear()



########### Problem 2

# Use a lambda function with map to square each number in the list.
# Expected output: numbers = [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))


# Use a lambda function to add corresponding elements from the two lists.
# Expected output: [5, 7, 9]
my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]

added_lists = list(map(lambda x, y: x + y, my_list_1, my_list_2))

# Use a lambda function with map to calculate the length of each string.
# Expected output: [6, 5, 10]
list_of_strings = ["banana", "apple", "strawberry"]

lengths = list(map(lambda s: len(s), list_of_strings))


########### Problem 3

# Create a tuple with the the fellowing fruits: "banana", "apple", "strawberry", "cherry"
fruits = ("banana", "apple", "strawberry", "cherry")

# Print the name of the second fruit in the tuple.
print(fruits[1])

# Count how many times "apple" appears in the tuple.
fruits.count("apple")

# Find the index of "banana" in the tuple.
fruits.index("banana")

# Create a new tuple containing the first three fruits.
three_fruits = fruits[:3]

########### Problem 4

# Create a dictionary with student names and grades: 'Alice': 85, 'Bob': 92, 'Charlie': 78
students = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Print Bob's grade
print(students['Bob'])

# Add a new student Sam and her grade 91
students['Sam'] = 91

# Remove 'Alice' from the class
del students['Alice']

# Check if there is a student named 'Charlie'
'Charlie' in students

# Print a list of all student names
print(list(students.keys()))

# Print a list of all grades
print(list(students.values()))

# Add 2 new students - Alex and Rob, and their grades - 93 and 76
students.update({'Alex': 93, 'Rob': 76})


########### Problem 5

# Create a set with the movies "Inception", "The Matrix", "Interstellar", "The Dark Knight"
movies = {"Inception", "The Matrix", "Interstellar", "The Dark Knight"}

# Add the movie "Avatar" movie to the set
movies.add("Avatar")

# Remove "Interstellar" from the set
movies.remove("Interstellar")

# Check if 'Interstellar' is in the set
"Interstellar" in movies

# Create another set with a friend's favorite movies: "Inception", "The Matrix", "The Lord of the Rings"
friends_movies = {"Inception", "The Matrix", "The Lord of the Rings"}

# Print the union of the two sets
movies.union(friends_movies)

# Print the intersection of the two sets
movies.intersection(friends_movies)

# Print the difference of the two sets
movies.difference(friends_movies)


########### Example 1 - reading a text file

with open("sample_files/02_text_file.txt", "r") as file:
    # read -> the content is a string
    content = file.read()
    print(content)

with open("sample_files/02_text_file.txt", "r") as file:
    # the content is a list of all the lines of the file
    content = file.readlines()
    print(content)

with open("sample_files/02_text_file.txt", "r") as file:
    # the content is the first unread line of the file
    content = file.readline()
    print(content)


########### Example 2 - writing to a text file

with open("sample_files/02_example_write.txt", "w") as file:
    file.write("Hello, World! ")

with open("sample_files/02_example_write.txt", "a") as file:
    file.write("My name is Alice")


########### Example 3 - reading a CSV file

import csv

with open("sample_files/02_customers-100.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


########### Example 4 - writing to a CSV file

with open("sample_files/02_example_write.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Jazmine", 30, "New York"])


########### Problem 5

from my_awesome_package import my_special_math

# Print the result of the 'special addition' of 2 and 3
print(my_special_math.special_addition(2, 3))

# Print the result of the 'special multiplication' of 2 and 3
print(my_special_math.special_multiplication(2, 3))


########### Problem 6

# Display a prompt for the user to enter their age
age = input("Enter your age:")

# Print the age of the user after 5 years
print(int(age) + 5)


########### Example 5 - using the os module

import os

# Print the path of the current working directory (CWD)
print(os.getcwd())

# Change the CWD
os.chdir("sample_files")
print(os.getcwd())

# List all the file names in the CWD
print(os.listdir(os.getcwd()))
