# write_employee.py

file = open("employees.txt", "w")

employee_id = input("Enter Employee ID: ")
employee_name = input("Enter Employee Name: ")
department = input("Enter Department: ")

file.write("Employee ID: " + employee_id + "\n")
file.write("Employee Name: " + employee_name + "\n")
file.write("Department: " + department + "\n")

file.close()

print("Employee information saved successfully.")