import streamlit as st
from chatbot_backend import MentalWellnessChatbot
import datetime

# Initialize chatbot
bot = MentalWellnessChatbot()

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Mental Wellness Assistant", page_icon="🧠", layout="wide")
st.markdown(
    """
    <style>
    /* General body */
    body {
        background-color: #E8F0F2;
        color: #333333;
        font-family: 'Helvetica', sans-serif;
    }

    /* Chat cards */
    .chat-card {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
        max-width: 80%;
    }
    .user-card {
        background-color: #A8DADC;
        color: #1D3557;
        text-align: right;
        margin-left: 20%;
    }
    .bot-card {
        background-color: #F1FAEE;
        color: #457B9D;
        text-align: left;
        margin-right: 20%;
    }

    /* Input box */
    .stTextInput > div > div > input {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #B0C4DE;
    }

    /* Buttons */
    .stButton>button {
        background-color: #457B9D;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        font-weight: bold;
    }

    /* Dashboard cards */
    .card {
        background-color: #F1FAEE;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True
)

# ----------------- LAYOUT -----------------
st.title("🧠 Mental Wellness Assistant")
st.markdown("Welcome! Talk to me or track your daily mood below.")

# Session state for conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Columns for chat and dashboard
col1, col2 = st.columns([2, 1])

# ----------------- CHAT INTERFACE -----------------
with col1:
    st.subheader("Chat with your assistant")
    user_input = st.text_input("Type your message here...", key="chat_input")

    if st.button("Send") or user_input:
        if user_input:
            # Append user message
            st.session_state.messages.append({"user": user_input})
            # Get bot response
            bot_response = bot.get_response(user_input)
            st.session_state.messages.append({"bot": bot_response})
            user_input = ""  # Clear input

    # Display chat
    for msg in st.session_state.messages:
        if "user" in msg:
            st.markdown(f"<div class='chat-card user-card'>{msg['user']}</div>", unsafe_allow_html=True)
        if "bot" in msg:
            st.markdown(f"<div class='chat-card bot-card'>{msg['bot']}</div>", unsafe_allow_html=True)

# ----------------- DASHBOARD -----------------
with col2:
    st.subheader("🌿 Wellness Dashboard")

    # Mood tracker
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("**Daily Mood Tracker**")
    mood_options = ["Happy 😊", "Neutral 😐", "Sad 😔", "Anxious 😟", "Tired 😴"]
    today = datetime.date.today().strftime("%b %d, %Y")
    selected_mood = st.selectbox(f"Select your mood for {today}:", mood_options)
    if st.button("Log Mood", key="mood_button"):
        st.success(f"Mood '{selected_mood}' logged for {today}!")
    st.markdown("</div>", unsafe_allow_html=True)

    # Insights
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("**Wellness Insights**")
    st.markdown("- Track your mood daily to notice patterns.\n- Reflect on what makes you feel better.\n- Practice small mindfulness exercises each day.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Guided meditation placeholder
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("**Guided Meditation**")
    st.markdown("🎵 *Meditation audio or video placeholder here*")
    st.markdown("</div>", unsafe_allow_html=True)