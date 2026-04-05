import { useState, useEffect } from 'react';
import { api } from '../api/axios';

const Employees = () => {
    const [employees, setEmployees] = useState([]);
    const [form, setForm] = useState({
        name: "",
        role: "staff",
        salary: "",
        bonus: "",
    });
    const [editId, setEditId] = useState(null);

    const fetchEmployees = async () => {
        try {
            const res = await api.get('/employees');
            setEmployees(res.data);
        } catch (error) {
            console.error(error);
        }
    };

    useEffect(() => {
        fetchEmployees();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const payload = {
                ...form,
                salary: Number(form.salary),
                bonus: Number(form.bonus)
            };

            if (editId) {
                await api.put(`/employees/${editId}`, payload);
            } else {
                await api.post("/employees", payload);
            }

            setForm({ name: "", role: "staff", salary: "", bonus: "" });
            setEditId(null);
            fetchEmployees();
        } catch (error) {
            console.error(error);
        }
    };

    const handleDelete = async (id) => {
        try {
            await api.delete(`/employees/${id}`);
            fetchEmployees();
        } catch (error) {
            console.error(error);
        }
    };

    const handleEdit = (emp) => {
        setForm({
            name: emp.name,
            role: emp.role,
            salary: emp.salary,
            bonus: emp.bonus
        });
        setEditId(emp.id);
    };

    const handleCancelEdit = () => {
        setForm({ name: "", role: "staff", salary: "", bonus: "" });
        setEditId(null);
    };

    return (
        <section className="flex flex-col lg:flex-row gap-6">
            {/* Form Section */}
            <div className="w-full lg:w-1/3 min-w-[300px]">
                <div className="bg-slate-800 rounded-xl shadow-lg border border-slate-700 p-6">
                    <h2 className="text-xl font-semibold mb-4 text-blue-400">
                        {editId ? 'Edit Employee' : 'Add Employee'}
                    </h2>
                    <form onSubmit={handleSubmit} className="space-y-4">
                        <div>
                            <label htmlFor="name" className="block text-sm font-medium text-slate-300 mb-1">Name</label>
                            <input 
                                type="text" id="name" required
                                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-slate-100 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                                value={form.name} 
                                onChange={(e) => setForm({ ...form, name: e.target.value })} 
                            />
                        </div>
                        <div>
                            <label htmlFor="role" className="block text-sm font-medium text-slate-300 mb-1">Role</label>
                            <select 
                                id="role" 
                                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-slate-100 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                                value={form.role} 
                                onChange={(e) => setForm({ ...form, role: e.target.value })}
                            >
                                <option value="staff">Staff</option>
                                <option value="manager">Manager</option>
                            </select>
                        </div>
                        <div>
                            <label htmlFor="salary" className="block text-sm font-medium text-slate-300 mb-1">Salary</label>
                            <input 
                                type="number" id="salary" required min="0"
                                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-slate-100 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500"
                                value={form.salary} 
                                onChange={(e) => setForm({ ...form, salary: e.target.value })} 
                            />
                        </div>
                        <div>
                            <label htmlFor="bonus" className="block text-sm font-medium text-slate-300 mb-1">Bonus</label>
                            <input 
                                type="number" id="bonus" min="0" disabled={form.role === 'staff'}
                                className="w-full bg-slate-900 border border-slate-700 rounded-lg px-4 py-2 text-slate-100 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
                                value={form.bonus} 
                                onChange={(e) => setForm({ ...form, bonus: e.target.value })} 
                            />
                        </div>
                        <div className="flex gap-3 pt-2">
                            <button 
                                type="submit"
                                className="flex-1 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-lg transition"
                            >
                                {editId ? 'Update' : 'Add'}
                            </button>
                            {editId && (
                                <button 
                                    type="button" onClick={handleCancelEdit}
                                    className="flex-1 bg-slate-700 hover:bg-slate-600 text-white font-medium py-2 px-4 rounded-lg transition"
                                >
                                    Cancel
                                </button>
                            )}
                        </div>
                    </form>
                </div>
            </div>

            {/* List Section */}
            <div className="w-full lg:w-2/3">
                <div className="bg-slate-800 rounded-xl shadow-lg border border-slate-700 overflow-hidden">
                    <div className="px-6 py-4 border-b border-slate-700">
                        <h2 className="text-xl font-semibold text-slate-100">Employee List</h2>
                    </div>
                    <div className="overflow-x-auto">
                        <table className="w-full text-left border-collapse">
                            <thead>
                                <tr className="bg-slate-900/50 text-slate-400 text-sm uppercase tracking-wider">
                                    <th className="px-6 py-4 font-medium">Name</th>
                                    <th className="px-6 py-4 font-medium">Role</th>
                                    <th className="px-6 py-4 font-medium">Salary</th>
                                    <th className="px-6 py-4 font-medium">Bonus</th>
                                    <th className="px-6 py-4 font-medium">Assets</th>
                                    <th className="px-6 py-4 font-medium text-right">Actions</th>
                                </tr>
                            </thead>
                            <tbody className="divide-y divide-slate-700/50">
                                {employees.length === 0 ? (
                                    <tr>
                                        <td colSpan="5" className="px-6 py-8 text-center text-slate-500">
                                            No employees found. Add one to get started.
                                        </td>
                                    </tr>
                                ) : (
                                    employees.map((emp) => (
                                        <tr key={emp.id} className="hover:bg-slate-800/80 transition group">
                                            <td className="px-6 py-4 font-medium text-slate-200">{emp.name}</td>
                                            <td className="px-6 py-4">
                                                <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium capitalize ${
                                                    emp.role === 'manager' ? 'bg-purple-500/10 text-purple-400 border border-purple-500/20' : 'bg-blue-500/10 text-blue-400 border border-blue-500/20'
                                                }`}>
                                                    {emp.role}
                                                </span>
                                            </td>
                                            <td className="px-6 py-4 text-slate-300">${emp.salary?.toLocaleString() || 0}</td>
                                            <td className="px-6 py-4 text-slate-300">${emp.bonus?.toLocaleString() || 0}</td>
                                            <td className="px-6 py-4">
                                                {emp.assets && emp.assets.length > 0 ? (
                                                    <div className="flex flex-wrap gap-1">
                                                        {emp.assets.map(a => (
                                                            <span key={a.id} className="inline-block bg-slate-700 border border-slate-600 text-slate-300 text-xs px-2 py-1 rounded">
                                                                {a.name}
                                                            </span>
                                                        ))}
                                                    </div>
                                                ) : (
                                                    <span className="text-slate-500 text-xs italic">None</span>
                                                )}
                                            </td>
                                            <td className="px-6 py-4 text-right space-x-3">
                                                <button 
                                                    onClick={() => handleEdit(emp)}
                                                    className="text-blue-400 hover:text-blue-300 font-medium text-sm transition"
                                                >
                                                    Edit
                                                </button>
                                                <button 
                                                    onClick={() => handleDelete(emp.id)}
                                                    className="text-red-400 hover:text-red-300 font-medium text-sm transition"
                                                >
                                                    Delete
                                                </button>
                                            </td>
                                        </tr>
                                    ))
                                )}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Employees;