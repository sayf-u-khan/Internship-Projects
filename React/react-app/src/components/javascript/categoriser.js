import React, { useEffect, useState } from 'react';

const CarCategoriser = () => {
    const [carInput, setCarInput] = useState('');
    const [carTypeCounts, setCarTypeCounts] = useState(new Map());
    const [message, setMessage] = useState('');

    // Effect to categorise cars whenever carInput changes
    useEffect(() => {
        if (carInput) {
            const carList = carInput.split(',').map(car => car.trim());
            const counts = new Map();
            let unknownCars = [];

            for (let car of carList) {
                switch (car) {
                    case 'Mercedes':
                    case 'Audi':
                        counts.set('Luxury', (counts.get('Luxury') || 0) + 1);
                        break;

                    case 'Toyota':
                    case 'Honda':
                    case 'Volvo':
                        counts.set('Economy', (counts.get('Economy') || 0) + 1);
                        break;
                    
                    case 'MG':
                        counts.set('Electric', (counts.get('Electric') || 0) + 1);
                        break;

                    case 'BMW':
                        counts.set('Luxury', (counts.get('Luxury') || 0) + 1);
                        counts.set('Electric', (counts.get('Electric') || 0) + 1);
                        break;

                    default:
                        unknownCars.push(car);
                        continue; // Skip to the next iteration
                }
            }

            setCarTypeCounts(counts);
            setMessage(unknownCars.length > 0 ? `Unknown car types: ${unknownCars.join(', ')}` : '');
        } else {
            setCarTypeCounts(new Map()); // Reset counts if input is empty
            setMessage('');
        }
    }, [carInput]); // Run this effect when carInput changes

    return (
        <div>
            <h2>Car Categoriser</h2>
            <input
                type="text"
                value={carInput}
                onChange={(e) => setCarInput(e.target.value)}
                placeholder="Enter car brands separated by commas"
            />
            <p>{message}</p>
            <h3>Car Type Counts:</h3>
            <ul>
                {Array.from(carTypeCounts.entries()).map(([type, count]) => (
                    <li key={type}>{type}: {count}</li>
                ))}
            </ul>
        </div>
    );
};

export default CarCategoriser;