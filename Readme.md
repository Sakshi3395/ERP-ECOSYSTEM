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
