import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../../api';

const InventoryItemList = () => {
    const { project_id } = useParams();
    const [inventoryItems, setInventoryItems] = useState([]);

    useEffect(() => {
        const fetchInventoryItems = async () => {
            try {
                const response = await api.get(`/projects/${project_id}/inventory-items/`);
                setInventoryItems(response.data);
            } catch (error) {
                console.error('Error fetching inventory items:', error);
            }
        };
        fetchInventoryItems();
    }, [project_id]);

    return (
        <div className="container mt-4">
            <h2>Inventory Items</h2>
            <ul className="list-group">
                {inventoryItems.map((item) => (
                    <li key={item.id} className="list-group-item">
                        {item.name} - Quantity: {item.quantity}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default InventoryItemList;
