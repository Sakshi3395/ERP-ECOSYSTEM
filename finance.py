import employee_menu
import asset_menu
from utils import confirm_action

def finance_menu():
    while True:
        print("\n=== FINANCE MANAGEMENT ===")
        print("1. Total Salary\n2. Total Asset Value\n3. Depreciation Report\n4. Back")
        choice = input("Select: ").strip()
        if choice == "1":
            total = sum(e.salary + getattr(e, 'bonus', 0) for e in employee_menu.employees.values())
            print(f"Total Expenditure: ₹{total}")
        elif choice == "2":
            total = sum(a.value for a in asset_menu.assets.values())
            print(f"Total Asset Value: ₹{total}")
        elif choice == "3":
            years = int(input("Years: "))
            for a in asset_menu.assets.values():
                print(f"{a.name} after {years}yr: ₹{a.depreciate(years):.2f}")
        elif choice == "4": break