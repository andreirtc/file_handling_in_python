# Pseudocode

# 1. Create a text file named "numbers.txt" that contains 20 integers
# 2. Read the text file
with open("numbers.txt", "r") as file:
    for num in file:
        numbers = int(num.strip())
# 3. Check if even or odd number    
# 4. Extract the even numbers from the text file and name it "even.txt"
# 5. Extract the odd numbers from the text file and name it "odd.txt"