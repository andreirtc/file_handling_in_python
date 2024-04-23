# Pseudocode

# 1. Create a text file named "numbers.txt" that contains 20 integers

# 2. Read the text file and convert the content as integer
with open("extracting_even_and_odd_numbers_from_a_text_file/numbers.txt", "r") as file:
    numbers = [int(num.strip()) for num in file.readlines()]

# 3. Check the content if even or odd number
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# 4. Extract the even numbers from the text file and name it "even.txt"
with open("even.txt", "w") as even_file:
    for num in even_numbers:
        even_file.write(str(num) + "\n")

# 5. Extract the odd numbers from the text file and name it "odd.txt"
with open("odd.txt", "w") as odd_file:
    for num in odd_numbers:
        odd_file.write(str(num) + "\n")