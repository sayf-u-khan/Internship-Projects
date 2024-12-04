import './login.css'

const login = () => {
    return (
        <div className="logincontainer">
            <div className="login-form">
                <h2>Login</h2>
                <form>
                    <div className="form-group">
                        <label htmlFor="username">Username</label>
                        <input type="text" id="username" name="username" required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" id="password" name="password" required />
                    </div>
                    <button className='loginbutton' type="submit">Login</button>
                </form>
            </div>
        </div>
    );
};

export default login;