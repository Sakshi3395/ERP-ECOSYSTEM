import React, { useState, useEffect } from "react";
import { api } from "../api/axios";

export const Overview = () => {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await api.get("/dashboard/stats");
        setStats(res.data);
      } catch (err) {
        console.error("Failed to fetch dashboard stats", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  if (loading) {
    return <div className="text-slate-400 p-6 tracking-wide">Loading dashboard data...</div>;
  }

  if (!stats) {
    return <div className="text-red-400 p-6">Error loading dashboard stats.</div>;
  }

  const statCards = [
    { label: "Total Employees", value: stats.total_employees, icon: "👤", color: "text-blue-400" },
    { label: "Active Assets", value: stats.total_assets, icon: "💻", color: "text-green-400" },
    { label: "Total Asset Value", value: `$${stats.total_asset_value.toFixed(2)}`, icon: "💰", color: "text-emerald-400" },
    { label: "Total Salary Cost", value: `$${stats.total_salary_cost.toLocaleString()}`, icon: "💵", color: "text-purple-400" },
    { label: "Assigned Assets", value: stats.number_of_assigned_assets, icon: "📎", color: "text-orange-400" },
    { label: "Unassigned Assets", value: stats.number_of_unassigned_assets, icon: "📦", color: "text-gray-400" },
  ];

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-semibold text-slate-100 mb-6">Company Overview</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {statCards.map((card, idx) => (
          <div key={idx} className="bg-slate-800 p-6 rounded-xl border border-slate-700 flex items-center space-x-4 shadow-sm hover:shadow-md transition">
            <div className={`text-4xl ${card.color}`}>{card.icon}</div>
            <div>
              <p className="text-sm text-slate-400 font-medium mb-1">{card.label}</p>
              <p className="text-2xl font-bold text-slate-100">{card.value}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Overview;
