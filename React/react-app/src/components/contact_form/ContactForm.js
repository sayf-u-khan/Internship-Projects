// src/components/ContactForm.js
import React, { useState } from 'react';

const ContactForm = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        message: '',
        gender: '',
        age: '',
        subscribe: false,
    });

    const handleChange = (e) => {
        const { name, value, type, checked } = e.target;
        setFormData({
            ...formData,
            [name]: type === 'checkbox' ? checked : value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle form submission logic here (e.g., send data to an API)
        console.log('Form submitted:', formData);
        // Reset form after submission
        setFormData({
            name: '',
            email: '',
            message: '',
            gender: '',
            age: '',
            subscribe: false,
        });
    };

    return (
        <form onSubmit={handleSubmit}>
            <h1>Contact Us</h1>
            <label htmlFor="name">Name:</label>
            <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
            />
            <br /><br />

            <label htmlFor="email">Email:</label>
            <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <br /><br />

            <label htmlFor="message">Message:</label>
            <textarea
                id="message"
                name="message"
                rows="4"
                value={formData.message}
                onChange={handleChange}
                required
            />
            <br /><br />

            <label>Gender:</label>
            <input
                type="radio"
                id="male"
                name="gender"
                value="male"
                checked={formData.gender === 'male'}
                onChange={handleChange}
            />
            <label htmlFor="male">Male</label>
            <input
                type="radio"
                id="female"
                name="gender"
                value="female"
                checked={formData.gender === 'female'}
                onChange={handleChange}
            />
            <label htmlFor="female">Female</label>
            <br /><br />

            <label htmlFor="age">Age:</label>
            <select
                id="age"
                name="age"
                value={formData.age}
                onChange={handleChange}
            >
                <option value="">Select Age</option>
                <option value="under18">Under 18</option>
                <option value="18-25">18-25</option>
                <option value="26-35">26-35</option>
                <option value="36-45">36-45</option>
                <option value="46-60">46-60</option>
                <option value="60plus">60+</option>
            </select>
            <br /><br />

            <label htmlFor="subscribe">
                <input
                    type="checkbox"
                    id="subscribe"
                    name="subscribe"
                    checked={formData.subscribe}
                    onChange={handleChange}
                />
                Subscribe to newsletter
            </label>
            <br /><br />

            <button type="submit">Submit</button>
        </form>
    );
};

export default ContactForm;