// src/App.js
import React from 'react';
import './App.css';
import MyFirstComponent from './components/MyFirstComponent';
import ContactForm from './components/ContactForm';
import CssDemo from './components/CssDemo';

function App() {
    return (
        <div className="App">
            <MyFirstComponent /> {/* Use your first component */}
            <ContactForm /> {/* Use your form component */}
            <CssDemo /> {/* Use your CSS demo component */}
        </div>
    );
}

export default App;

