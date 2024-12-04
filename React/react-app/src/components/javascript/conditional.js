import React, { useEffect, useState } from 'react';

const CarAvailability = () => {
    const [availableCars, setAvailableCars] = useState([]);
    const [carToCheck, setCarToCheck] = useState("BMW");
    const [message, setMessage] = useState("");

    useEffect(() => {
        // Fetch available cars from the JSON file
        fetch('/cars.json')
            .then(response => response.json())
            .then(data => {
                setAvailableCars(data.availableCars);
            })
            .catch(error => {
                console.error('Error fetching car data:', error);
            });
    }, []);

    useEffect(() => {
        // Check if the car is available
        if (availableCars.includes(carToCheck)) {
            setMessage(`${carToCheck} is available!`);
        } else {
            setMessage(`${carToCheck} is not available.`);
        }
    }, [availableCars, carToCheck]);

    return (
        <div>
            <h2>Car Availability Check</h2>
            <input 
                type="text" 
                value={carToCheck} 
                onChange={(e) => setCarToCheck(e.target.value)} 
                placeholder="Enter car name" 
            />
            <p>Checking availability for: {carToCheck}</p>
            <p>{message}</p>
        </div>
    );
};

export default CarAvailability;