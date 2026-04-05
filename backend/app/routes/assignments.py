from flask import Blueprint, request, jsonify
from app.database import get_db_connection

assignments_bp = Blueprint("assignments", __name__)

@assignments_bp.route("/assignments", methods=["POST"])
def assign_asset():
    data = request.get_json()
    employee_id = data.get("employee_id")
    asset_id = data.get("asset_id")

    if not employee_id or not asset_id:
        return jsonify({"error": "employee_id and asset_id are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    # Verify employee exists
    emp = cursor.execute("SELECT id FROM employees WHERE id = ?", (employee_id,)).fetchone()
    if not emp:
        conn.close()
        return jsonify({"error": "Employee not found"}), 404

    # Verify asset exists and is active
    asset = cursor.execute("SELECT id, is_active FROM assets WHERE id = ?", (asset_id,)).fetchone()
    if not asset:
        conn.close()
        return jsonify({"error": "Asset not found"}), 404
        
    if not asset["is_active"]:
        conn.close()
        return jsonify({"error": "Cannot assign an inactive asset"}), 400

    # Verify asset is not already assigned
    existing_assignment = cursor.execute("SELECT id FROM asset_assignments WHERE asset_id = ?", (asset_id,)).fetchone()
    if existing_assignment:
        conn.close()
        return jsonify({"error": "Asset is already assigned"}), 400

    cursor.execute(
        "INSERT INTO asset_assignments (employee_id, asset_id) VALUES (?, ?)",
        (employee_id, asset_id)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Asset assigned successfully"}), 201

@assignments_bp.route("/assignments", methods=["GET"])
def get_assignments():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        SELECT a.id, a.employee_id, a.asset_id, e.name as employee_name, ast.name as asset_name 
        FROM asset_assignments a
        JOIN employees e ON a.employee_id = e.id
        JOIN assets ast ON a.asset_id = ast.id
    """
    assignments = cursor.execute(query).fetchall()
    conn.close()

    return jsonify([dict(a) for a in assignments]), 200
