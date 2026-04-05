import React from "react";
import { Link, Outlet, useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

export const AdminDashboard = () => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = async () => {
    await logout();
    navigate("/login");
  };

  return (
    <div className="flex h-screen bg-slate-900 text-slate-100 font-sans">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-800 border-r border-slate-700 flex flex-col">
        <div className="p-6 border-b border-slate-700">
          <h2 className="text-2xl font-bold text-blue-400">Mini ERP</h2>
        </div>
        
        <nav className="flex-1 p-4 space-y-2">
          <Link 
            to="/dashboard" 
            className="block px-4 py-2 rounded-lg hover:bg-slate-700 transition"
          >
            Overview
          </Link>
          <Link 
            to="/dashboard/employees" 
            className="block px-4 py-2 rounded-lg hover:bg-slate-700 transition"
          >
            Employees
          </Link>
          <Link 
            to="/dashboard/assets" 
            className="block px-4 py-2 rounded-lg hover:bg-slate-700 transition"
          >
            Assets
          </Link>
          <Link 
            to="/dashboard/assignments" 
            className="block px-4 py-2 rounded-lg hover:bg-slate-700 transition"
          >
            Assignments
          </Link>
          <button 
            onClick={handleLogout}
            className="w-full text-left px-4 py-2 mt-auto text-red-400 hover:bg-slate-700 rounded-lg transition"
          >
            Logout
          </button>
        </nav>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 flex flex-col overflow-hidden">
        <header className="h-16 bg-slate-800 border-b border-slate-700 flex items-center justify-between px-6">
          <h1 className="text-xl font-semibold">Admin Panel</h1>
        </header>
        
        <div className="flex-1 overflow-auto p-6 bg-slate-900">
          {/* Renders nested routes (e.g., /dashboard/employees) */}
          <Outlet />
        </div>
      </main>
    </div>
  );
};
