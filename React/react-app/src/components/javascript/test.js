import {useEffect} from "react";

const Test1 = () => {
    useEffect(() => {
        const displayCars = () => {
            fetch('/cars.json')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json();
                })
                .then(data => {
                    const cars = data.availableCars;
                    const text = cars.join("<br>");
                    document.getElementById("carList").innerHTML = text;
                })
                .catch(error => {
                    console.error('Error fetching car data:', error);
                });
        };

        displayCars();
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