import { Link } from "react-router-dom";
import "./Layout.css";

const Layout = ({ children }) => {
    return (
        <div>
            <nav>
                <ul>
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/CssPositions">Css Positions</Link></li>
                    <li><Link to="/ContactForm">Contact Form</Link></li>
                    <li><Link to="/CssVanity">Css Vanity</Link></li>
                    <li><Link to="/ImagePage">Images</Link></li>
                    <li><Link to="/login">Login</Link></li>
                    <li><Link to="/javascipt">JavaScript</Link></li>
                    <li class="dropdown">
                        <a href="." class="dropbtn">Dropdown</a>
                        <div class="dropdown-content">
                        <a href=".">Link 1</a>
                        <a href=".">Link 2</a>
                        <a href=".">Link 3</a>
                        </div>
                    </li>
                </ul>
            </nav>
            <main>
                {children} 
            </main>
        </div>
    );
};

export default Layout;