import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../api';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('http://127.0.0.1:8000/login/', { email, password });
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            if (response.status === 200) {
                navigate('/');
            }
        } catch (error) {
            setError('Invalid email or password');
        }
    };

    return (
        <div className="d-flex justify-content-center align-items-center">
            <div className="col-md-6">
                <h2 className="mb-3">Login</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <input
                            type="email"
                            className="form-control"
                            placeholder="Email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <input
                            type="password"
                            className="form-control"
                            placeholder="Password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        />
                    </div>
                    <button type="submit" className="btn btn-primary w-100">Login</button>
                </form>
                {error && <p className="text-danger mt-3">{error}</p>}
            </div>
        </div>
    );
};

export default Login;
