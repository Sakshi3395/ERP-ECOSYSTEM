import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ASSET_FILE = os.path.join(BASE_DIR, "assets.txt")
EMP_FILE = os.path.join(BASE_DIR, "employees.txt")
FINANCE_FILE = os.path.join(BASE_DIR, "finance.txt")

def save_asset(asset):
    with open(ASSET_FILE, "a") as f:
        f.write(f"{asset.asset_id},{asset.name},{asset.value}\n")

def save_employee(emp):
    with open(EMP_FILE, "a") as f:
        f.write(f"{emp.emp_id},{emp.name},{emp.role},{emp.salary}\n")

def save_finance(text):
    with open(FINANCE_FILE, "a") as f:
        f.write(text + "\n")