import streamlit as st
from google import genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Quantm AI Elite", page_icon="💠", layout="wide")

# --- CYBERPUNK GLASS UI ---
st.markdown("""
<style>
.stApp { background: radial-gradient(circle at top right, #0f172a, #020617); color: #f8fafc; }
header, footer { visibility: hidden; }
.neon-title {
    font-size: 50px; font-weight: 900; text-align: center;
    background: linear-gradient(180deg, #fff 20%, #38bdf8 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 15px rgba(56, 189, 248, 0.6));
}
.glass-panel {
    background: rgba(30, 41, 59, 0.4); backdrop-filter: blur(15px);
    border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 24px; padding: 25px;
}
.stButton>button {
    background: rgba(56, 189, 248, 0.1) !important; color: #38bdf8 !important;
    border: 1px solid #38bdf8 !important; border-radius: 12px !important;
    width: 100%; height: 50px; font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- ENGINE SETUP ---
try:
    # Bhai, apni API Key (AIzaSy...) yahan dalo
    client = genai.Client(api_key="TUMHARI_API_KEY_YAHAN_DALO")
except Exception as e:
    st.error("API Key missing!")
    st.stop()

# --- UI ---
st.markdown("<h1 class='neon-title'>QUANTM AI ELITE</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#94a3b8;'>Architected by the_aka | Future is Live</p>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown("<div class='glass-panel'>", unsafe_allow_html=True)
    st.write("### ⚡ COMMAND CENTER")
    if st.button("📊 ANALYSIS: FOREX"): st.session_state.p = "Bhai, Forex strategy batao."
    if st.button("🚀 GROWTH: BRANDING"): st.session_state.p = "AI brand growth ideas?"
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    if "m" not in st.session_state: st.session_state.m = []
    
    for msg in st.session_state.m:
        with st.chat_message(msg["role"]): st.markdown(msg["content"])
        
    prompt = st.chat_input("Command your AI Architect...")
    if prompt:
        st.session_state.m.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            try:
                res = client.models.generate_content(model='gemini-2.0-flash', contents=prompt)
                st.markdown(res.text)
                st.session_state.m.append({"role": "assistant", "content": res.text})
            except Exception as e:
                st.error("API Key check karo!")

