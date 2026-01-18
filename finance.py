from file_manager import save_finance
from employee_menu import employees
from asset_menu import assets
from utils import confirm_action

def finance_menu():
    while True:
        print("\n=== FINANCE MANAGEMENT ===")
        print("1. Total Salary Expenditure")
        print("2. Total Asset Value")
        print("3. Asset Depreciation Report")
        print("4. Employee-wise Asset Report")
        print("5. Back")

        choice = input("Select option: ")

        match choice:
            case "1":
                total_salary = sum(emp.salary for emp in employees.values())
                print(f"Total Salary Expenditure: ₹{total_salary}")

            case "2":
                total_assets = sum(asset.value for asset in assets.values())
                print(f"Total Asset Value: ₹{total_assets}")

            case "3":
                years = int(input("Enter years: "))
                print("\nAsset Depreciation Report")
                for asset in assets.values():
                    print(
                        f"{asset.name} → ₹{asset.depreciate(years):.2f}"
                    )

            case "4":
                print("\nEmployee-wise Asset Report")
                for emp in employees.values():
                    asset_names = [a.name for a in emp.assets]
                    print(
                        f"{emp.name}: {', '.join(asset_names) if asset_names else 'No Assets'}"
                    )

            case "5":
                if confirm_action("Back to main menu? (Y/N): "):
                    break

            case _:
                print("Invalid option")