from flask import Blueprint, jsonify
from app.database import get_db_connection

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/dashboard/stats", methods=["GET"])
def get_dashboard_stats():
    conn = get_db_connection()
    cursor = conn.cursor()

    # total_employees
    emp_count = cursor.execute("SELECT COUNT(*) FROM employees").fetchone()[0]

    # total_assets (active)
    assets_count = cursor.execute("SELECT COUNT(*) FROM assets WHERE is_active = 1").fetchone()[0]

    # total_asset_value
    asset_value = cursor.execute("SELECT SUM(value) FROM assets WHERE is_active = 1").fetchone()[0] or 0

    # total_salary_cost (salary + bonus)
    salary_sum = cursor.execute("SELECT SUM(salary) FROM employees").fetchone()[0] or 0
    bonus_sum = cursor.execute("SELECT SUM(bonus) FROM employees").fetchone()[0] or 0
    total_salary_cost = salary_sum + bonus_sum

    # number_of_assigned_assets
    assigned_count = cursor.execute("SELECT COUNT(DISTINCT asset_id) FROM asset_assignments").fetchone()[0]

    # number_of_unassigned_assets (active only)
    unassigned_count = assets_count - assigned_count

    conn.close()

    return jsonify({
        "total_employees": emp_count,
        "total_assets": assets_count,
        "total_asset_value": asset_value,
        "total_salary_cost": total_salary_cost,
        "number_of_assigned_assets": assigned_count,
        "number_of_unassigned_assets": unassigned_count
    }), 200
