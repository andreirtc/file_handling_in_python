# Pseudocode

# 1. Create a text file named "integers.txt" that contains 20 integers

# 2. Read integers from the text file and convert them as integers
with open("finding_the_squares_and_cubes_of_integers_inside_a_text_file/integers.txt", "r") as file:
    numbers = [int(num) for num in file.read().split()]

# 3. Square even integers and cube odd integers
even_numbers = [num ** 2 for num in numbers if num % 2 == 0]
odd_numbers = [num ** 3 for num in numbers if num % 2 != 0]

# 4. Create the file for the square of even integers and name it 'double.txt'
with open("finding_the_squares_and_cubes_of_integers_inside_a_text_file/double.txt", "w") as double_file:
    for num in even_numbers:
        double_file.write(str(num) + "\n")

# 5. Create the file for the cube of odd integers and name it 'triple.txt'
with open("finding_the_squares_and_cubes_of_integers_inside_a_text_file/triple.txt", "w") as triple_file:
    for num in odd_numbers:
        triple_file.write(str(num) + "\n")