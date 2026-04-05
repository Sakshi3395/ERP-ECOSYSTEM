import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_BASE_URL,
  withCredentials: true,
});

// api.interceptors.response.use(
//   (response) => response,
//   async (error) => {
//     const originalRequest = error.config;
//     if (!originalRequest) {
//       return Promise.reject(error);
//     }

//     if (originalRequest.url.includes("/refresh")) {
//       return Promise.reject(error);
//     }
//     if (
//       error.response?.status === 401 &&
//       !originalRequest._retry
//     ) {
//       originalRequest._retry = true;

//       try {
//         await api.post("/refresh");
//         return api(originalRequest);
//       } catch (err) {
//         window.location.href = "/login";
//       }
//     }
//     return Promise.reject(error);
//   },
// );
