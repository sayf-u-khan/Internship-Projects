# Internship Projects - Comprehensive Documentation

## Overview
This repository contains projects developed during my internship at SeQuenX. It showcases a collection of applications, including:

- A Django-powered backend for user management and API capabilities.
- A React-based frontend app providing a responsive user interface.
- A FastAPI app serving as the integration point for Python logic within the React app.

### Project Structure
- **Backend (Django)**: Contains the core server logic and user management.
- **Frontend (React)**: A responsive user interface with its own standalone functionality.
- **Integration (FastAPI)**: Provides API endpoints consumed by the React frontend for specific Python logic.
- **Other folders**: Supporting files such as `requirements.txt`, `.env`, and `.gitignore` for environment configuration and dependency management.

---

## Backend - Django App

### Features
1. **User Management**:
   - User registration with email and password.
   - Secure login using Django’s built-in authentication.
   - Profile management: Edit fields such as name, email, phone number, and profile picture.

2. **API Design**:
   - Built with Django REST Framework (DRF).
   - Endpoints:
     - `POST /api/user/UserRegisterView/`: Register a new user.
     - `POST /api/token/`: Authenticate user and retrieve a token.
     - `GET /api/session/CurrentUserView/`: Fetch current logged in user.
     - `GET /api/user/find-users-by-first-name/`: Fetch all information on a user by searching their first name.
     - `PUT /api/user/EditPhoneNumber/`: Update the users' phone number.
     - `POST /api/session/UserSessionLoginView/`: Logs in a selected user.
     - `POST /api/session/UserLogoutView/`: Logs current active user out.

3. **Database**:
   - Uses mySQL for local development - experimented with S3 buckets but did not succeed.
   - Custom django models for User and Profile.

4. **Validation and Security**:
   - Input validation via DRF serializers.
   - Secure token-based authentication.
  
5. **Unit Tested**:
   - Completed a fairly comprehensive set of unit tests going over many cases:
      - Invalid user credentials such as email or password.
      - Failing validation when registering a user such as incorrect phone number format.
      - Missing fields when logging in or registering a user.
      - Logging in an inactive user.
      - Password 1 and 2 do not match in registration.
    - Test coverage was over 65%, sitting at around 69-73% overall.

7. **Development Setup**:
   - Install dependencies: `pip install -r requirements.txt`
   - Run migrations: `python manage.py migrate`
   - Start the server: `python manage.py runserver`

### Tasks Completed
- Initialized the Django project and set up a virtual environment.
- Designed user models and implemented registration and login functionality.
- Created validation logic for fields including custom validators for passwords and phone numbers.
- Configured the Django REST Framework for building APIs.
- Fixed authentication issues between custom and default Django models.
- Researched and resolved issues with JWT authentication clashing with Django's default authentication.
- Integrated Swagger for API documentation.
- Experimented with deployment via AWS. Used Elastic Beanstalk and ECS but ran into compatibility issues with their virtual linux systems.

### Key Files
- `settings.py`: Configurations for the Django project.
- `models.py`: Database models for the app.
- `views.py`: Logic for handling API requests.
- `serializers.py`: Transforming data between JSON and Python.

---

## Frontend - React App

### Features
1. **User Interface**:
   - Clean and responsive design using React and CSS.
   - Pages include:
     - Registration form
     - Login form
     - Profile editor
     - Calculator
     - Contact form
     - Javascript showcase
     - Python showcase

2. **API Integration**:
   - Interacts with the FastAPI backend for dynamic features.
   - Axios is used for making HTTP requests.

3. **Validation and Feedback**:
   - Frontend validation for forms.
   - Toast notifications for errors and successes.

4. **Development Setup**:
   - Install dependencies: `npm install`
   - Run the app: `npm start`

### Tasks Completed
- Set up GitHub and established the repository for the React project as well as for the django app too.
- Structured the React project with reusable components and organized pages.
- Built essential UI elements such as a navigation bar, login page, and registration form.
- Styled components using CSS features like gradients, shadows, and media queries.
- Added dynamic features like a working calculator and profile page generator.
- Resolved CSS scope and conflict issues.
- Integrated API calls for dynamic interaction with the FastAPI backend.

### Key Files
- `src/components`: Contains reusable UI components.
- `src/pages`: Contains page-specific components like Login and Profile.
- `src/context/AuthContext.js`: Authentication state management.
- `src/utils/api.js`: API interaction logic.

---

## Integration - FastAPI App

### Features
1. **Python Logic Integration with React**:
   - Provides specific functionality implemented in Python.
   - Exposes endpoints consumed by the React frontend for dynamic interactions on the 'Python' page in react.

2. **API Design**:
   - Endpoints:
     - `GET /plot HTTP/1.1`: Performs server-side computations and returns a plot of the results.

3. **Development Setup**:
   - Install dependencies: `pip install -r requirements.txt`
   - Run the server: `uvicorn main:app --reload`

### Tasks Completed
- Selected FastAPI as the web framework for Python integration for a lightweight app.
- Created API endpoints for computations and dynamic interactions with React.

### Key Files
- `main.py`: Entry point for the FastAPI app.
- `routes.py`: Contains API endpoint logic.
- `requirements.txt`: Dependencies for FastAPI.

---

## Deployment
1. **Backend (Django)**:
   - Use Gunicorn or uWSGI with Nginx for production.
   - Environment variables managed via `.env`.
   - Ensure static files are collected.

2. **Frontend (React)**:
   - Build for production using `npm run build`.
   - Serve static files through Nginx or a CDN.

3. **FastAPI**:
   - Deploy using Gunicorn or uvicorn in production mode.
   - Configure endpoints to serve through Nginx.

---

## Future Improvements
- Create a UI for the backend django app so there is a responsive frontend for users.
- Migrate to PostgreSQL for production and explore different options for databases.
- Work on deployment a little more to try and get it working properly.

---

## Acknowledgments
Special thanks to the team at SeQuenX for the opportunity to work on this project and for their guidance throughout the internship.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.



