# Mini ERP - Backend

## Project Overview
This is the backend for the Mini ERP application, developed using Python and Flask. It uses a lightweight SQLite database for storage and JWT for authentication.

## Folder Structure & Files

- `run.py`: The main entry point for the Flask application. It initializes the app and configs CORS.
- `database.db`: The SQLite database file generated at runtime.
- `requirements.txt`: Contains all the Python dependencies required for the project.
- `.env`: Environment variables configuration (like secret keys, admin credentials).
- `app/`: The core application directory.
  - `__init__.py`: The app factory. It initializes the Flask app, connects to the database, seeds the admin user, and registers the authentication blueprint.
  - `database.py`: Contains the database connection logic and the `init_db` function which defines the schema for `users`, `employees`, `assets`, and `asset_assignments` tables.
  - `routes/`: Directory for API route handlers.
    - `auth.py`: Contains endpoints for authentication (`/login`, `/me`, `/logout`, `/refresh`).
  - `utils/`: Utility functions and helpers.
    - `jwt.py`: Contains logic for creating and decoding access and refresh JWT tokens.

## Current State & Missing Features
Currently, the backend has implemented user authentication (login/logout/token refresh) and the basic database schema. 
However, based on the project requirements, the following features are **missing**:
- **Employee Management:** CRUD operations for employees.
- **Asset Management:** CRUD operations for assets.
- **Asset Assignments:** Endpoints to assign assets to employees and view assignments.
- **Dashboard Overview:** An endpoint to fetch company-wide statistics (e.g., total employees, total asset cost, depreciated assets).

## Implementation Plan (Step-by-Step)
To achieve the missing features, follow this simple plan:

1. **Create Models/Queries Outline:**
   - Instead of a full ORM, stick to the `sqlite3` direct queries as seen in `database.py`.

2. **Develop Employee Routes (`app/routes/employees.py`):**
   - Create a new blueprint for employees.
   - Implement `GET /api/employees` to list all employees.
   - Implement `POST /api/employees` to add a new employee.
   - Implement `PUT /api/employees/<id>` to update employee details.
   - Implement `DELETE /api/employees/<id>` to remove an employee.

3. **Develop Asset Routes (`app/routes/assets.py`):**
   - Create a blueprint for assets.
   - Implement `GET /api/assets` to list all assets.
   - Implement `POST /api/assets` to add an asset.
   - Implement `PUT /api/assets/<id>` to update an asset.
   - Implement `DELETE /api/assets/<id>` to remove an asset.

4. **Develop Assignment Routes (`app/routes/assignments.py`):**
   - Implement `POST /api/assignments` to create a record linking an `employee_id` and `asset_id`.
   - Implement `GET /api/assignments` to list which assets are with which employees.

5. **Develop Dashboard Analytics Route (`app/routes/dashboard.py`):**
   - Implement `GET /api/dashboard/stats` that aggregates data:
     - Count total rows in `employees`.
     - Sum the `salary` + `bonus` from `employees` to get total employee cost.
     - Sum the `value` from `assets` to get total asset cost.
     - Return these stats as a JSON object.

6. **Register Blueprints:**
   - Finally, open `app/__init__.py` and register the newly created blueprints (employees, assets, assignments, dashboard) similar to how `auth_bp` is registered.
