import {
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";
import { api } from "../api/axios";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        const res = await api.get("/me");
        setUser(res.data);
      } catch (err) {
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, []);

  const login = async (data) => {
    try {
      await api.post("/login", data);
      const res = await api.get("/me");
      setUser(res.data);
    } catch (err) {
      setUser(null);
      throw err;
    }
  };

  const logout = async () => {
    try {
      await api.post("/logout");
    } catch (err) {
      // best-effort logout, still clear client state
    }
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{ user, login, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
