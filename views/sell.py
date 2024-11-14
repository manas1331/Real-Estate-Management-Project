import streamlit as st
import mysql.connector
from mysql.connector import Error

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

# Function to insert property data into both the sell and buy tables
def insert_property(property_name, address, price):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            
            # Insert into the 'sell' table
            sell_query = """INSERT INTO sell (property_name, address, price) 
                            VALUES (%s, %s, %s)"""
            cursor.execute(sell_query, (property_name, address, price))
            
            # Insert into the 'buy' table
            buy_query = """INSERT INTO buy (property_name, address, price) 
                           VALUES (%s, %s, %s)"""
            cursor.execute(buy_query, (property_name, address, price))
            
            connection.commit()
            cursor.close()
            connection.close()
            st.success("Property details added successfully to both sell and buy tables!")
    except Error as e:
        st.error(f"Error: {e}")

# Function to fetch all properties from the sell table
def fetch_properties():
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM sell"
            cursor.execute(query)
            properties = cursor.fetchall()
            cursor.close()
            connection.close()
            return properties
    except Error as e:
        st.error(f"Error: {e}")
        return []

# Streamlit page layout for adding a property and displaying properties
def sell_property_page():
    st.title("Sell Property")

    # Property details form
    with st.form(key="property_form"):
        property_name = st.text_input("Property Name")
        address = st.text_area("Address")
        price = st.number_input("Price (INR)", min_value=1, step=100000)

        submit_button = st.form_submit_button(label="Submit")

    # If the form is submitted
    if submit_button:
        if not property_name or not address or not price:
            st.error("Please fill in all the details.")
        else:
            # Insert property data into both tables
            insert_property(property_name, address, price)

    # Fetch and display all properties for sale
    properties = fetch_properties()
    if properties:
        # Display properties in a tabular format
        st.subheader("Properties for Sale")
        st.table(properties)  # Display properties as a table
    else:
        st.info("No properties available for sale yet.")

# Main function to run the app
def main():
    sell_property_page()

if __name__ == "__main__":
    main()
