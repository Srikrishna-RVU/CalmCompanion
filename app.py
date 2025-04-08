import os
import streamlit as st
import streamlit.components.v1 as components
from chat_engine import get_response, init_conversation
from utils import is_crisis
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Set page appearance
st.set_page_config(page_title="Calm Companion", page_icon="🪷")
st.title("🪷 Calm Companion")
st.markdown("""
Welcome to **CalmCompanion**, your gentle mental health support chat.  
This assistant offers emotionally supportive conversation — it's not a replacement for therapy or emergency care.
""")

# Init state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    init_conversation()
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("➕ New Chat"):
    st.session_state.chat_history = []
    st.rerun()  # Optional: clear inputs & UI refresh


with st.sidebar:
    st.markdown("### 🧘 Calm Tools")

    if "show_breath" not in st.session_state:
        st.session_state.show_breath = False

    if st.button("🌬️ Start Deep Breathing"):
        st.session_state.show_breath = True

    if st.session_state.show_breath:
        st.markdown("#### One Deep Breath Cycle")

        breathing_animation = """
        <style>
@keyframes breath {
  0% { transform: scale(1); }
  25% { transform: scale(1.5); }
  50% { transform: scale(1); }
  75% { transform: scale(0.8); }
  100% { transform: scale(1); }
}

.circle {
  margin: 20px auto;
  width: 100px;
  height: 100px;
  background: #B9BEA5;  
  border-radius: 50%;
  animation: breath 8s ease-in-out 1;
}

.breathe-label {
  text-align: center;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 20px;
  color: #2E2E2E;
  margin-top: 12px;
}
</style>

<div class="circle"></div>
<div class="breathe-label">Inhale... Hold... Exhale...</div>

        """
        components.html(breathing_animation, height=200)
        st.session_state.show_breath = False 


# Chat input and logic
user_input = st.chat_input("How are you feeling today?")
if user_input:
    if is_crisis(user_input):
        bot_response = (
            "I'm really sorry you're feeling this way. "
            "You're not alone. Please reach out to a trusted person or mental health professional."
        )
    else:
        bot_response = get_response(user_input)

    # Save conversation
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("CalmCompanion", bot_response))

# Display chat
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)
