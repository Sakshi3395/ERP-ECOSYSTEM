from login import login
import employee_menu as em
import asset_menu as am
from finance import finance_menu
from utils import confirm_action
from file_manager import load_assignments

print("="*40)
print("      ERP ECOSYSTEM")
print("="*40)

def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Manage Employees\n2. Manage Assets\n3. Finance Management\n4. Exit")
        choice = input("Select: ").strip()
        match choice:
            case "1": em.employee_menu()
            case "2": am.asset_menu()
            case "3": finance_menu()
            case "4":
                if confirm_action("Exit? "): break

if __name__ == "__main__":
    if login():
        load_assignments(em.employees, am.assets)
        main_menu()