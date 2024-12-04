export function Car(props) {
    return <li>I am a {props.brand}</li>;
}

export function Garage() {
    const cars = [
        { id: 1, brand: 'Ford' },
        { id: 2, brand: 'BMW' },
        { id: 3, brand: 'Audi' }
    ];
    return (
        <div>
            <h3>Who lives in my garage?</h3>
            <ul>
                {cars.map((car) => <Car key={car.id} brand={car.brand} />)}
            </ul>
        </div>
    );
}
