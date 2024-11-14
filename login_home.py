import streamlit as st
import mysql.connector
import os

st.logo("Images\logo.png")

# Set page title and layout
st.set_page_config(page_title="Landmark Estates - Home", layout="wide")

# Function to create a connection to the MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Manas12345",
        database="flask_real"
    )

# Function to authenticate a user
def authenticate(username, password):
    conn = create_connection()
    cursor = conn.cursor() #Used to communicate with the mysql database
    query = "SELECT password FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    conn.close()
    if result and result[0] == password:
        return True
    return False

# Function to create a new user
def new_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s"
    cursor.execute(query, (username,))
    if cursor.fetchone():
        conn.close()
        return "User already exists."
    
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))
    conn.commit()
    conn.close()
    return "User created successfully."

# Function to handle the registration form and process
def register():
    st.subheader("Register New Account")
    new_username = st.text_input("Enter a new username")
    new_password = st.text_input("Enter a new password", type="password")

    if st.button("Register"):
        result = new_user(new_username, new_password)
        if result == "User created successfully.":
            st.success(result)
            st.session_state.page = 'login'  # Redirect to login page after successful registration
            st.rerun()
        else:
            st.error(result)

# Function to dynamically load and display page content
def load_page(page_path):
    if os.path.exists(page_path):
        with open(page_path, "r") as file:
            exec(file.read(), globals())

# Function to display the main content after login
def main_content():
    st.write("Welcome to Landmark Estates!")

    # Sidebar navigation with radio buttons for each page
    page_options = {
        "Home": "views/home.py",
        "Properties": "views/properties.py",
        "My Properties": "views/my_property.py",
        "Buy": "views/buy.py",
        "Sell": "views/sell.py",
        "Chatbot":"views\chatbot.py",
        "Complaints": "views/complaint.py",
        "Logout": "views/logout.py"
    }
    st.sidebar.title("Navigation")
    page_choice = st.sidebar.radio("Go to", list(page_options.keys()))

    if page_choice == "Logout":
        st.session_state.is_logged_in = False
        st.session_state.page = 'login'
        st.rerun()
    else:
        page_path = page_options[page_choice]
        load_page(page_path)

# Function to handle logout and redirect to login page
def logout():
    st.session_state.is_logged_in = False
    st.session_state.page = 'login'
    st.rerun()

# Main app function
def main():
    st.title("Landmark Estates")

    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False
        st.session_state.page = 'login'

    if st.session_state.page == 'register':
        register()
    elif st.session_state.page == 'login':
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.is_logged_in = True
                st.session_state.page = "home"
                st.rerun()  # Rerun to refresh the app and hide the form
            else:
                st.error("Incorrect username or password")

        if st.button("Don't have an account? Register here"):
            st.session_state.page = 'register'
            st.rerun()

    elif st.session_state.page == "home" and st.session_state.is_logged_in:
        st.success("Logged in successfully!")
        main_content()  # Display main content

        if st.button("Logout"):
            logout()  # Call logout function to logout and redirect to login page

    st.markdown("""
    <div style='text-align: center; font-size: 20px; margin-top: 50px;'>
        © Copyright 2024. All rights reserved Landmark Estates inc.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
