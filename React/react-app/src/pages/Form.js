import React from 'react';
import './Form.css';
import ContactForm from './components/ContactForm';

function Form() {
    return (
        <div className="Form">
            <ContactForm /> {/* Use your first component */}
        </div>
    );
}

export default Form;