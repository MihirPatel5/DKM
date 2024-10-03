import axios from 'axios';

const api = axios.create({
    baseURL: 'http://127.0.0.1:8000/',  // Base URL of your Django backend
});

// Add an interceptor to include the token in requests
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default api;  // Export api as default
