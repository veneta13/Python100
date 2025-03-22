########### Problem 1

# You are a librarian, and you need to perform various
# operations on the list of books.

# Initialize the Library: Start with an empty list of books.

# Add the books "Harry Potter", "1984", "The Great Gatsby", "Animal Farm", "Dracula" to the collection.

# Remove "Harry Potter" from the collection.

# Sort the books alphabetically.

# Check if "Harry Potter" is in the library.

# Check if "Romeo and Juliet" is in the collection.

# Count the total number of books.

# Insert "Alice in Wonderland" at the appropriate position.

# Remove and return the last (alphabetically) book.

# Find the index of "1984".

# Add "Wuthering Heights" to the back of the list.

# Create a new library, excluding the first book of the current one.

# Create a new library, including only second and the third book of the current one.

# Reverse the order of the books.

# Remove all books from the collection.


########### Problem 2

# Use a lambda function with map to square each number in the list.
# Expected output: numbers = [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]


# Use a lambda function to add corresponding elements from the two lists.
# Expected output: [5, 7, 9]
my_list_1 = [1, 2, 3]
my_list_2 = [4, 5, 6]

# Use a lambda function with map to calculate the length of each string.
# Expected output: [6, 5, 10]
list_of_strings = ["banana", "apple", "strawberry"]


########### Problem 3

# Create a tuple with the the fellowing fruits: "banana", "apple", "strawberry", "cherry"

# Print the name of the second fruit in the tuple.

# Count how many times "apple" appears in the tuple.

# Find the index of "banana" in the tuple.

# Create a new tuple containing the first three fruits.


########### Problem 4

# Create a dictionary with student names and grades: 'Alice': 85, 'Bob': 92, 'Charlie': 78

# Print Bob's grade

# Add a new student Sam and her grade 91

# Remove 'Alice' from the class

# Check if there is a student named 'Charlie'

# Print a list of all student names

# Print a list of all grades

# Add 2 new students - Alex and Rob, and their grades - 93 and 76


########### Problem 5

# Create a set with the movies "Inception", "The Matrix", "Interstellar", "The Dark Knight"

# Add the movie "Avatar" movie to the set

# Remove "Interstellar" from the set

# Check if 'Interstellar' is in the set

# Create another set with a friend's favorite movies: "Inception", "The Matrix", "The Lord of the Rings"

# Print the union of the two sets

# Print the intersection of the two sets

# Print the difference of the two sets


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

# Print the result of the 'special addition' of 2 and 3

# Print the result of the 'special multiplication' of 2 and 3


########### Problem 6

# Display a prompt for the user to enter their age

# Print the age of the user after 5 years


########### Example 5 - using the os module

import os

# Print the path of the current working directory (CWD)
print(os.getcwd())

# Change the CWD
os.chdir("sample_files")
print(os.getcwd())

# List all the file names in the CWD
print(os.listdir(os.getcwd()))
