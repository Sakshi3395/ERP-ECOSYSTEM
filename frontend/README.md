# Mini ERP - Frontend

## Project Overview
This is the frontend for the Mini ERP application, built with React and Vite. It serves as the admin panel interface where the admin can manage employees, assets, and view company overview statistics.

## Folder Structure & Files

- `index.html`: The main HTML file serving the React app.
- `vite.config.js`: Configuration file for the Vite bundler.
- `package.json` / `package-lock.json`: NPM dependencies and project metadata.
- `src/`: The main source code directory.
  - `main.jsx`: The React entry point which renders the `App` component into the DOM.
  - `App.jsx`: Main application component setting up React Router routes (`/login` and `/dashboard`).
  - `App.css` / `index.css`: Global cascading style sheets.
  - `api/`: Directory for API communication.
    - `axios.js`: Configured Axios instance (typically for base URL and intercepting tokens).
  - `components/`: Reusable UI components.
    - `ProtectedRoute.jsx`: A wrapper component guarding routes that require admin access.
  - `context/`: React Context providers for state management.
    - `AuthContext.jsx`: Manages the global authentication state (current user, login status).
  - `pages/`: Represents the different views/pages of the application.
    - `auth/Login.jsx`: The login page UI and form handling logic.
    - `dashboard/AdminDashboard.jsx`: The main dashboard page wrapper (currently minimal).

## Current State & Missing Features
The frontend currently supports a functional authentication flow (login screen, protected routes, and auth state management). 
The following required features for the Admin Dashboard are **missing**:
- **Main Dashboard View:** A visual overview of company stats (Total Employee Cost, Asset Cost, Depreciated Assets).
- **Employee Management UI:** A dedicated section or page to view, add, edit, and delete employees.
- **Asset Management UI:** A section to view, add, edit, and delete assets.
- **Asset Assignment UI:** A form/modal to assign existing assets to specific employees.

## Implementation Plan (Step-by-Step)
To achieve the missing features, follow this simple plan to extend the UI:

1. **Dashboard Layout Structure:**
   - Update `AdminDashboard.jsx` to include a Sidebar for navigation (Tabs: Overview, Employees, Assets, Assignments).
   - Use a state variable to toggle which view is currently active.

2. **Overview Component (`src/components/Overview.jsx`):**
   - Create a component that fetches data from the backend analytics endpoint (`/api/dashboard/stats`).
   - Display the data using simple metric cards (e.g., Total Employees, Total Asset Cost).

3. **Employee Management Component (`src/components/Employees.jsx`):**
   - Create a table to list all employees.
   - Add a form (either inline or in a modal) to create standard employee records.
   - Implement action buttons on each table row for `Edit` and `Delete` linking to the backend API.

4. **Asset Management Component (`src/components/Assets.jsx`):**
   - Create a table to list all company assets.
   - Add a form to create/edit assets.
   - Ensure the `value` and `type` fields are clearly visible for financial tracking.

5. **Assignment Component (`src/components/Assignments.jsx`):**
   - Build a UI featuring two dropdowns: one listing all employees and another listing available assets.
   - Add an "Assign" button that posts to the backend and associates the employee with the asset.
   - Display a list/table of active assignments below the form.

6. **Integrate and Polish:**
   - Link all these newly created components to the `AdminDashboard`.
   - Ensure the UI remains clean and does not overcomplicate navigation. Use generic CSS or a simple library if added to keep styling straightforward.
