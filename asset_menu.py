from asset import Hardware, Software
from utils import confirm_action
from file_manager import read_data_from_assets, save_assets_data, save_assignments
import employee_menu

# Load existing assets from file into the dictionary
assets = read_data_from_assets()

def asset_menu():
    while True:
        print("\n=== ASSET MANAGEMENT ===")
        print("1. Add Asset")
        print("2. View Assets")
        print("3. Assign Asset to Employee")
        print("4. Back")

        choice = input("Select option: ").strip()

        match choice:
            case "1":
                atype = input("Type (Hardware/Software): ").lower()
                name = input("Asset Name: ")
                val = float(input("Asset Value: "))
                # Generate unique ID
                aid = f"A{100 + len(assets) + 1}"

                if atype == "hardware":
                    cond = input("Condition: ")
                    assets[aid] = Hardware(aid, name, val, cond)
                elif atype == "software":
                    exp = input("Expiry Date: ")
                    assets[aid] = Software(aid, name, val, exp)
                else:
                    print("Invalid type!")
                    continue

                # --- CRITICAL FIX: This line writes to assets.txt ---
                save_assets_data(assets)
                print(f"✔ Asset {aid} added and saved to assets.txt")

            case "2":
                if not assets:
                    print("No assets found.")
                for a in assets.values():
                    print(a)

            case "3":
                aid = input("Asset ID: ")
                eid = input("Employee ID: ")
                if aid in assets and eid in employee_menu.employees:
                    emp = employee_menu.employees[eid]
                    if assets[aid] not in emp.assets:
                        emp.assets.append(assets[aid])
                        save_assignments(employee_menu.employees)
                        print("✔ Assigned and saved to assignments.txt")
                else:
                    print("Invalid IDs.")

            case "4":
                break