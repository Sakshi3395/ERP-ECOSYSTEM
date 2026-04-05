# Full Stack ERP System

A full-stack Enterprise Resource Planning (ERP) system built with Flask backend and React frontend.

## Project Structure

- `backend/` - Flask API server
- `frontend/` - React application with Vite

## Features

- User authentication (login)
- RESTful API backend
- Modern React frontend with routing

## Setup and Installation

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. Create and activate virtual environment:

   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the backend server:
   ```bash
   python app.py
   ```
   The server will start on http://127.0.0.1:5000

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The app will be available at http://localhost:5173

## Quick Start (Recommended)

You can start both backend and frontend together using the orchestrator script:

```bash
npm install # (in the project root, only needed once)
npm run start-all
```
- This will automatically activate the backend virtual environment, run the backend, and start the frontend.
- The backend will use the Python venv located at `backend/venv`.
- The frontend will run on http://localhost:5173

### Environment Variables
- Copy or create a `.env` file in `backend/` and `frontend/` as needed. These files are not tracked in git for security.
- Example for backend/.env:
  ```env
  SECRET_KEY=your_secret_key
  ADMIN_USERNAME=admin
  ADMIN_PASSWORD=your_password
  ```

### Notes
- If you change the backend venv location, update the script in `start.js`.
- Make sure Python and Node.js are installed and available in your PATH.
- For any issues, check the terminal output for errors.

## Usage

1. Start the backend server
2. Start the frontend development server
3. Open http://localhost:5173 in your browser
4. Navigate to /login to access the login page

## API Endpoints

- `POST /api/login` - User authentication

## Technologies Used

- **Backend**: Flask, Flask-CORS
- **Frontend**: React, Vite, React Router, Tailwind CSS
- **Styling**: Tailwind CSS
