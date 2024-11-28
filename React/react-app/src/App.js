// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'; // Import necessary components
import Layout from './pages/Layout';
import MyFirstComponent from './components/MyFirstComponent';
import ContactForm from './components/ContactForm';
import CssDemo from './components/CssDemo';
import CssVanity from './components/CssVanity';
import ImagePage from './components/ImagePage';
import Login from './components/login'
import Javascript from './pages/Javascript';

function App() {
    return (
        <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<MyFirstComponent />} />
                    <Route path="/ContactForm" element={<ContactForm />} />
                    <Route path="/CssPositions" element={<CssDemo />} />
                    <Route path="/CssVanity" element={<CssVanity />} />
                    <Route path="/ImagePage" element={<ImagePage />} />
                    <Route path="/login" element={<Login />} />
                    <Route path="/javascript" element={<Javascript />} />
                </Routes>
            </Layout>
        </Router>
    );
}

export default App;