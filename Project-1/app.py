from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'tisha_super_secret_key_2026_change_this_in_real_project'  # Require for session

DB_FILE = "users.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    if 'username' in session:
        return f"Hello {session['username']}! <a href='/dashboard'>Dashboard</a> | <a href='/logout'>Logout</a>"
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.isdigit() for c in password) or not any(c in "!@#$%^&*()_+" for c in password):
            flash("Password is weak! 8+ chars, 1 capital, 1 number, 1 special mandatory")
            return redirect('/register')

        hashed = generate_password_hash(password, method='pbkdf2:sha256:600000')

        try:
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed))
            conn.commit()
            conn.close()
            flash("Registration successful! Now you can login")
            return redirect('/login')
        except sqlite3.IntegrityError:
            flash("Username already taken!")
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        conn.close()

        if result and check_password_hash(result[0], password):
            session['username'] = username                     #Start the sesion 
            flash(f"Welcome back, {username}! ")
            return redirect('/dashboard')
        else:
            flash("Wrong username or password!")
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:           # Access Control
        flash("Please Login First!")
        return redirect('/login')
    
    return render_template('dashboard.html', username=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("Successfully logged out!")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)