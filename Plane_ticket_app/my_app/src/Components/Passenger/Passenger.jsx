// src/pages/Passengers.js
import React, { useEffect, useState } from 'react';
import { getPassengers, createPassenger } from '../services/api';

function Passengers() {
  const [passengers, setPassengers] = useState([]);
  const [newPassenger, setNewPassenger] = useState({ name: '', age: '' });

  useEffect(() => {
    fetchPassengers();
  }, []);

  const fetchPassengers = async () => {
    const response = await getPassengers();
    setPassengers(response.data);
  };

  const handleAddPassenger = async (e) => {
    e.preventDefault();
    await createPassenger(newPassenger);
    fetchPassengers();
  };

  return (
    <div>
      <h1>Passengers</h1>
      <form onSubmit={handleAddPassenger}>
        <input
          type="text"
          placeholder="Name"
          value={newPassenger.name}
          onChange={(e) => setNewPassenger({ ...newPassenger, name: e.target.value })}
        />
        <input
          type="number"
          placeholder="Age"
          value={newPassenger.age}
          onChange={(e) => setNewPassenger({ ...newPassenger, age: e.target.value })}
        />
        <button type="submit">Add Passenger</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
          </tr>
        </thead>
        <tbody>
          {passengers.map((passenger) => (
            <tr key={passenger.id}>
              <td>{passenger.id}</td>
              <td>{passenger.name}</td>
              <td>{passenger.age}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Passengers;
