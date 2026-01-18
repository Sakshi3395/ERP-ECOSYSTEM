class Employee:
    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary
        self.assets = []

    def __str__(self):
        asset_names = ", ".join(a.name for a in self.assets) if self.assets else "None"
        return f"ID: {self.emp_id} | Name: {self.name} | Role: {self.role} | Salary: ₹{self.salary} | Assets: {asset_names}"

class Manager(Employee):
    def __init__(self, emp_id, name, role, salary, bonus=0.0):
        super().__init__(emp_id, name, role, salary)
        self.bonus = bonus

    def __str__(self):
        asset_names = ", ".join(a.name for a in self.assets) if self.assets else "None"
        return f"ID: {self.emp_id} | Name: {self.name} | Role: Manager | Salary: ₹{self.salary} | Bonus: ₹{self.bonus} | Assets: {asset_names}"