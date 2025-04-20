
import streamlit as st
from llm_chat import get_response  # Make sure this is importing correctly
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up page title and description
st.set_page_config(page_title="Apna AI", page_icon="🤖")
st.title("Apna AI 🤖")


# Initialize memory list to store chat history
memory = []

# Create a text input box for user input
user_input = st.text_input("You: ", "")


# Debugging log for checking user input
st.write(f"User Input: {user_input}")

# Add a button to submit the input
if user_input:
    try:
        # Get response from the model
        reply = get_response(user_input, memory)
        # Log AI response for debugging
        st.write(f"AI Response: {reply}")

        # Append user and assistant messages to memory
        memory.append({"role": "user", "content": user_input})
        memory.append({"role": "assistant", "content": reply})

        # Display the conversation in the Streamlit UI
        st.text_area("Conversation:", value="\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in memory]), height=400)
        st.text(f"AI: {reply}")
    except Exception as e:
        # If an error occurs, display it on the UI
        st.error(f"Error: {e}")
else:
    st.text("Please type your message to start the conversation.")
    

# Allow user to exit or quit
if st.button('Exit'):
    st.stop()

