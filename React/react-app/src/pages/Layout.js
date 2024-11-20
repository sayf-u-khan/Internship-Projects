import { Link } from "react-router-dom";

const Layout = ({ children }) => {
    return (
        <div>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/CssPositions">CssPositions</Link></li>
                    <li><Link to="/ContactForm">ContactForm</Link></li>
                    <li><Link to="/CssVanity">CssVanity</Link></li>
                </ul>
            </nav>
            <main>
                {children} 
            </main>
        </div>
    );
};

export default Layout;