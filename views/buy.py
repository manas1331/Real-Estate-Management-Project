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
            password="your password",
            database="flask_real"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

# Function to fetch all properties from the buy table
def fetch_properties_from_buy():
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "SELECT id, property_name, address, price FROM buy"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            connection.close()
            return rows
    except Error as e:
        st.error(f"Error: {e}")
        return []

# Function to add a property to my_properties table after user clicks "BUY"
def add_property_to_my_properties(property_name, address, price, property_id):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            
            # Insert into my_properties table
            query_insert = """INSERT INTO my_properties (property_name, address, price) 
                              VALUES (%s, %s, %s)"""
            cursor.execute(query_insert, (property_name, address, price))
            connection.commit()

            # Delete from the buy table
            query_delete = "DELETE FROM buy WHERE id = %s"
            cursor.execute(query_delete, (property_id,))
            connection.commit()

            cursor.close()
            connection.close()
            st.success(f"Property '{property_name}' added to your properties and removed from the buy list!")
    except Error as e:
        st.error(f"Error: {e}")

# Streamlit page layout for displaying properties
def buy_property_page():
    st.title("Properties Available for Buy")

    # Display properties from buy table
    buy_properties = fetch_properties_from_buy()
    if buy_properties:
        st.subheader("Available Properties")

        # Display properties in tabular format
        property_df = pd.DataFrame(buy_properties, columns=["ID", "Property Name", "Address", "Price"])
        st.table(property_df[["Property Name", "Address", "Price"]])  # Show only relevant columns

        # Provide a dropdown for the user to select a property
        property_names = [prop[1] for prop in buy_properties]
        selected_property_name = st.selectbox("Select a property to buy", property_names)

        if selected_property_name:
            # Get the details of the selected property
            selected_property = next(property for property in buy_properties if property[1] == selected_property_name)
            property_id, property_name, address, price = selected_property

            # Provide a button to buy the selected property
            if st.button(f"Buy {selected_property_name}"):
                st.write(f"Buying {selected_property_name} - {address} for {price}")
                add_property_to_my_properties(property_name, address, price, property_id)

    else:
        st.warning("No properties available for purchase.")

# Main function to run the app
def main():
    buy_property_page()

if __name__ == "__main__":
    main()
