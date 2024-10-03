import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../api';

const CreateProject = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const navigate = useNavigate();

    const handleCreateProject = async (e) => {
        e.preventDefault();
        try {
            await api.post('/projects/', { name, description, user_id: localStorage.getItem('user_id') });
            alert('Project created successfully!');
            navigate('/projects');
        } catch (error) {
            console.error('Error creating project:', error);
        }
    };

    return (
        <div className="container mt-4">
            <h2>Create Project</h2>
            <form onSubmit={handleCreateProject}>
                <input
                    type="text"
                    placeholder="Project Name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                    className="form-control mb-3"
                />
                <textarea
                    placeholder="Project Description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    required
                    className="form-control mb-3"
                />
                <button type="submit" className="btn btn-primary">Create Project</button>
            </form>
        </div>
    );
};

export default CreateProject;
