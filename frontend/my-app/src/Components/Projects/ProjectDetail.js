import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../../api';  // Import api as default

const ProjectDetail = () => {
  const { id } = useParams();
  const [project, setProject] = useState(null);

  useEffect(() => {
    const fetchProject = async () => {
      try {
        const response = await api.get(`projects/${id}/`);
        setProject(response.data);
      } catch (error) {
        console.error('Error fetching project details:', error);
      }
    };
    fetchProject();
  }, [id]);

  return (
    <div>
      <h2>Project Detail</h2>
      {project ? (
        <div>
          <p>Name: {project.name}</p>
          <p>Description: {project.description}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ProjectDetail;
