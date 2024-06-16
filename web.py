# auth.py
import streamlit as st
import streamlit_authenticator as stauth
import sqlite3
import hashlib

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# Initialize database
def init_db():
    conn = get_db_connection()
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                name TEXT,
                hashed_password TEXT,
                email TEXT,
                health_data TEXT
            )
        ''')
    conn.close()

# Add user
def add_user(username, name, password, email):
    conn = get_db_connection()
    hashed_password = hash_password(password)
    with conn:
        conn.execute('INSERT INTO users (username, name, hashed_password, email) VALUES (?, ?, ?, ?)',
                     (username, name, hashed_password, email))
    conn.close()

# Authenticate user
def authenticate_user(username, password):
    conn = get_db_connection()
    hashed_password = hash_password(password)
    user = conn.execute('SELECT * FROM users WHERE username = ? AND hashed_password = ?', (username, hashed_password)).fetchone()
    conn.close()
    return user

# Get user profile
def get_user_profile(username):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user

# Initialize the database
init_db()



# app.py
import streamlit as st


st.title("Diabetic Retinopathy Detection")

# Sidebar for user authentication
st.sidebar.title("User Authentication")

# Tabs for login and signup
tab1, tab2 = st.sidebar.tabs(["Login", "Sign Up"])

with tab1:
    st.subheader("Login")
    login_username = st.text_input("Username", key="username")
    login_password = st.text_input("Password", type="password", key="password")
    login_button = st.button("Login")
    
    if login_button:
        user = authenticate_user(login_username, login_password)
        if user:
            st.success(f"Welcome, {user[2]}!")
            st.session_state.logged_in = True
            st.session_state.username = user[1]
        else:
            st.error("Invalid username or password")

with tab2:
    st.subheader("Sign Up")
    signup_name = st.text_input("Full Name", key="fullname")
    signup_username = st.text_input("Username", "username")
    signup_password = st.text_input("Password", type="password", key="password")
    signup_email = st.text_input("Email", key="email")
    signup_button = st.button("Sign Up")
    
    if signup_button:
        try:
            add_user(signup_username, signup_name, signup_password, signup_email)
            st.success("Account created successfully!")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Main content
if 'logged_in' in st.session_state and st.session_state.logged_in:
    st.header("User Profile")
    
    user_profile = get_user_profile(st.session_state.username)
    st.write(f"Name: {user_profile[2]}")
    st.write(f"Email: {user_profile[4]}")
    
    # Placeholder for health data management
    st.write("Manage your health data here...")
else:
    st.write("Please login or sign up to access the application.")
