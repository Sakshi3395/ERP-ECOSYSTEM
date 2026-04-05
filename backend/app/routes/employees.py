from flask import Blueprint, request, jsonify
from app.database import get_db_connection

emp_bp = Blueprint("employees", __name__)




@emp_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    name = data.get("name")
    role = data.get("role")
    salary = data.get("salary", 0)
    bonus = data.get("bonus", 0)

    if role not in ["manager", "staff"]:
        return jsonify({"error": "Invalid role"}), 400
    
    if role == "staff":
        bonus = 0
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO employees (name, role, salary, bonus) VALUES (?, ?, ?, ?)", (name, role, salary, bonus))
    conn.commit()
    emp__id = cursor.lastrowid
    conn.close()

    return jsonify({"message": "Employee created successfully", "id": emp__id}), 201


@emp_bp.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    employees_rows = cursor.execute("SELECT * FROM employees").fetchall()
    
    # Also fetch all assignments
    assignments_rows = cursor.execute('''
        SELECT aa.employee_id, a.id, a.name 
        FROM asset_assignments aa
        JOIN assets a ON aa.asset_id = a.id
        WHERE a.is_active = 1
    ''').fetchall()
    
    conn.close()

    employees = []
    for emp in employees_rows:
        emp_dict = dict(emp)
        # Match assignments by stringified employee_id since DB field is TEXT
        emp_dict["assets"] = [{"id": a["id"], "name": a["name"]} for a in assignments_rows if str(a["employee_id"]) == str(emp["id"])]
        employees.append(emp_dict)

    return jsonify(employees), 200



@emp_bp.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    employee = cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,)).fetchone()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()

    name = data.get("name")
    role = data.get("role")
    salary = data.get("salary")
    bonus = data.get("bonus", 0)

    if role not in ["manager", "staff"]:
        return jsonify({"error": "Invalid role"}), 400
    
    if role == "staff":
        bonus = 0

   

    cursor.execute("UPDATE employees SET name = ?, role = ?, salary = ?, bonus = ? WHERE id = ?", (name, role, salary, bonus, emp_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee updated successfully"}), 200


@emp_bp.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    employee = cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,)).fetchone()
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee deleted successfully"}), 200

    
