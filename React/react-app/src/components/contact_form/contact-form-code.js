import React, { useState } from 'react';

const Contactform = () => {
    const [name, setName] = useState('');
    const [feedback, setFeedback] = useState('');
    const [easterEggMessage, setEasterEggMessage] = useState('');
    const [ageRange, setAgeRange] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Name:', name);
        console.log('Feedback:', feedback);
        alert('Thank you for your feedback!');
    };

    const handleFeedbackChange = (e) => {
        const value = e.target.value;
        setFeedback(value);

        if (value.includes("El Psy Kongroo")) {
            setEasterEggMessage("You've unlocked a secret! Remember, the past is not a straight line. 😉");
        } else {
            setEasterEggMessage('');
        }
    };

    return (
        <div className="survey-form-container">
            <h2 className="survey-title">Feedback Survey</h2>
            <form className="survey-form" onSubmit={handleSubmit}>
                <div className="form-group">
                    <label className="form-label" htmlFor="name">Name:</label>
                    <input
                        className="form-input"
                        type="text"
                        id="name"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        required
                    />
                    <label className="form-label" htmlFor="ageRange">Age Range:</label>
                    <select
                        className="form-input"
                        id="ageRange"
                        value={ageRange}
                        onChange={(e) => setAgeRange(e.target.value)}
                        required
                    >
                        <option value="">Select your age range</option>
                        <option value="under_18">Under 18</option>
                        <option value="18_24">18-24</option>
                        <option value="25_34">25-34</option>
                        <option value="35_44">35-44</option>
                        <option value="45_54">45-54</option>
                        <option value="55_64">55-64</option>
                        <option value="65_plus">65 and above</option>
                    </select>
                </div>
                <div className="form-group">
                    <label className="form-label" htmlFor="feedback">Feedback:</label>
                    <textarea
                        className="form-textarea"
                        id="feedback"
                        value={feedback}
                        onChange={handleFeedbackChange}
                        required
                    ></textarea>
                </div>
                {easterEggMessage && <div className="easter-egg-message">{easterEggMessage}</div>}
                <button className="form-button" type="submit">Submit</button>
            </form>
        </div>
    );
};


export default Contactform;