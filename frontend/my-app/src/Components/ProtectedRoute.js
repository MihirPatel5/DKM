import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
    const token = localStorage.getItem('access_token');
    
    if (!token) {
        // If no token exists, redirect to the login page
        return <Navigate to="/login" />;
    }
    
    // If token exists, render the children components
    return children;
};

export default ProtectedRoute;
