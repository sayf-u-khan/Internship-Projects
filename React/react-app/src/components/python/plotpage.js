import React, { useEffect, useState } from 'react';
import axios from 'axios';

const PlotPage = () => {
    const [plotUrl, setPlotUrl] = useState('');

    useEffect(() => {
        const fetchPlot = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/plot', {
                    responseType: 'blob',
                });
                const url = URL.createObjectURL(new Blob([response.data]));
                setPlotUrl(url);
            } catch (error) {
                console.error('Error fetching the plot:', error);
            }
        };

        fetchPlot();
    }, []);

    return (
        <div>
            <h2>Iris Sepal Length vs Width Plot</h2>
            {plotUrl ? (
                <img src={plotUrl} alt="Iris Plot" />
            ) : (
                <p>Loading plot...</p>
            )}
        </div>
    );
};

export default PlotPage;