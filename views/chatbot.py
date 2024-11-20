import streamlit as st
import google.generativeai as genai
from llama_index.core import PromptTemplate
import re

# Set up the API key for Google AI
genai.configure(api_key=st.secrets["general"]["GOOGLE_API_KEY"])


# Title for the app
st.title("Real Estate Assistant Bot")

# Define the assistant's instructions
instruction_str = """\
    You are a real estate assistant helping users with property-related inquiries.
    Provide helpful responses, including information about properties, contact details, or general real estate advice.
    Do not make any legal or financial decisions on behalf of the user.
"""

# Prompt template for the real estate assistant
real_estate_prompt = PromptTemplate(
    """\
    As a real estate assistant:
    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Response: """
)

# Create the generative model
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=['''
        As a real estate assistant, provide helpful information about property listings, availability, and general real estate tips.
    '''],
    generation_config={
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 50,
        "max_output_tokens": 500,
    },
)

# Initialize the chat session if it doesn't already exist
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.chat_history = []

# Function to extract city from user input (basic example)
def extract_city(query):
    match = re.search(r'(\w+)', query)
    if match:
        return match.group(1)
    return None

# Chat input from user
prompt = st.chat_input("Ask about real estate properties")

# Handle chat input and response
if prompt:
    st.session_state.chat_history.append({"role": "user", "message": prompt})
    st.chat_message("user").markdown(prompt)

    # If the query mentions properties or cities, generate a response
    if "property" in prompt.lower() or "city" in prompt.lower():
        city = extract_city(prompt)
        
        if city:
            # Generate a response based on the city or property query
            property_response = f"Here are some available properties in {city}. Please check the website for more details or let me know if you need assistance."
        else:
            property_response = "Can you please specify the city or property type you're interested in?"

        st.session_state.chat_history.append({"role": "assistant", "message": property_response})
        st.chat_message("assistant").markdown(property_response)
    else:
        # Handle other queries by sending to the generative model
        response = st.session_state.chat_session.send_message(prompt)
        st.session_state.chat_history.append({"role": "assistant", "message": response.text})
        st.chat_message("assistant").markdown(response.text)

# Display the chat history
st.subheader("Chat History")
for entry in st.session_state.chat_history:
    role = "User" if entry["role"] == "user" else "Assistant"
    st.markdown(f"*{role}:* {entry['message']}")

