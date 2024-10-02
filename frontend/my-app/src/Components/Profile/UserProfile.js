import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserProfile = () => {
    const [user, setUser] = useState({});
    
    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.get('http://127.0.0.1:8000/profile/', {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    }
                });
                setUser(response.data);
            } catch (error) {
                console.error("Error fetching profile:", error);
            }
        };
        
        fetchProfile();
    }, []);

    return (
        <div>
            <h2>My Profile</h2>
            <p>Name: {user.first_name} {user.last_name}</p>
            <p>Email: {user.email}</p>
            <p>Phone: {user.phone_number}</p>
        </div>
    );
};

export default UserProfile;
