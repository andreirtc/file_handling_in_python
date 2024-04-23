# Pseudocode

# 1. Create a text file named "integers.txt" that contains 20 integers

# 2. Read integers from the text file and convert them as integers
with open("finding_the_squares_and_cubes_of_integers_inside_a_text_file/integers.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]

# 3. Square even integers and cube odd integers
# 4. Create the file for the square of even integers and name it 'double.txt'
# 5. Create the file for the cube of odd integers and name it 'triple.txt'