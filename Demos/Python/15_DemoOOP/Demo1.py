import Employee;

emp1 = Employee.Employee(1, "John Doe", 50000); # Object Creation with Constructor
emp1.display_details(); # Calling Instance Method
emp1.increment_salary(5000); # Calling Instance Method to increment salary
print(f"Company Name : {Employee.Employee.company}"); # Accessing Class Attribute
print("Calling Static Method to display company policy:");
Employee.Employee.company_policy(); # Calling Static Method

emp2 = Employee.Employee(2, "Jane Smith", 60000); # Object Creation with Constructor
emp2.display_details(); # Calling Instance Method
emp2.increment_salary(7000); # Calling Instance Method to increment salary
print(f"Company Name : {Employee.Employee.company}"); # Accessing Class Attribute
print("Calling Static Method to display company policy:");
Employee.Employee.company_policy(); # Calling Static Method

# Calling Class Method to change company name
Employee.Employee.change_company("Google");
print(f"Updated Company Name : {Employee.Employee.company}"); # Accessing Class Attribute after change

