import { Link } from "react-router-dom";
import "./Layout.css";

const Layout = ({ children }) => {
    return (
        <div>
            <nav>
                <ul class='ul1'>
                    <li class='li1'><Link to="/">Home</Link></li>
                    <li class='li1'><Link to="/CssPositions">Css Positions</Link></li>
                    <li class='li1'><Link to="/ContactForm">Contact Form</Link></li>
                    <li class='li1'><Link to="/CssVanity">Css Vanity</Link></li>
                    <li class='li1'><Link to="/ImagePage">Images</Link></li>
                    <li class='li1'><Link to="/login">Login</Link></li>
                    <li class='li1'><Link to="/JavaScript">JavaScript</Link></li>
                    <li class="dropdown li1">
                        <a href="." class="dropbtn">Dropdown</a>
                        <div class="dropdown-content">
                        <a href=".">Link 1</a>
                        <a href=".">Link 2</a>
                        <a href=".">Link 3</a>
                        </div>
                    </li>
                    <li class='li1'><Link to="/Calculator">Calculator</Link></li>
                    <li class='li1'><Link to="/Profile">Profile</Link></li>
                </ul>
            </nav>
            <main>
                {children} 
            </main>
            <footer>
                <p>Author: Sayf Khan</p>
                <p><a href="mailto:sayf.khan@sequenx.com">sayf.khan@sequenx.com</a></p>
            </footer>
        </div>
    );
};

export default Layout;