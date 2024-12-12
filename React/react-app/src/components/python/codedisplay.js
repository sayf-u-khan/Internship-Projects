import React, { useEffect, useState } from 'react';

const CodeDisplay = () => {
    const [message, setMessage] = useState('');

    const fetchMessage = async () => {
        const response = await fetch('http://localhost:8000/code');
        const data = await response.json();
        setMessage(data.message);

        setTimeout(() => {
            setMessage('');
        }, 5000);
    };

    return (
        <div>
            <h2>Click the button to get a message!</h2>
            <button onClick={fetchMessage} style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer', backgroundColor: 'violet'}}>
                Get Message
            </button>
            {message && <p style={{ marginTop: '20px', fontSize: '18px', color: '#ff69b4' }}>{message}</p>}
        </div>
    );
};

export default CodeDisplay;