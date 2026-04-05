from flask import Blueprint, request , jsonify, make_response
from werkzeug.security import check_password_hash

from app.database import get_db_connection
from app.utils.jwt import create_refresh_token, create_access_token, decode_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/login', methods = ["POST"])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = get_db_connection()
    cursor= conn.cursor()

    user = cursor.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    conn.close()

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"status": "error", "message": "Invalid Credentials"}), 401
    
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)

    response = make_response(jsonify({"message": "Login successfull"}))

    response.set_cookie("access_token", access_token, httponly=True)
    response.set_cookie("refresh_token", refresh_token, httponly=True)

    return response

@auth_bp.route("/me", methods=["GET"])
def get_me():
    token = request.cookies.get("access_token")

    if not token:
        return jsonify({"message": "UNauthorized"}), 401
    
    decoded = decode_token(token)

    if not decoded:
        return jsonify({"message": "Token Invalid or expired"}), 401
    
    return jsonify({
        "user_id": decoded["user_id"],
        "username": decoded["username"]
    }), 200


@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({"message": "Logged out"}))
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return response, 200


@auth_bp.route('/refresh', methods=["POST"])
def refresh():
    token = request.cookies.get("refresh_token")

    if not token:
        return jsonify({"message": "Unauthorized"}), 401
    
    decoded = decode_token(token)

    if not decoded:
        return jsonify({"message": "Token Invalid or expired"}), 401
    

    conn = get_db_connection()
    cursor= conn.cursor()

    # Ensure tuple for parameter binding has comma
    cursor.execute("SELECT * FROM users WHERE id = ?", (decoded["user_id"],))
    
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"message": "User not found"}), 404

    new_access_token = create_access_token(user)

    response = make_response(jsonify({"message": "Token refreshed"}))
    response.set_cookie("access_token", new_access_token, httponly=True)

    return response