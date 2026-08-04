import csv

file = open("employees.csv", "r")

reader = csv.DictReader(file)

for employee in reader:

    print("\nEmployee Information")

    print(
        "ID:",
        employee["EmployeeID"]
    )

    print(
        "Name:",
        employee["Name"]
    )

    print(
        "Department:",
        employee["Department"]
    )

    print(
        "Salary:",
        employee["Salary"]
    )

file.close()