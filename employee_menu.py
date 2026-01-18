from file_manager import save_employee
from employee import Employee
from utils import confirm_action

employees = {}

def employee_menu():
    while True:
        print("\n=== EMPLOYEE MANAGEMENT ===")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee Salary")
        print("4. Delete Employee")
        print("5. Back")

        choice = input("Select option: ")

        match choice:
            case "1":
                name = input("Enter Name: ")
                role = input("Enter Role (Staff/Manager): ")
                salary = float(input("Enter Salary: "))

                if confirm_action("Confirm add employee? (Y/N): "):
                    emp_id = f"E{100 + len(employees) + 1}"
                    employees[emp_id] = Employee(emp_id, name, role, salary)
                    print(f"✔ Employee added with ID {emp_id}")

            case "2":
                if not employees:
                    print("No employees found")
                for emp in employees.values():
                    print(emp)

            case "3":
                emp_id = input("Enter Employee ID: ")
                if emp_id in employees:
                    new_salary = float(input("Enter new salary: "))
                    employees[emp_id].salary = new_salary
                    print("✔ Salary updated")
                else:
                    print("Employee not found")

            case "4":
                emp_id = input("Enter Employee ID: ")
                if emp_id in employees:
                    if confirm_action("Confirm delete? (Y/N): "):
                        del employees[emp_id]
                        print("✔ Employee deleted")
                else:
                    print("Employee not found")

            case "5":
                break

            case _:
                print("Invalid choice")