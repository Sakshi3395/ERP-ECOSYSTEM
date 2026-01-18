import os
from employee import Employee, Manager
from asset import Hardware, Software

def read_data_from_employee():
    emp_dict = {}
    if not os.path.exists("employee.txt"): return emp_dict
    with open("employee.txt", "r") as f:
        for line in f:
            p = line.strip().split("|")
            if len(p) < 4: continue
            if p[2].lower() == "manager":
                emp_dict[p[0]] = Manager(p[0], p[1], p[2], float(p[3]), float(p[4]))
            else:
                emp_dict[p[0]] = Employee(p[0], p[1], p[2], float(p[3]))
    return emp_dict

def save_employee_data(emp_dict):
    with open("employee.txt", "w") as f:
        for e in emp_dict.values():
            if isinstance(e, Manager):
                f.write(f"{e.emp_id}|{e.name}|manager|{e.salary}|{e.bonus}\n")
            else:
                f.write(f"{e.emp_id}|{e.name}|{e.role}|{e.salary}\n")

def read_data_from_assets():
    asset_dict = {}
    if not os.path.exists("assets.txt"): return asset_dict
    with open("assets.txt", "r") as f:
        for line in f:
            p = line.strip().split("|")
            if len(p) < 4: continue
            if p[2] == "Hardware":
                asset_dict[p[0]] = Hardware(p[0], p[1], float(p[3]), p[4])
            else:
                asset_dict[p[0]] = Software(p[0], p[1], float(p[3]), p[4])
    return asset_dict

def save_assets_data(asset_dict):
    with open("assets.txt", "w") as f:
        for a in asset_dict.values():
            if isinstance(a, Hardware):
                f.write(f"{a.asset_id}|{a.name}|Hardware|{a.value}|{a.condition}\n")
            else:
                f.write(f"{a.asset_id}|{a.name}|Software|{a.value}|{a.expiry_date}\n")

def save_assignments(emp_dict):
    with open("assignments.txt", "w") as f:
        for emp in emp_dict.values():
            for asset in emp.assets:
                f.write(f"{emp.emp_id}|{asset.asset_id}\n")

def load_assignments(emp_dict, asset_dict):
    if not os.path.exists("assignments.txt"): return
    with open("assignments.txt", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                eid, aid = parts
                if eid in emp_dict and aid in asset_dict:
                    if asset_dict[aid] not in emp_dict[eid].assets:
                        emp_dict[eid].assets.append(asset_dict[aid])