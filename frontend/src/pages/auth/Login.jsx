import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const { login } = useAuth();

  const handleLogin = async (e) => {
    e.preventDefault();
    setMessage("");
    try {
      await login({ username, password });
      navigate("/dashboard");
    } catch (err) {
      setMessage("Invalid credentials");
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword((prev) => !prev);
  };

  return (
    <section className="min-h-screen flex items-center justify-center bg-background p-4">
      <div className="w-full max-w-md bg-surface rounded-xl shadow-lg p-8 border border-border">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-serif text-text-primary">
            Login
          </h2>
          <p className="text-text-secondary mt-2">
            Access your ERP dashboard
          </p>
        </div>

        <form onSubmit={handleLogin} className="space-y-6">
          {/* Username field */}
          <div>
            <label
              htmlFor="username"
              className="block text-sm font-medium text-text-secondary mb-1">
              Username{" "}
              <span className="text-danger">*</span>
            </label>
            <input
              type="text"
              name="username"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-4 py-2 border border-border rounded-lg bg-surface text-text-primary focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition"
              placeholder="Enter your username"
              required
            />
          </div>

          {/* Password field with visibility toggle */}
          <div>
            <label
              htmlFor="password"
              className="block text-sm font-medium text-text-secondary mb-1">
              Password{" "}
              <span className="text-danger">*</span>
            </label>
            <div className="relative">
              <input
                type={showPassword ? "text" : "password"}
                name="password"
                id="password"
                value={password}
                onChange={(e) =>
                  setPassword(e.target.value)
                }
                className="w-full px-4 py-2 pr-12 border border-border rounded-lg bg-surface text-text-primary focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition"
                placeholder="Enter your password"
                required
              />
              <button
                type="button"
                onClick={togglePasswordVisibility}
                className="absolute right-3 top-1/2 -translate-y-1/2 text-text-secondary hover:text-primary focus:outline-none transition-transform duration-200 active:scale-90"
                aria-label={
                  showPassword
                    ? "Hide password"
                    : "Show password"
                }>
                {showPassword ? (
                  // Eye-off icon (password hidden)
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.5}
                    stroke="currentColor"
                    className="w-5 h-5">
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88"
                    />
                  </svg>
                ) : (
                  // Eye icon (password visible)
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    strokeWidth={1.5}
                    stroke="currentColor"
                    className="w-5 h-5">
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z"
                    />
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                    />
                  </svg>
                )}
              </button>
            </div>
          </div>

          {/* Submit button */}
          <div>
            <button
              type="submit"
              className="w-full bg-primary hover:bg-primary-dark text-white font-medium py-2.5 rounded-lg transition duration-200 ease-in-out transform hover:scale-[1.02] focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2">
              Sign In
            </button>
          </div>

          {/* Message display */}
          {message && (
            <div
              className={`mt-4 p-3 rounded-lg text-sm ${
                message.startsWith("Welcome")
                  ? "bg-success/10 text-success border border-success/20"
                  : "bg-danger/10 text-danger border border-danger/20"
              }`}>
              {message}
            </div>
          )}
        </form>
      </div>
    </section>
  );
};

export default Login;
