"""
Name: Kiran G
Program: Write a program that takes a string and returns the number of unique characters in it.

"""


# Get input from the user
input_string = input("Enter a string: ")

# Use a set to find unique characters
unique_characters = set(input_string)

# Count the number of unique characters
unique_num_count = len(unique_characters)

# Print the result
print("Number of unique characters:", unique_num_count)
