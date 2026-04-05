from flask import Blueprint, request, jsonify
from app.database import get_db_connection
from datetime import datetime

assets_bp = Blueprint("assets", __name__)

def auto_deactivate_expired(cursor):
    today_str = datetime.now().strftime("%Y-%m-%d")
    # Find expired active software
    expired = cursor.execute("SELECT id FROM assets WHERE type = 'software' AND expiry_date < ? AND is_active = 1", (today_str,)).fetchall()
    for exp in expired:
        cursor.execute("UPDATE assets SET is_active = 0 WHERE id = ?", (exp["id"],))
        cursor.execute("DELETE FROM asset_assignments WHERE asset_id = ?", (exp["id"],))
    
    # Also find 'damaged' hardware that shouldn't be active
    damaged = cursor.execute("SELECT id FROM assets WHERE type = 'hardware' AND condition = 'damaged' AND is_active = 1").fetchall()
    for dam in damaged:
        cursor.execute("UPDATE assets SET is_active = 0 WHERE id = ?", (dam["id"],))
        cursor.execute("DELETE FROM asset_assignments WHERE asset_id = ?", (dam["id"],))

@assets_bp.route("/assets", methods=["GET"])
def get_assets():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    status = request.args.get("status", "active")
    
    # Run auto-deactivation rules first
    auto_deactivate_expired(cursor)
    conn.commit()

    if status == "all":
        assets = cursor.execute("SELECT * FROM assets").fetchall()
    elif status == "inactive":
        assets = cursor.execute("SELECT * FROM assets WHERE is_active = 0").fetchall()
    else:
        assets = cursor.execute("SELECT * FROM assets WHERE is_active = 1").fetchall()
        
    conn.close()
    
    return jsonify([dict(a) for a in assets]), 200

@assets_bp.route("/assets", methods=["POST"])
def create_asset():
    data = request.get_json()
    
    name = data.get("name")
    asset_type = data.get("type")
    value = data.get("value", 0)
    condition = data.get("condition")
    expiry_date = data.get("expiry_date")
    
    if not name or not asset_type:
        return jsonify({"error": "Name and type are required"}), 400
        
    if asset_type not in ["hardware", "software"]:
        return jsonify({"error": "Type must be hardware or software"}), 400
        
    is_active = 1
    if asset_type == "hardware":
        if not condition or condition not in ["new", "good", "damaged"]:
            return jsonify({"error": "Hardware must have valid condition"}), 400
        expiry_date = None
        if condition == "damaged":
            is_active = 0
    else:
        if not expiry_date:
            return jsonify({"error": "Software must have expiry date"}), 400
        condition = None
        today_str = datetime.now().strftime("%Y-%m-%d")
        if expiry_date < today_str:
            is_active = 0

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO assets (name, type, value, condition, expiry_date, is_active) VALUES (?, ?, ?, ?, ?, ?)",
        (name, asset_type, value, condition, expiry_date, is_active)
    )
    conn.commit()
    asset_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"message": "Asset created successfully", "id": asset_id}), 201

@assets_bp.route("/assets/<int:asset_id>", methods=["PUT"])
def update_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    existing = cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,)).fetchone()
    if not existing:
        conn.close()
        return jsonify({"error": "Asset not found"}), 404
        
    data = request.get_json()
    name = data.get("name")
    asset_type = data.get("type")
    value = data.get("value", 0)
    condition = data.get("condition")
    expiry_date = data.get("expiry_date")
    
    if not name or not asset_type:
        conn.close()
        return jsonify({"error": "Name and type are required"}), 400
        
    if asset_type not in ["hardware", "software"]:
        conn.close()
        return jsonify({"error": "Type must be hardware or software"}), 400
        
    is_active = existing["is_active"]
    
    if asset_type == "hardware":
        if not condition or condition not in ["new", "good", "damaged"]:
            conn.close()
            return jsonify({"error": "Hardware must have a valid condition (new, good, damaged)"}), 400
        expiry_date = None 
        if condition == "damaged":
            is_active = 0
            cursor.execute("DELETE FROM asset_assignments WHERE asset_id = ?", (asset_id,))
    else:
        if not expiry_date:
            conn.close()
            return jsonify({"error": "Software must have an expiry date"}), 400
        condition = None 
        today_str = datetime.now().strftime("%Y-%m-%d")
        if expiry_date < today_str:
            is_active = 0
            cursor.execute("DELETE FROM asset_assignments WHERE asset_id = ?", (asset_id,))
        
    cursor.execute(
        "UPDATE assets SET name = ?, type = ?, value = ?, condition = ?, expiry_date = ?, is_active = ? WHERE id = ?",
        (name, asset_type, value, condition, expiry_date, is_active, asset_id)
    )
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Asset updated successfully"}), 200

@assets_bp.route("/assets/<int:asset_id>/deactivate", methods=["PATCH"])
def deactivate_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    existing = cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,)).fetchone()
    if not existing:
        conn.close()
        return jsonify({"error": "Asset not found"}), 404
        
    cursor.execute("UPDATE assets SET is_active = 0 WHERE id = ?", (asset_id,))
    cursor.execute("DELETE FROM asset_assignments WHERE asset_id = ?", (asset_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Asset deactivated successfully"}), 200

@assets_bp.route("/assets/<int:asset_id>/reactivate", methods=["PATCH"])
def reactivate_asset(asset_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    existing = cursor.execute("SELECT * FROM assets WHERE id = ?", (asset_id,)).fetchone()
    if not existing:
        conn.close()
        return jsonify({"error": "Asset not found"}), 404
        
    # Validation: Can't reactivate damaged hardware or expired software
    if existing["type"] == "hardware" and existing["condition"] == "damaged":
        conn.close()
        return jsonify({"error": "Cannot reactivate a damaged asset. Please update condition first."}), 400
        
    if existing["type"] == "software":
        today_str = datetime.now().strftime("%Y-%m-%d")
        if existing["expiry_date"] and existing["expiry_date"] < today_str:
            conn.close()
            return jsonify({"error": "Cannot reactivate an expired software asset. Please update expiry date first."}), 400
            
    cursor.execute("UPDATE assets SET is_active = 1 WHERE id = ?", (asset_id,))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Asset reactivated successfully"}), 200
