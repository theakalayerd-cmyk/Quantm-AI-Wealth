import streamlit as st
from google import genai

# --- ENGINE SETUP ---
st.set_page_config(page_title="Quantm AI", page_icon="💠", layout="wide")

# Connect to the key you just saved
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Bhai, Secrets mein key check karo!")
    st.stop()

# --- THE SOUL OF QUANTM AI ---
SYSP = "You are Quantm AI Wealth Architect by the_aka. Tone: Witty smart friend (Hinglish mix)."

# --- DASHBOARD UI ---
st.markdown("<h1 style='text-align: center; color: #22d3ee;'>💠 Quantm AI Wealth</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Your Wealth & Creative Architect by the_aka</p>", unsafe_allow_html=True)

# Chat History Setup
if "m" not in st.session_state: st.session_state.m = []

# Display Messages
for msg in st.session_state.m:
    with st.chat_message(msg["role"]): st.markdown(msg["content"])

# Chat Input & AI Response
if prompt := st.chat_input("Ask Quantm AI anything..."):
    st.session_state.m.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)
    
    with st.chat_message("assistant"):
        res = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=prompt, 
            config={'system_instruction': SYSP}
        )
        st.markdown(res.text)
        st.session_state.m.append({"role": "assistant", "content": res.text})
