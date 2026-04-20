import streamlit as st
from google import genai

st.set_page_config(page_title="Quantm AI", layout="wide")
st.title("💠 Quantm AI Wealth")
st.write("the_aka, humne engine start kar diya hai! 🔥")
# --- API & CLIENT ---
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    client = genai.Client(api_key=api_key)
except:
    st.error("Yaar, API Key check karo!")

# --- THE SOUL (Persona) ---
SYSP = "You are Quantm AI Wealth Architect by the_aka. Tone: Witty smart friend (Hinglish)."

