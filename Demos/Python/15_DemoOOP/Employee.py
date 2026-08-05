class Employee:
    
    # Class Attribute
    company = "Microsoft"
    
    # Constructor
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    
    # Instance Method
    def display_details(self):
        print(f"Employee ID : {self.emp_id}")
        print(f"Employee Name : {self.name}")
        print(f"Salary : {self.salary}")
    
    # Instance Method
    def increment_salary(self, amount):
        self.salary = self.salary + amount
        print(f"Updated Salary : {self.salary}")

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static Method
    @staticmethod
    def company_policy():
        print("All employees must follow company policies.")