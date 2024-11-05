# Box479 Team Management System

A Flask-based web application for managing team members and their profiles with secure authentication and role-based access control.

## Features

- User Authentication (Login/Register)
- Profile Management
  - View and edit personal profile
  - Phone number formatting
  - Last initial privacy
- Team Member Management
  - View all team members
  - Admin-only user deletion
  - Role-based access control
- Dark Theme UI using Bootstrap

## Tech Stack

- Flask (Python web framework)
- PostgreSQL (Database)
- Bootstrap 5 (UI framework with dark theme)
- SQLAlchemy (ORM)

## Project Structure

```
├── static/
│   ├── css/
│   │   └── custom.css
│   └── js/
│       └── main.js
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   └── edit_profile.html
├── app.py
├── forms.py
├── main.py
├── models.py
└── routes.py
```

## Setup Instructions

1. Make sure you have Python 3.x installed
2. Install the required dependencies:
   ```
   pip install flask flask-sqlalchemy flask-login flask-wtf
   ```
3. Set up environment variables:
   - `DATABASE_URL`: PostgreSQL database URL
   - `FLASK_SECRET_KEY`: Secret key for Flask sessions

4. Run the application:
   ```
   python main.py
   ```

## Environment Variables

The following environment variables are required:
- `DATABASE_URL`: PostgreSQL database connection string
- `FLASK_SECRET_KEY`: Secret key for Flask session management
- PostgreSQL Configuration:
  - `PGHOST`: Database host
  - `PGPORT`: Database port
  - `PGUSER`: Database user
  - `PGPASSWORD`: Database password
  - `PGDATABASE`: Database name

## User Roles

- **Admin**: Can view all team members and delete other users
- **Pump**: Team member with pump operator role
- **Laborer**: Team member with laborer role
- **Finisher**: Team member with finisher role

## Security Features

- Password hashing using Werkzeug
- CSRF protection
- Role-based access control
- Session management
- SQL injection prevention through SQLAlchemy
