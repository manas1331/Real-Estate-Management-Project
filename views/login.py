#from backend.app import hhh
from login_home import gth
import streamlit as st



# Login form with background container
st.markdown("<div class='login-container'>", unsafe_allow_html=True)


# Dummy authentication function
def authenticate(username, password):
    return username == "admin" and password == "password"

# Main app function

st.title("Streamlit App")

    # User inputs
if 'is_logged_in' not in st.session_state: st.session_state.is_logged_in = False
if not st.session_state.is_logged_in: 
    username = st.text_input("Username") 
    password = st.text_input("Password", type="password") 
    if st.button("Login"): 
        if authenticate(username, password): 
            st.session_state.is_logged_in = True 
            st.rerun() # Rerun to refresh the app and hide the form else: 
            st.error("Incorrect username or password") 
        else:
            st.success("Logged in successfully!") 
            gth()
# Additional app functionality
# if st.session_state.get("is_logged_in"):
#     st.write("Welcome to the app!")
#     hhh()

# Example function to be called after login




st.markdown("</div>", unsafe_allow_html=True)
