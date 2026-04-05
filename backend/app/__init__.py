from flask import Flask
from dotenv import load_dotenv
import os

from app.database import init_db, get_db_connection
from werkzeug.security import generate_password_hash


def create_app():
    load_dotenv()

    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    #Initialize DB
    init_db()

    #admin user create
    seed_admin()

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix = "/api")

    from app.routes.employees import emp_bp
    app.register_blueprint(emp_bp, url_prefix = "/api")

    from app.routes.assets import assets_bp
    app.register_blueprint(assets_bp, url_prefix = "/api")

    from app.routes.assignments import assignments_bp
    app.register_blueprint(assignments_bp, url_prefix = "/api")

    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp, url_prefix = "/api")

    return app



def seed_admin():
    conn = get_db_connection()
    cursor = conn.cursor()

    admin_username = os.getenv("ADMIN_USERNAME")
    admin_password = os.getenv("ADMIN_PASSWORD")
    cursor.execute("SELECT * FROM users WHERE username = ?", (admin_username,))
    user = cursor.fetchone()

    if not user:
        hashed_pwd = generate_password_hash(admin_password)
        
        cursor.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (admin_username, hashed_pwd, "admin" ))
        conn.commit()
        print("ADMIN USER CREATED")
    else:
        print("ADMIN ALREADY EXITS")
    
    conn.close()
