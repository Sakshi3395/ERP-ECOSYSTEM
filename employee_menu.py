from employee import Employee, Manager
from utils import confirm_action
from file_manager import read_data_from_employee, save_employee_data

employees = read_data_from_employee()

def employee_menu():
    while True:
        print("\n=== EMPLOYEE MANAGEMENT ===")
        print("1. Add Employee\n2. View Employees\n3. Update Salary\n4. Delete Employee\n5. Back")
        choice = input("Select: ").strip()

        if choice == "1":
            name = input("Name: ")
            role = input("Role (Staff/Manager): ").lower()
            sal = float(input("Salary: "))
            eid = f"E{100 + len(employees) + 1}"
            if role == "manager":
                bonus = float(input("Bonus: "))
                employees[eid] = Manager(eid, name, role, sal, bonus)
            else:
                employees[eid] = Employee(eid, name, role, sal)
            save_employee_data(employees)
            print(f"✔ Added {eid}")
        elif choice == "2":
            for e in employees.values(): print(e)
        elif choice == "3":
            eid = input("ID: ")
            if eid in employees:
                employees[eid].salary = float(input("New Salary: "))
                save_employee_data(employees)
                print("✔ Updated")
        elif choice == "4":
            eid = input("ID: ")
            if eid in employees and confirm_action("Delete? "):
                del employees[eid]
                save_employee_data(employees)
                print("✔ Deleted")
        elif choice == "5": break