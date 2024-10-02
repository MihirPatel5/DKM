import React, { useState, useEffect } from 'react';
import axios from 'axios';

const InventoryItemList = ({ projectId }) => {
    const [items, setItems] = useState([]);

    useEffect(() => {
        const fetchInventoryItems = async () => {
            try {
                const token = localStorage.getItem('access_token');
                const response = await axios.get(`http://127.0.0.1:8000/projects/${projectId}/inventory-items/`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    }
                });
                setItems(response.data);
            } catch (error) {
                console.error("Error fetching inventory items:", error);
            }
        };
        
        fetchInventoryItems();
    }, [projectId]);

    return (
        <div>
            <h2>Inventory Items</h2>
            <ul>
                {items.map(item => (
                    <li key={item.id}>{item.name} - {item.quantity}</li>
                ))}
            </ul>
        </div>
    );
};

export default InventoryItemList;
