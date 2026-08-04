import csv

file = open("students.csv", "w", newline="")

writer = csv.writer(file)

writer.writerow([
    "RollNo",
    "Name",
    "Marks"
])

writer.writerow([
    "101",
    "John",
    "85"
])

writer.writerow([
    "102",
    "Mary",
    "92"
])

writer.writerow([
    "103",
    "David",
    "78"
])

file.close()

print("CSV File Created Successfully")