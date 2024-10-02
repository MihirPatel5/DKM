// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './Components/Auth/Login.js';
import Register from './Components/Auth/Register';
import UserProfile from './Components/Profile/UserProfile';
import ProjectList from './Components/Projects/ProjectList';
import ProjectDetail from './Components/Projects/ProjectDetail';
import CreateProject from './Components/Projects/CreateProject';
import InventoryItemList from './Components/Inventory/InventoryItemList';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="/projects" element={<ProjectList />} />
        <Route path="/projects/:id" element={<ProjectDetail />} />
        <Route path="/projects/new" element={<CreateProject />} />
        <Route path="/inventory" element={<InventoryItemList />} />
      </Routes>
    </Router>
  );
};

export default App;
