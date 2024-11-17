import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

const FlightBookingSystem = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showDropdown, setShowDropdown] = useState(false);

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token) {
            setIsLoggedIn(true);
        }
    }, []);

    const handleLogout = () => {
        localStorage.removeItem('token');
        setIsLoggedIn(false);
    };

    const toggleDropdown = () => {
        setShowDropdown(!showDropdown);
        document.querySelector('.drop-menu').classList.toggle('hidden');
    };

    return (
        <>
        <nav className="bg-[#0c1523] text-white p-4 fixed top-0 w-full h-[70px]">
            <div className="container mx-auto flex justify-between fixed">
                <h1 className="text-2xl">Flight Booking System</h1>
                <ul className="flex items-center mr-4">
                    {!isLoggedIn && (
                        <>
                            <li className="mr-10 px-2 rounded border bottom-5 border-primary"><a href="/login">Login</a></li>
                            <li className="mr-10 px-2 rounded border bottom-5"><a href="/register">Register</a></li>
                        </>
                    )}
                    {isLoggedIn && (
                        <>
                            <li className="mr-10 border bottom-3 border-white"><a href="/flights">Search Flights</a></li>
                            <li className="mr-10 relative">
                                <a  
                                    onClick={toggleDropdown}
                                    className="cursor-pointer"
                                >
                                    Profile
                                </a>
                                <ul className="drop-menu absolute hidden group-hover:block bg-gray-800 text-white rounded-md mt-2 ml-[-100px] w-42">
                                    <div className='h-[10px] w-[10px] rotate-45 bg-gray-800 absolute top-[-5px] right-2 -z-10'></div>
                                    <li className="px-4 py-2 hover:bg-gray-700"><a href="/booked-flights">Booked Flights</a></li>
                                    <li className="px-4 py-2 hover:bg-gray-700"><a href="/services">Services</a></li>
                                    <li className="px-4 py-2 hover:bg-gray-700"><a href="/reviews">Reviews</a></li>
                                    <li className="px-4 py-2 hover:bg-gray-700"><a href="/notifications">Notifications</a></li>
                                    <li className="px-4 py-2 hover:bg-gray-700"><a href="/logout" onClick={handleLogout}>Logout</a></li>
                                </ul>
                            </li>
                        </>
                    )}
                </ul>
            </div>
        </nav>
        </>
    );
};

export default FlightBookingSystem;


