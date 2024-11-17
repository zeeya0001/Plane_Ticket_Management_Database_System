// src/services/api.js
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export const createPassenger = (data) => axios.post(`${API_BASE_URL}/passengers`, data);

export const getPassengers = () => axios.get(`${API_BASE_URL}/passengers`);

export const getPassengerById = (id) => axios.get(`${API_BASE_URL}/passengers/${id}`);

export const updatePassenger = (id, data) => axios.put(`${API_BASE_URL}/passengers/${id}`, data);

export const deletePassenger = (id) => axios.delete(`${API_BASE_URL}/passengers/${id}`);


// Similarly add functions for flights, bookings, services, etc.
