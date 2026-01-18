from login import login
from employee_menu import employee_menu
from asset_menu import asset_menu
from finance import finance_menu
from utils import confirm_action

print("="*40)
print("      ERP ECOSYSTEM")
print("="*40)

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Manage Employees")
        print("2. Manage Assets")
        print("3. Finance Management")
        print("4. Exit")

        choice = input("Select option: ").strip()

        match choice:
            case "1":
                employee_menu()

            case "2":
                asset_menu()

            case "3":
                finance_menu()

            case "4":
                if confirm_action("Do you want to exit? (Y/N): "):
                    print("Thank you! Program exited")
                    break

            case _:
                print("Invalid option Please try again.")


if __name__ == "__main__":
    if login():
        print("\nLogin successful")
        main_menu()
    else:
        print("\nLogin failed Program closed")