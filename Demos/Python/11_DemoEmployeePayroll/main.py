# main.py

import payroll_module as pm

print("=================================")
print("EMPLOYEE PAYROLL MANAGEMENT")
print("=================================")

# Global Scope Function
pm.display_company()

# User Input

emp_id = int(input("\nEnter Employee ID: "))
name = input("Enter Employee Name: ")
department = input("Enter Department: ")

basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
bonus = float(input("Enter Bonus: "))

# Positional Arguments
pm.employee_details(
    emp_id,
    name,
    department
)

# Function with Parameters and Return Value

gross_salary = pm.calculate_salary(
    basic_salary,
    hra,
    bonus
)

print("\nGross Salary =", gross_salary)

# Default Argument Demo

tax = pm.calculate_tax(gross_salary)

print("Tax (Default 10%) =", tax)

# Keyword Argument Demo

pm.employee_details(
    emp_id=emp_id,
    name=name,
    department=department
)

# Variable-Length Arguments Demo

num_allowances = int(
    input(
        "\nEnter Number of Extra Allowances: "
    )
)

allowance_values = []

for i in range(num_allowances):
    amount = float(
        input(f"Allowance {i+1}: ")
    )

    allowance_values.append(amount)

extra_total = pm.add_allowances(
    *allowance_values
)

print("\nTotal Allowances =", extra_total)

# Net Salary

net_salary = gross_salary + extra_total - tax

print("Net Salary =", net_salary)

# Lambda Function Demo

grade = pm.salary_grade(net_salary)

print("Salary Grade =", grade)

# Variable-Length Keyword Arguments

pm.display_additional_info(
    Email="employee@company.com",
    Location="Pune",
    Experience="5 Years",
    EmploymentType="Full Time"
)

# Local Scope Demo

pm.local_scope()

print("\nProgram Completed Successfully")