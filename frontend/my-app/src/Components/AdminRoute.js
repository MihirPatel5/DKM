import React from 'react';
import { Navigate } from 'react-router-dom';
// import api from '../api';  

const AdminRoute = ({ children }) => {
    const userRole = localStorage.getItem('user_role'); 
    const isAuthenticated = localStorage.getItem('access_token');

    if (!isAuthenticated || userRole !== 'admin') {
        return <Navigate to="/login" />;
    }

    return children;
};

export default AdminRoute;
