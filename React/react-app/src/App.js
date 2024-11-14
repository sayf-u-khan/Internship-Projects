// src/App.js
import React from 'react';
import './App.css';
import MyFirstComponent from './components/MyFirstComponent';
import ContactForm from './components/ContactForm';

function App() {
    return (
        <div className="App">
            <MyFirstComponent /> {/* Use your first component */}
            <ContactForm /> {/* Use your form component */}
        </div>
    );
}

export default App;

