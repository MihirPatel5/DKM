import React, { useState } from 'react';
import api from '../../api';

const RegisterUser = () => {
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await api.post('/user/', {
        email,
        username,
        first_name: firstName,
        last_name: lastName,
        phone_number: phoneNumber,
      });
      setSuccessMessage(`User registered successfully. Login credentials have been sent to ${email}`);
      setEmail('');
      setUsername('');
      setFirstName('');
      setLastName('');
      setPhoneNumber('');
    } catch (error) {
      setError('User registration failed. Please try again.');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Register New User</h2>
      {successMessage && <div className="alert alert-success">{successMessage}</div>}
      {error && <div className="alert alert-danger">{error}</div>}
      <form onSubmit={handleRegister}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          className="form-control mb-3"
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          className="form-control mb-3"
        />
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          required
          className="form-control mb-3"
        />
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          required
          className="form-control mb-3"
        />
        <input
          type="text"
          placeholder="Phone Number"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
          required
          className="form-control mb-3"
        />
        <button type="submit" className="btn btn-primary">Register</button>
      </form>
    </div>
  );
};

export default RegisterUser;
