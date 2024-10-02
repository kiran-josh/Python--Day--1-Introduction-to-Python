"""
Name: Kiran G
Program: Create a pyramid of numbers from 1 to 20 using for loop.

"""

# Initialize the starting number
num = 1

# Loop to create the pyramid
for i in range(1, 7):
    # Print leading spaces for alignment
    print(' ' * (5 - i), end='')
    
    # Print the numbers in the current row
    for j in range(i):
        if num <= 20:
            print(num, end=' ')
            num += 1
    
    # Move to the next line after each row
    print()
