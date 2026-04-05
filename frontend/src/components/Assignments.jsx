import React, { useState, useEffect } from "react";
import { api } from "../api/axios";

export const Assignments = () => {
  const [assignments, setAssignments] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [assets, setAssets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    employee_id: "",
    asset_id: "",
  });

  const fetchData = async () => {
    try {
      setLoading(true);
      const [assignRes, empRes, assetRes] = await Promise.all([
        api.get("/assignments"),
        api.get("/employees"),
        api.get("/assets"),
      ]);

      setAssignments(assignRes.data);
      setEmployees(empRes.data);
      setAssets(assetRes.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.employee_id || !formData.asset_id) {
      alert("Please select both employee and asset.");
      return;
    }

    try {
      await api.post("/assignments", formData);
      setFormData({ employee_id: "", asset_id: "" });
      fetchData();
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.error || "Error assigning asset");
    }
  };

  // Filter available assets: must be active (already done in /api/assets) and unassigned
  const assignedAssetIds = assignments.map(a => a.asset_id);
  const availableAssets = assets.filter(a => !assignedAssetIds.includes(a.id));

  return (
    <div className="space-y-6">
      <div className="bg-slate-800 p-6 rounded-lg border border-slate-700">
        <h2 className="text-xl font-semibold mb-4">Assign Asset</h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-1">Employee</label>
              <select
                name="employee_id"
                value={formData.employee_id}
                onChange={handleChange}
                required
                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
              >
                <option value="">-- Select Employee --</option>
                {employees.map(emp => (
                  <option key={emp.id} value={emp.id}>{emp.name} ({emp.role})</option>
                ))}
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-1">Asset (Unassigned only)</label>
              <select
                name="asset_id"
                value={formData.asset_id}
                onChange={handleChange}
                required
                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
              >
                <option value="">-- Select Asset --</option>
                {availableAssets.map(asset => (
                  <option key={asset.id} value={asset.id}>{asset.name} ({asset.type})</option>
                ))}
              </select>
            </div>
          </div>
          <button
            type="submit"
            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-6 rounded-lg transition"
            disabled={availableAssets.length === 0}
          >
            Assign
          </button>
        </form>
      </div>

      <div className="bg-slate-800 rounded-lg border border-slate-700 overflow-hidden">
        <div className="p-6 border-b border-slate-700">
          <h2 className="text-xl font-semibold">Current Assignments</h2>
        </div>
        {loading ? (
          <div className="p-6 text-center text-slate-400">Loading...</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead className="bg-slate-900 text-slate-400">
                <tr>
                  <th className="px-6 py-3 font-medium">Employee Name</th>
                  <th className="px-6 py-3 font-medium">Asset Name</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-700">
                {assignments.length === 0 ? (
                  <tr>
                    <td colSpan="2" className="px-6 py-4 text-center text-slate-400">
                      No assignments found.
                    </td>
                  </tr>
                ) : (
                  assignments.map((assignment) => (
                    <tr key={assignment.id} className="hover:bg-slate-750 transition">
                      <td className="px-6 py-4">{assignment.employee_name}</td>
                      <td className="px-6 py-4">{assignment.asset_name}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default Assignments;
