# Project-1: Secure Web Application

**First Cybersecurity Internship Project**  
Building a real secure login system instead of just finding bugs

## Project Purpose
To demonstrate how to create a **secure web application** from scratch, focusing on authentication, password protection, session handling, and access control.

## Key Features & Security Highlights

- **Register + Login System** – Full authentication flow
- **Strong Password Hashing** – Never stored in plain text  
  → PBKDF2 (600,000 iterations + salt) using Werkzeug
- **Password Policy Enforcement**  
  → Minimum 8 characters  
  → At least 1 uppercase letter  
  → At least 1 number  
  → At least 1 special character (!@#$%^&*)
- **Session Management** – Safe login persistence using Flask sessions
- **Access Control** – Dashboard visible only after login
- **Modern & Responsive UI** – Built with Bootstrap 5  
- **User Feedback** – Flash messages (green success / red error alerts)
- **Database** – SQLite (`users.db`)  
  → Stores only username + hashed password (no plain text)

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Security**: Werkzeug (PBKDF2 hashing)
- **Frontend**: Bootstrap 5 + Bootstrap Icons
- **Database**: SQLite
- **Version Control**: Git + GitHub

