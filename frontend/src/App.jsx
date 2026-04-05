import React from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import Login from "./pages/auth/Login";
import { AdminDashboard } from "./pages/dashboard/AdminDashboard";
import Employees from "./components/Employees";
import { Assets } from "./components/Assets";
import { Assignments } from "./components/Assignments";
import { Overview } from "./components/Overview";
import ProtectedRoute from "./components/ProtectedRoute";
import { AuthProvider } from "./context/AuthContext";

const App = () => {
  return (
    <div>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />

          <Route
            path="/dashboard"
            element={
              <ProtectedRoute adminOnly={true}>
                <AdminDashboard />
              </ProtectedRoute>
            }
          >
            <Route index element={<Overview />} />
            <Route path="employees" element={<Employees />} />
            <Route path="assets" element={<Assets />} />
            <Route path="assignments" element={<Assignments />} />
          </Route>

          <Route
            path="*"
            element={<Navigate to="/login" />}
          />
        </Routes>
      </AuthProvider>
    </div>
  );
};

export default App;
