from file_manager import save_asset
from asset import Hardware, Software
from employee_menu import employees
from utils import confirm_action

assets = {}

def asset_menu():
    while True:
        print("\n=== ASSET MANAGEMENT ===")
        print("1. Add Asset")
        print("2. View Assets")
        print("3. Assign Asset to Employee")
        print("4. Calculate Depreciation")
        print("5. Back")

        choice = input("Select option: ")

        match choice:
            case "1":
                asset_type = input("Type (Hardware/Software): ").lower()
                name = input("Asset Name: ")
                value = float(input("Asset Value: "))
                asset_id = f"A{100 + len(assets) + 1}"

                if not confirm_action("Confirm add asset? (Y/N): "):
                    continue

                match asset_type:
                    case "hardware":
                        condition = input("Condition: ")
                        assets[asset_id] = Hardware(asset_id, name, value, condition)
                    case "software":
                        expiry = input("Expiry Date: ")
                        assets[asset_id] = Software(asset_id, name, value, expiry)
                    case _:
                        print("Invalid asset type")
                        continue

                print(f"✔ Asset added with ID {asset_id}")

            case "2":
                for asset in assets.values():
                    print(asset)

            case "3":
                aid = input("Asset ID: ")
                eid = input("Employee ID: ")
                if aid in assets and eid in employees:
                    if confirm_action("Confirm assign asset? (Y/N): "):
                        employees[eid].assets.append(assets[aid])
                        print("✔ Asset assigned")
                else:
                    print("Invalid ID")

            case "4":
                aid = input("Asset ID: ")
                years = int(input("Enter years: "))
                if aid in assets:
                    val = assets[aid].depreciate(years)
                    print(f"Current Value: ₹{val:.2f}")
                else:
                    print("Asset not found")

            case "5":
                break

            case _:
                print("Invalid choice")