import streamlit as st
import os


# Header
st.title("Our Properties")

# Sample data for properties with Indian names, Bengaluru addresses, and prices in INR
property_names = [
    "Prestige Lakeside Habitat", "Brigade Exotica", "Sobha Dream Acres", "Godrej Woodland",
    "Purva Palm Beach", "Prestige Golfshire", "Brigade El Dorado", "RMZ Galleria",
    "Vaishnavi Oasis", "Mantri Serenity", "Nitesh Park Avenue", "Shobha Forest View",
    "Rohan Upavan", "Adarsh Palm Retreat", "Purva Atmosphere", "Embassy Boulevard",
    "Salarpuria Sattva Divinity", "Mahaveer Ranches", "Total Environment Pursuit", "Kolte Patil Mirabilis"
]

# Define the directory path for images
image_directory = r"Images"
property_images = [
    os.path.join(image_directory, f"property_{i+1}.jpg") for i in range(20)
]

property_addresses = [
    "Whitefield, Bengaluru", "Old Madras Road, Bengaluru", "Panathur, Bengaluru", "Sarjapur, Bengaluru",
    "Hennur Road, Bengaluru", "Devanahalli, Bengaluru", "Bagalur, Bengaluru", "Yelahanka, Bengaluru",
    "JP Nagar, Bengaluru", "Kanakapura Road, Bengaluru", "Sankey Road, Bengaluru", "Kanakapura Road, Bengaluru",
    "Hennur, Bengaluru", "Bellandur, Bengaluru", "Thanisandra Main Road, Bengaluru", "North Bengaluru",
    "Mysore Road, Bengaluru", "Sarjapur Road, Bengaluru", "Whitefield, Bengaluru", "Horamavu, Bengaluru"
]

property_prices = [
    "1,20,00,000", "85,00,000", "95,00,000", "78,00,000",
    "1,50,00,000", "1,10,00,000", "92,00,000", "65,00,000",
    "98,00,000", "1,25,00,000", "89,00,000", "80,00,000",
    "94,00,000", "1,30,00,000", "71,00,000", "84,00,000",
    "99,00,000", "1,05,00,000", "1,10,00,000", "1,20,00,000"
]

# Define image width
image_width = 290  # Width in pixels for a compact layout

# Creating 20 boxes for properties, 4 per row
for i in range(0, 20, 4):  # Loop to display 4 property boxes per row
    col1, col2, col3, col4 = st.columns(4, gap="small")  # Set 4 columns with small gaps

    for col, idx in zip([col1, col2, col3, col4], [i, i+1, i+2, i+3]):
        with col:
            if idx < len(property_names):  # Ensure index is within range
                st.image(property_images[idx], width=image_width)  # Set custom image width
                st.subheader(property_names[idx])
                st.write(f"**Address:** {property_addresses[idx]}")
                # Use HTML encoding for the rupee symbol
                st.markdown(f"**Price:** &#8377;{property_prices[idx]}")
