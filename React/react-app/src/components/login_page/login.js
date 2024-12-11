import './login.css'

const login = () => {
    return (
        <div className="logincontainer">
            <div className="login-form">
                <h2 class='loginh2'>Login</h2>
                <form>
                    <div className="form-group">
                        <label class='loginlabel' htmlFor="username">Username</label>
                        <input class='logininput' type="text" id="username" name="username" required />
                    </div>
                    <div className="form-group">
                        <label class='loginlabel' htmlFor="password">Password</label>
                        <input class='logininput' type="password" id="password" name="password" required />
                    </div>
                    <button className='loginbutton' type="submit">Login</button>
                </form>
            </div>
        </div>
    );
};

export default login;