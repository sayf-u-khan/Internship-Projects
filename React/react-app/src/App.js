// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes} from 'react-router-dom'; // Import necessary components
import Layout from './pages/Layout';
import MyFirstComponent from './components/my_first_component/MyFirstComponent';
import ContactForm from './components/contact_form/ContactForm';
import CssDemo from './components/css_demo/CssDemo';
import CssVanity from './components/css_vanity/CssVanity';
import ImagePage from './components/image_page/ImagePage';
import Login from './components/login_page/login'
import Javascript from './components/javascript/javascript';
import Calculator from './components/calculator/calculator';
import UserProfile from './components/profile/profile-code';
import Python from './pages/Python';

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
                    <Route path="/calculator" element={<Calculator />} />
                    <Route path="/profile" element={<UserProfile />} />
                    <Route path='/python' element={<Python />} />
                </Routes>
            </Layout>
        </Router>
    );
}

export default App;