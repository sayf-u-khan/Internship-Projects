import React, { useState } from 'react';

const DataAnalysis = () => {
    const [data, setData] = useState('');
    const [result, setResult] = useState(null);
    const [plot, setPlot] = useState(null);

    const analyseData = async () => {
        const dataArray = data.split(',').map(Number);
        const response = await fetch('http://localhost:8000/analyse-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dataArray),
        });
        const analysisResult = await response.json();
        setResult(analysisResult);
        setPlot(analysisResult.plot);
    };

    return (
        <div>
            <h2>Data Analysis</h2>
            <input
                type="text"
                placeholder="Enter numbers separated by commas"
                value={data}
                onChange={(e) => setData(e.target.value)}
            />
            <button onClick={analyseData}>Analyse Data</button>
            {result && (
                <div>
                    <h3>Analysis Result:</h3>
                    <p>Mean: {result.mean}</p>
                    <p>Median: {result.median}</p>
                    <p>Standard Deviation: {result.std_dev}</p>
                </div>
            )}
            {plot && <img src={plot} alt="Scatter Plot" style={{ marginTop: '20px' }} />}
        </div>
    );
};

export default DataAnalysis;