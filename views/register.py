import streamlit as st


st.title("Register")
name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    # Add registration logic here (e.g., saving user data)
    st.success("Registration successful!")

# Optional message or footer
st.markdown("<p class='sub-header'>Thank you for choosing Landmark Estates!</p>", unsafe_allow_html=True)

# Display the registration page

