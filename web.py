import streamlit as st
import sqlite3
import hashlib
import numpy as np
import pandas as pd
from PIL import Image
import time

# Database functions
def create_usertable():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')
    conn.commit()
    conn.close()

def add_userdata(username, password):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO userstable(username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM userstable WHERE username =? AND password =?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Simulated prediction function (Replace with actual model prediction)
def predict_diabetic_retinopathy(image):
    prediction = np.random.choice([0, 1])  # 0 for No DR, 1 for DR
    confidence_score = np.random.rand()  # Random confidence score for demo purposes
    return prediction, confidence_score

# Set up the database
create_usertable()

# Streamlit application
st.title("Diabetic Retinopathy Prediction")

def login_tab():
    st.sidebar.subheader("Login Section")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type='password')
    if st.sidebar.button("Login"):
        hashed_pswd = hash_password(password)
        result = login_user(username, hashed_pswd)
        if result:
            st.session_state['authenticated'] = True
            st.success(f"Logged in as {username}")

            # Main app content
            st.write("""
            ## Upload patient images
            (Note: In practice, these would be actual clinical images)
            """)

            # Allow multiple file uploads
            uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=["jpg", "jpeg", "png"])

            if uploaded_files:
                if st.button('Identify Diagnosis'):
                    progress_bar = st.progress(0)
                    total_files = len(uploaded_files)
                    for i, uploaded_file in enumerate(uploaded_files):
                        image = Image.open(uploaded_file)
                        st.image(image, caption=f'Uploaded Image: {uploaded_file.name}', use_column_width=True)
                        input_data = np.random.rand(1, 5)
                        prediction, confidence_score = predict_diabetic_retinopathy(input_data)
                        rounded_confidence_score = round(confidence_score, 4)
                        confidence_scores = [round((1 - confidence_score), 4), rounded_confidence_score]
                        binary_class = ["No DR", "DR"]
                        st.write(f"### Confidence Scores for {uploaded_file.name}")
                        st.bar_chart(pd.DataFrame({"Confidence Score": confidence_scores}, index=binary_class))
                        if prediction == 1:
                            st.success(f"The model predicts Diabetic Retinopathy for {uploaded_file.name} with a confidence score of {rounded_confidence_score:.4f}.")
                        else:
                            st.success(f"The model predicts No Diabetic Retinopathy for {uploaded_file.name} with a confidence score of {rounded_confidence_score:.4f}.")
                        progress = (i + 1) / total_files
                        progress_bar.progress(progress)
                        time.sleep(0.1)
                    st.success("Processing complete!")
        else:
            st.warning("Incorrect Username/Password")

def signup_tab():
    st.sidebar.subheader("Create New Account")
    new_user = st.sidebar.text_input("Username", key="username")
    new_password = st.sidebar.text_input("Password", type='password', key="password")
    if st.sidebar.button("SignUp"):
        create_usertable()
        hashed_new_password = hash_password(new_password)
        add_userdata(new_user, hashed_new_password)
        st.success("You have successfully created an account")
        st.info("Go to Login Tab to login")

tab1, tab2 = st.sidebar.tabs(["Login", "SignUp"])
with tab1:
    login_tab()
with tab2:
    signup_tab()

