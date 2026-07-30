students = [
    {"name": "Amit", "marks": 92},
    {"name": "Riya", "marks": 78},
    {"name": "Karan", "marks": 35},
    {"name": "Neha", "marks": 65},
    {"name": "Stop", "marks": 0}
]

for student in students:

    if student["name"] == "Stop":
        break

    marks = student["marks"]

    if marks < 40:
        print(student["name"], "- Failed")
        continue

    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    else:
        grade = "C"

    if grade == "A+":
        print(student["name"], "- Excellent")
    else:
        pass

    print(student["name"], "- Grade:", grade)