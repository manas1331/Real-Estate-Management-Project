import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Function to create a database connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manas12345",
            database="flask_real"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

# Function to insert a complaint into the database
def insert_complaint(username, contact_info, complaint):
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO complaints (username, contact_info, complaint)
                VALUES (%s, %s, %s)
            """
            cursor.execute(insert_query, (username, contact_info, complaint))
            connection.commit()
            st.success("Complaint submitted successfully.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Streamlit form to collect complaint details
st.title("Complaint Submission Form")

with st.form("complaint_form"):
    username = st.text_input("Username")
    contact_info = st.text_input("Contact Information (Email or Phone)")
    complaint = st.text_area("Complaint")
    
    # Submit button
    submitted = st.form_submit_button("Submit Complaint")
    
    if submitted:
        if username and contact_info and complaint:
            # Insert the complaint into the database
            insert_complaint(username, contact_info, complaint)
        else:
            st.error("Please fill out all fields.")

# Function to view complaints in tabular format
def view_complaints():
    connection = create_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id, username, contact_info, complaint FROM complaints")
            complaints = cursor.fetchall()
            
            # Convert the data to a pandas DataFrame
            if complaints:
                complaints_df = pd.DataFrame(complaints, columns=["ID", "Username", "Contact Information", "Complaint"])
                st.dataframe(complaints_df)  # Display as a table
            else:
                st.write("No complaints found.")
        except Error as e:
            st.error(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Admin view option to see all complaints in a table
if st.checkbox("Show all complaints"):
    view_complaints()
