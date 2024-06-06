import React, { useState } from 'react';
import axios from 'axios';

const TicketSearch = () => {
  const [departureDate, setDepartureDate] = useState('');
  const [departureStation, setDepartureStation] = useState('');
  const [arrivalStation, setArrivalStation] = useState('');
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await axios.get('/api/tickets/search', {
        params: {
          date: departureDate,
          departure: departureStation,
          arrival: arrivalStation,
        },
      });
      setTickets(response.data);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Search Tickets</h1>
      <form onSubmit={handleSearch}>
        <div>
          <label htmlFor="date">Departure Date:</label>
          <input
            type="date"
            id="date"
            value={departureDate}
            onChange={(e) => setDepartureDate(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="departure">Departure Station:</label>
          <input
            type="text"
            id="departure"
            value={departureStation}
            onChange={(e) => setDepartureStation(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="arrival">Arrival Station:</label>
          <input
            type="text"
            id="arrival"
            value={arrivalStation}
            onChange={(e) => setArrivalStation(e.target.value)}
          />
        </div>
        <button type="submit">Search</button>
      </form>

      {loading && <div>Loading...</div>}
      {error && <div>Error: {error}</div>}

      <ul>
        {tickets.map((ticket) => (
          <li key={ticket.id}>
            <div>
              <strong>Ticket ID:</strong> {ticket.id}
            </div>
            <div>
              <strong>Fare ID:</strong> {ticket.fare_id}
            </div>
            <div>
              <strong>Company ID:</strong> {ticket.company_id}
            </div>
            <div>
              <strong>Trip ID:</strong> {ticket.trip ? ticket.trip.id : 'No trip assigned'}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TicketSearch;
