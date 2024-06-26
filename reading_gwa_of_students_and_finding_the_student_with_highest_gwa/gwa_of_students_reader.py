# Pseudocode

# 1. Create a text file with students' name and GWA

# 2. Create an empty list of student data, read student data from the text file, split the name and GWA, and set 1.00 as highest and 5.00 as lowest GWA
student_data = []

with open("reading_gwa_of_students_and_finding_the_student_with_highest_gwa/student_data.txt", "r") as file:
    for line in file:
        name, gwa = line.strip().split(',')
        gwa = 1.00 - (float(gwa) - 5.00)
        student_data.append((name, gwa))

# 3. Initialize highest student name and GWA as None and 0 and find the student with highest GWA
highest_gwa = 0
student_name_with_highest_gwa = None

for name, gwa in student_data:
    if gwa > highest_gwa:
       highest_gwa = gwa
       student_name_with_highest_gwa = (name, 5.00 - gwa + 1.00) 

# 4. Print the student with the highest GWA
print(f"The student with the highest GWA is {student_name_with_highest_gwa[0]} with a GWA of {student_name_with_highest_gwa[1]:.2f}")