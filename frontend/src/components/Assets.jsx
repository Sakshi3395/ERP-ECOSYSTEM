import React, { useState, useEffect } from "react";
import { api } from "../api/axios";

export const Assets = () => {
  const [assets, setAssets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [editId, setEditId] = useState(null);
  const [depreciationRate, setDepreciationRate] = useState(20);
  const [formData, setFormData] = useState({
    name: "",
    type: "hardware",
    value: "",
    condition: "good",
    expiry_date: "",
  });

  const fetchAssets = async () => {
    try {
      setLoading(true);
      const res = await api.get("/assets?status=all");
      setAssets(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAssets();
  }, []);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editId) {
        await api.put(`/assets/${editId}`, formData);
      } else {
        await api.post("/assets", formData);
      }
      
      setFormData({
        name: "",
        type: "hardware",
        value: "",
        condition: "good",
        expiry_date: "",
      });
      setEditId(null);
      fetchAssets();
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.error || "Error saving asset");
    }
  };

  const handleEdit = (asset) => {
    setEditId(asset.id);
    setFormData({
      name: asset.name,
      type: asset.type,
      value: asset.value,
      condition: asset.condition || "good",
      expiry_date: asset.expiry_date || "",
    });
  };

  const handleCancelEdit = () => {
    setEditId(null);
    setFormData({
      name: "",
      type: "hardware",
      value: "",
      condition: "good",
      expiry_date: "",
    });
  };

  const deactivateAsset = async (id) => {
    if (!window.confirm("Are you sure you want to deactivate this asset?")) return;
    try {
      await api.patch(`/assets/${id}/deactivate`);
      fetchAssets();
    } catch (err) {
      console.error(err);
    }
  };

  const reactivateAsset = async (id) => {
    try {
      await api.patch(`/assets/${id}/reactivate`);
      fetchAssets();
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.error || "Cannot reactivate asset.");
    }
  };

  const todayStr = new Date().toISOString().split("T")[0];

  return (
    <div className="space-y-6">
      <div className="bg-slate-800 p-6 rounded-lg border border-slate-700">
        <h2 className="text-xl font-semibold mb-4 text-blue-400">
          {editId ? "Edit Asset" : "Add New Asset"}
        </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-1">Asset Name</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-1">Type</label>
              <select
                name="type"
                value={formData.type}
                onChange={handleChange}
                disabled={!!editId} // Typically shouldn't change type after creation, but optional
                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500 disabled:opacity-50"
              >
                <option value="hardware">Hardware</option>
                <option value="software">Software</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-400 mb-1">Value ($)</label>
              <input
                type="number"
                name="value"
                value={formData.value}
                onChange={handleChange}
                required
                min="0"
                step="0.01"
                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
              />
            </div>

            {formData.type === "hardware" ? (
              <div>
                <label className="block text-sm font-medium text-slate-400 mb-1">Condition</label>
                <select
                  name="condition"
                  value={formData.condition}
                  onChange={handleChange}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
                >
                  <option value="new">New</option>
                  <option value="good">Good</option>
                  <option value="damaged">Damaged (Will Auto-Deactivate)</option>
                </select>
              </div>
            ) : (
              <div>
                <label className="block text-sm font-medium text-slate-400 mb-1">Expiry Date</label>
                <input
                  type="date"
                  name="expiry_date"
                  value={formData.expiry_date}
                  onChange={handleChange}
                  required
                  min={todayStr}
                  className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 focus:outline-none focus:border-blue-500"
                />
                <p className="text-xs text-slate-500 mt-1">Past dates will auto-deactivate the asset.</p>
              </div>
            )}
          </div>
          <div className="flex gap-3">
            <button
              type="submit"
              className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-6 rounded-lg transition"
            >
              {editId ? "Update Asset" : "Add Asset"}
            </button>
            {editId && (
              <button
                type="button"
                onClick={handleCancelEdit}
                className="bg-slate-700 hover:bg-slate-600 text-white font-medium py-2 px-6 rounded-lg transition"
              >
                Cancel
              </button>
            )}
          </div>
        </form>
      </div>

      <div className="bg-slate-800 rounded-lg border border-slate-700 overflow-hidden">
        <div className="p-6 border-b border-slate-700 flex justify-between items-center flex-wrap gap-4">
          <h2 className="text-xl font-semibold">Asset Inventory</h2>
          <div className="flex items-center space-x-3 bg-slate-900/80 p-2 px-4 rounded-lg border border-slate-700/80">
            <span className="text-xl">📉</span>
            <label className="text-sm font-medium text-slate-300">Hardware Depreciation Rate:</label>
            <div className="flex items-center">
              <input
                type="number"
                min="0"
                max="100"
                value={depreciationRate}
                onChange={(e) => setDepreciationRate(e.target.value)}
                className="w-16 bg-slate-950 border border-slate-600 rounded-l-md text-slate-100 font-semibold px-2 py-1 text-sm focus:outline-none focus:border-blue-500 text-center"
              />
              <span className="bg-slate-700 border border-l-0 border-slate-600 rounded-r-md px-2 py-1 text-sm text-slate-300">%</span>
            </div>
          </div>
        </div>
        {loading ? (
          <div className="p-6 text-center text-slate-400">Loading...</div>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead className="bg-slate-900 text-slate-400">
                <tr>
                  <th className="px-6 py-3 font-medium">Name</th>
                  <th className="px-6 py-3 font-medium">Type</th>
                  <th className="px-6 py-3 font-medium">Value</th>
                  <th className="px-6 py-3 font-medium">Condition/Expiry</th>
                  <th className="px-6 py-3 font-medium">Status</th>
                  <th className="px-6 py-3 font-medium text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-700">
                {assets.length === 0 ? (
                  <tr>
                    <td colSpan="6" className="px-6 py-4 text-center text-slate-400">
                      No assets found.
                    </td>
                  </tr>
                ) : (
                  assets.map((asset) => (
                    <tr key={asset.id} className={`transition ${asset.is_active ? 'hover:bg-slate-750' : 'bg-slate-800/50 opacity-75'}`}>
                      <td className="px-6 py-4">{asset.name}</td>
                      <td className="px-6 py-4 capitalize">{asset.type}</td>
                      <td className="px-6 py-4">
                        <div className="font-medium text-slate-200">${asset.value?.toFixed(2)}</div>
                        {asset.type === "hardware" && depreciationRate > 0 && asset.is_active === 1 && (
                          <div className="text-xs mt-1.5 p-1.5 bg-slate-900/50 rounded border border-slate-700/50">
                            <div className="text-orange-400 font-medium tracking-wide">
                              -${(asset.value * (depreciationRate / 100)).toFixed(2)} (Dep.)
                            </div>
                            <div className="text-emerald-400 font-bold mt-0.5">
                              Net: ${(asset.value * (1 - depreciationRate / 100)).toFixed(2)}
                            </div>
                          </div>
                        )}
                      </td>
                      <td className="px-6 py-4">
                        {asset.type === "hardware" ? (
                          <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                            asset.condition === 'new' ? 'bg-green-500/20 text-green-400' :
                            asset.condition === 'good' ? 'bg-blue-500/20 text-blue-400' :
                            'bg-red-500/20 text-red-400'
                          }`}>
                            {asset.condition}
                          </span>
                        ) : (
                          <span className="text-slate-300">{asset.expiry_date}</span>
                        )}
                      </td>
                      <td className="px-6 py-4">
                         {asset.is_active ? (
                           <span className="px-2 py-1 block w-max bg-emerald-500/20 text-emerald-400 rounded-md text-xs font-semibold">Active</span>
                         ) : (
                           <span className="px-2 py-1 block w-max bg-slate-700 text-slate-400 rounded-md text-xs font-semibold">Inactive</span>
                         )}
                      </td>
                      <td className="px-6 py-4 text-right space-x-3">
                        <button
                          onClick={() => handleEdit(asset)}
                          className="text-blue-400 hover:text-blue-300 font-medium text-sm transition"
                        >
                          Edit
                        </button>
                        {asset.is_active ? (
                          <button
                            onClick={() => deactivateAsset(asset.id)}
                            className="text-red-400 hover:text-red-300 font-medium text-sm transition"
                          >
                            Deactivate
                          </button>
                        ) : (
                          <button
                            onClick={() => reactivateAsset(asset.id)}
                            className="text-emerald-400 hover:text-emerald-300 font-medium text-sm transition"
                          >
                            Reactivate
                          </button>
                        )}
                      </td>
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

export default Assets;
