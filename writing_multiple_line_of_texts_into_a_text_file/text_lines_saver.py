# Pseudocode

# 1. Create a text file named "my_life.txt" using 'write' in python.
with open("writing_multiple_line_of_texts_into_a_text_file/my_life.txt", "w") as file:
# 2. Use while loop to ask the user repeatedly about the lines to enter and break if the user entered 'n'
    while True:
        line = input("Enter line: ")
        file.write(line + '\n')
        more_lines = input("Are there more lines y/n? ").strip().lower()
        if more_lines != 'y':
            break
# 3. Display a text indicating the texts inputted was written to 'my_life.txt' successfully
print("\nTexts written to 'my_life.txt' successfully.")