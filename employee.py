class Employee:
    def __init__(self, emp_id, name, role, salary):
        self.emp_id = emp_id
        self.name = name
        self.role = role
        self.salary = salary
        self.assets = []

    def __str__(self):
        asset_list = ", ".join(a.name for a in self.assets) if self.assets else "None"
        return (
            f"ID: {self.emp_id} | Name: {self.name} | "
            f"Role: {self.role} | Salary: ₹{self.salary}\n"
            f"Assigned Assets: {asset_list}"
        )