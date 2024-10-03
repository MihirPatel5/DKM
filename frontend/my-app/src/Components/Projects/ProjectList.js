import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import api from '../../api';

const ProjectList = () => {
    const [projects, setProjects] = useState([]);

    useEffect(() => {
        const fetchProjects = async () => {
            try {
                const response = await api.get('/projects/');
                setProjects(response.data);
            } catch (error) {
                console.error('Error fetching projects:', error);
            }
        };
        fetchProjects();
    }, []);

    return (
        <div className="container mt-4">
            <h2>Your Projects</h2>
            <ul className="list-group">
                {projects.map((project) => (
                    <li key={project.id} className="list-group-item">
                        <Link to={`/projects/${project.id}`}>{project.name}</Link>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ProjectList;
