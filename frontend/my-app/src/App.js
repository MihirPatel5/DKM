import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Components/Auth/Login.js";
// import Register from "./Components/Auth/Register";
import UserProfile from "./Components/Profile/UserProfile";
import ProjectList from "./Components/Projects/ProjectList";
import ProjectDetail from "./Components/Projects/ProjectDetail";
import CreateProject from "./Components/Projects/CreateProject";
import InventoryItemList from "./Components/Inventory/InventoryItemList";
import ProtectedRoute from "./Components/ProtectedRoute";
import AdminRoute from './Components/AdminRoute'; 
import RegisterUser from './Components/Auth/RegisterUser'; 
import Navbar from "./Components/Navbar";
import Footer from "./Components/Footer.js";

function App() {
  return (
    <Router>
            <Navbar />
            <div className="container mt-4">
                <Routes>
                    <Route path="/login" element={<Login />} />
                    <Route path="/profile" element={<ProtectedRoute><UserProfile /></ProtectedRoute>} />
                    <Route path="/projects" element={<ProtectedRoute><ProjectList /></ProtectedRoute>} />
                    <Route path="/projects/:id" element={<ProtectedRoute><ProjectDetail /></ProtectedRoute>} />
                    <Route path="/projects/create" element={<ProtectedRoute><CreateProject /></ProtectedRoute>} />
                    <Route path="/projects/:project_id/inventory-items" element={<ProtectedRoute><InventoryItemList /></ProtectedRoute>} />
                    
                    {/* Admin-Only Route */}
                    <Route path="/admin/register-user" element={<AdminRoute><RegisterUser /></AdminRoute>} />
                </Routes>
            </div>
            <Footer />
        </Router>
  );
}

export default App;
