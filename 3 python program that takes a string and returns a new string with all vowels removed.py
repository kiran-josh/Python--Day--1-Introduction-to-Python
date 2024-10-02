"""
Name: Kiran G
Program: Write a program that takes a string and returns a new string with all vowels removed.

"""



# Get input from the user
input_string = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize an empty string for the result
result = ""

# Iterate through each character in the input string
for char in input_string:
    # If the character is not a vowel, add it to the result
    if char not in vowels:
        result += char

# Print the result
print("String with vowels removed:", result)

