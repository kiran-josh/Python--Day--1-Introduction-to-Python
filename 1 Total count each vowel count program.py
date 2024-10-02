"""
Name: Kiran G
Program:Write a python program to calculate the total number of vowels and count of each individual vowel A,E,I,O,U in the string "Guvi Geeks Network Private Limited"?

"""

# Define the input string
input_string = "Guvi Geeks Network Private Limited"

# casefold() coverts the whole string into lower case
input_string = input_string.casefold()

# Define the vowels
vowels = "aeiou"

#Initialize a dictionary to store the count of each vowel
eachvowelcount = {}.fromkeys(vowels,0)

# Initialize a variable to store the total number of vowels
totalvowelcount = 0

# Iterate over each character in the string
for char in input_string:
    if char in vowels:
        eachvowelcount[char] +=1
        totalvowelcount = totalvowelcount + 1

  # Print the total number of vowels      
print("Total vowels count : ", totalvowelcount)

# Print the count of each vowel
print("Each vowel count", eachvowelcount)