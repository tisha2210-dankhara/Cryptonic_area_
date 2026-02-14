Project -1 
Project Name: Secure Web Application
Purpose: First cybersecurity internship project – show how to build a real secure login system instead of just finding bugs.

Main Features / Security Done:

Register + Login system
Password never saved in plain text → PBKDF2 hashing (very strong, 600,000 rounds)
Password must be strong: 8+ chars, 1 uppercase, 1 number, 1 special character
Session management (user stays logged in safely)
Dashboard only visible after login (access control)
Modern UI with Bootstrap 5 (gradient background, nice cards, responsive)
Flash messages for success/error
SQLite database (users.db) – only username + hashed password saved

Tech Used:

Flask (Python web framework)
Werkzeug (for hashing)
Bootstrap 5 + Bootstrap Icons
Git + GitHub
