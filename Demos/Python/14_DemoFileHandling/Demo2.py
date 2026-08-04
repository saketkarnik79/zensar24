# read_employee.py

file = open("employees.txt", "r")

content = file.read()

print("\nEmployee Information")
print("--------------------")
print(content)

file.close()