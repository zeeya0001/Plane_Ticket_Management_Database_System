import React from 'react';
import plane from '../../Assets/airplane-svg.svg';

const FlightBookingSystem = () => {
    return (
        <div className="min-h-screen flex items-center justify-center bg-gray-900">
            <div className="container mx-auto flex items-center justify-around ">
                <div className="bg-white/10 backdrop-blur-md rounded-2xl shadow-xl p-8 border border-white/20 max-w-lg">
                    <form action="/flight_get" method="GET" className="space-y-6">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label htmlFor="from" className="block text-white mb-2 font-medium">From</label>
                                <input type="text"
                                    className="w-full bg-white/5 border border-white/20 rounded-lg p-3 text-white placeholder-white/50 focus:ring-2 focus:ring-blue-400 focus:border-transparent"
                                    id="from" name="from" placeholder="Departure City" required />
                            </div>
                            <div>
                                <label htmlFor="to" className="block text-white mb-2 font-medium">To</label>
                                <input type="text"
                                    className="w-full bg-white/5 border border-white/20 rounded-lg p-3 text-white placeholder-white/50 focus:ring-2 focus:ring-blue-400 focus:border-transparent"
                                    id="to" name="to" placeholder="Arrival City" required />
                            </div>
                        </div>
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                            <div>
                                <label htmlFor="date" className="block text-white mb-2 font-medium">Date</label>
                                <input type="date"
                                    className="w-full bg-white/5 border border-white/20 rounded-lg p-3 text-white focus:ring-2 focus:ring-blue-400 focus:border-transparent"
                                    id="date" name="date" required />
                            </div>
                            <div>
                                <label htmlFor="passengers" className="block text-white mb-2 font-medium">Passengers</label>
                                <input type="number"
                                    className="w-full bg-white/5 border border-white/20 rounded-lg p-3 text-white focus:ring-2 focus:ring-blue-400 focus:border-transparent"
                                    id="passengers" name="passengers" min="1" placeholder="Number of passengers" required />
                            </div>
                        </div>
                        <button type="submit"
                            className="w-full bg-gradient-to-r from-blue-500 to-indigo-500 text-white p-4 rounded-lg hover:from-blue-600 hover:to-indigo-600 transition duration-300 font-medium text-lg mt-6">
                            Search Flights
                        </button>
                    </form>
                </div>
            <img src={plane} alt="Airplane" className="w-[300px] h-[300px] object-cover mr-16" />
            </div>
        </div>
    );
};

export default FlightBookingSystem;

