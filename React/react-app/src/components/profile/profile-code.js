import React, { useState } from 'react';
import styles from './profile-code.module.css';

const UserProfile = () => {
    const [name, setName] = useState('');
    const [title, setTitle] = useState('');
    const [bio, setBio] = useState('');
    const [interests, setInterests] = useState('');
    const [image, setImage] = useState('');
    const [showProfile, setShowProfile] = useState(false);
    const [formVisible, setFormVisible] = useState(true); // New state variable

    const handleSubmit = (event) => {
        event.preventDefault();
        setShowProfile(true);
        setFormVisible(false); // Hide the form after generating the profile
    };

    const interestList = interests.split(',').map((interest, index) => (
        <li key={index}>{interest.trim()}</li>
    ));

    const handleEditProfile = () => {
        // Reset the form and show it again
        setName('');
        setTitle('');
        setBio('');
        setInterests('');
        setImage('');
        setShowProfile(false);
        setFormVisible(true);
    };

    return (
        <div className={styles.container}>
            {formVisible && (
            <div>
                <header className={styles.header}>
                    <h1>User Profile Generator</h1>
                </header><div className={styles.formContainer}>
                        <h2>Enter Your Information</h2>
                        <form onSubmit={handleSubmit}>
                            <label htmlFor="name">Name:</label>
                            <input type="text" id="name" value={name} onChange={(e) => setName(e.target.value)} required />

                            <label htmlFor="title">Title:</label>
                            <input type="text" id="title" value={title} onChange={(e) => setTitle(e.target.value)} required />

                            <label htmlFor="bio">About Me:</label>
                            <textarea id="bio" value={bio} onChange={(e) => setBio(e.target.value)} required />

                            <label htmlFor="interests">Interests (comma-separated):</label>
                            <input type="text" id="interests" value={interests} onChange={(e) => setInterests(e.target.value)} required />

                            <label htmlFor="image">Image URL:</label>
                            <input type="url" id="image" value={image} onChange={(e) => setImage(e.target.value)} required />

                            <button className={styles.profilebutton} type="submit">Generate Profile</button>
                        </form>
                    </div>
            </div>
            )}
            {showProfile && (
                <div className={styles.profile}>
                    <h2>Your Profile</h2>
                    <div className={styles.profileContent}>
                        <img src={image} alt="Profile" className={styles.profileImage} />
                        <div className={styles.bio}>
                            <h3>{name}</h3>
                            <p>{title}</p>
                            <p>{bio}</p>
                            <h4>Interests</h4>
                            <ul>{interestList}</ul>
                        </div>
                    </div>
                    <button onClick={handleEditProfile}>Create Another Profile</button>
                </div>
            )}
        </div>
    );
};

export default UserProfile;