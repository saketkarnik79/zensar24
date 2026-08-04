import csv

file = open(
    "students.csv",
    "a",
    newline=""
)

writer = csv.writer(file)

roll_no = input("Roll Number: ")
name = input("Name: ")
marks = input("Marks: ")

writer.writerow([
    roll_no,
    name,
    marks
])

file.close()

print("Student Added Successfully")