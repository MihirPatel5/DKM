import React, { useState } from 'react';
import axios from 'axios';

const CreateProject = () => {
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [error, setError] = useState('');
    const [success, setSuccess] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('access_token');
            await axios.post('http://127.0.0.1:8000/projects/', { name, description }, {
                headers: {
                    Authorization: `Bearer ${token}`,
                }
            });
            setSuccess('Project created successfully');
        } catch (error) {
            setError('Failed to create project');
        }
    };

    return (
        <div>
            <h2>Create Project</h2>
            <form onSubmit={handleSubmit}>
                <input 
                    type="text" 
                    placeholder="Project Name" 
                    value={name} 
                    onChange={(e) => setName(e.target.value)} 
                />
                <textarea 
                    placeholder="Description" 
                    value={description} 
                    onChange={(e) => setDescription(e.target.value)} 
                />
                <button type="submit">Create</button>
            </form>
            {error && <p>{error}</p>}
            {success && <p>{success}</p>}
        </div>
    );
};

export default CreateProject;
