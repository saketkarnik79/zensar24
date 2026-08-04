import csv

file = open(
    "students.csv",
    "r"
)

reader = csv.DictReader(file)

total_marks = 0
count = 0

for student in reader:

    total_marks += int(
        student["Marks"]
    )

    count += 1

average = total_marks / count

print("Total Students:", count)

print("Average Marks:", average)

file.close()