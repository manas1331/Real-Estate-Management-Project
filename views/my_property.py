import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd

# MySQL connection function
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

# Function to fetch all properties from my_properties table
def fetch_properties_from_my_properties():
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT property_name, address, price FROM my_properties"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
            return rows
    except Error as e:
        st.error(f"Error: {e}")
        return []

# Streamlit page layout for displaying user's purchased properties
def my_properties_page():
    st.title("Your Purchased Properties")

    # Fetch properties from the my_properties table
    user_properties = fetch_properties_from_my_properties()
    if user_properties:
        st.subheader("Your Properties")

        # Create a DataFrame to display the properties
        property_df = pd.DataFrame(user_properties, columns=["Property Name", "Address", "Price"])
        st.dataframe(property_df)  # Display properties in tabular format with interactive features
    else:
        st.warning("You have not purchased any properties yet.")

# Main function to run the app
def main():
    my_properties_page()

if __name__ == "__main__":
    main()
