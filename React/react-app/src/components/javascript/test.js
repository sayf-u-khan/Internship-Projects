import {useEffect} from "react";

const Test1 = () => {
    useEffect(() => {
        // Define the displayCars function inside the useEffect
        const displayCars = () => {
            // Fetch available cars from the JSON file
            fetch('/cars.json') // Ensure this path is correct
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const cars = data.availableCars; // Get the car list from the JSON data
                    const text = cars.join("<br>"); // Join car names with line breaks
                    document.getElementById("carList").innerHTML = text; // Insert into the DOM
                })
                .catch(error => {
                    console.error('Error fetching car data:', error);
                });
        };

        displayCars(); // Call the function when the component mounts
    }, []);

    return (
        <div>
            <h2>JavaScript Practice in React</h2>
            <p>This is using standard js code in a react component</p>
            <p>Car list:</p>
            <div id="carList"></div>
        </div>
    );
};

export default Test1;