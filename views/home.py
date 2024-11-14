import streamlit as st




# Title of the page
st.title("Welcome to Landmark Estates")

# About Us section
st.write("### About Us")
st.write("""
    Landmark Estates is a leading real estate agency dedicated to helping our clients find their dream homes. 
    Our team of experienced agents is committed to providing personalized service and expert guidance throughout 
    the entire real estate journey. We offer a wide range of properties, from cozy apartments to luxurious estates, 
    ensuring that every client’s needs are met with the highest level of satisfaction and professionalism.
""")

# Mission statement or business values
st.write("### Our Mission")
st.write("""
    At Landmark Estates, our mission is to empower individuals and families by connecting them with properties 
    that meet their needs, preferences, and aspirations. We believe in building lasting relationships through trust, 
    integrity, and dedication to excellence.
""")

# Call to Action (CTA) section
st.write("### Start Your Property Journey Today!")
st.write("""
    Whether you re buying your first home, selling a property, or looking for investment opportunities, we are here to 
    help. Explore our website, view available listings, and find the perfect place for you and your family.
""")


st.image("Images/welcome.jpg", width=800, caption="Your Real Estate advisor.")
# Call to action with links for registration and login
# st.write("#### Ready to get started?")
# st.markdown("""
#     - [Register here to get started](views/register.py)  
#     - [Login to view properties](login)  
# """)

# Featured Properties Section (Placeholder for future property data)
st.write("### Featured Properties")
st.write("""
    We have a variety of properties available across different price ranges. Check out our featured listings for 
    prime opportunities in residential and commercial real estate.
""")
# Here you can add code to display actual property listings using a database or a collection of image links.

# Subheader to encourage further interaction
st.markdown("<p class='sub-header'>Start exploring today!</p>", unsafe_allow_html=True)

# Footer section with contact details or more CTA
st.write("### Contact Us")
st.write("""
    If you have any questions or need assistance, feel free to reach out to us.  
    You can contact us at [info@landmarkestates.com](mailto:info@landmarkestates.com) or call us at (123) 456-7890.
""")
