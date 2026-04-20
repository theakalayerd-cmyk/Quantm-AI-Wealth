import streamlit as st
from google import genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Quantm AI Wealth", page_icon="💠", layout="wide")

# --- ENGINE ---
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Bhai, API Key missing hai!")
    st.stop()

SYSP = "You are Quantm AI Wealth Architect by the_aka. Tone: Witty, high-level mentor (Hinglish mix)."

# --- THE "REPLIT" CSS INJECTION ---
st.markdown("""
    <style>
    /* Full Dark Mode Background */
    .stApp { background-color: #06090f; color: white; }
    header, footer { visibility: hidden; }

    /* Sidebar - Left Panel */
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #1e293b;
        width: 260px !important;
    }

    /* Neon Gradient Title (Center) */
    .replit-title {
        font-size: 32px; font-weight: 800;
        background: linear-gradient(90deg, #ffffff, #22d3ee);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        letter-spacing: 1px;
    }

    /* Glowing Tool Cards */
    .tool-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Custom Chat Container (Right) */
    .chat-box {
        background: #0d1117;
        border: 1px solid #22d3ee33;
        border-radius: 15px;
        padding: 20px;
    }

    /* Buttons Style */
    .stButton>button {
        background: #1e293b88; color: #e2e8f0;
        border: 1px solid #334155; border-radius: 8px;
        width: 100%; transition: 0.2s;
    }
    .stButton>button:hover {
        border-color: #22d3ee; color: #22d3ee;
        box-shadow: 0px 0px 10px #22d3ee44;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LAYOUT: SIDEBAR (Left) ---
with st.sidebar:
    st.markdown("<h3 style='color:#22d3ee;'>💠 QUANTM AI</h3>", unsafe_allow_html=True)
    st.caption("by the_aka")
    st.markdown("---")
    st.write("📂 **FILES**")
    st.caption("app.py")
    st.caption("requirements.txt")
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    if st.button("⭐ Go Elite — ₹199/mo"): st.balloons()

# --- MAIN LAYOUT: CANVAS (Middle) & CHAT (Right) ---
left_col, right_col = st.columns([1, 1.2], gap="large")

with left_col:
    st.markdown("<h2 class='replit-title'>QUANTM AI WEALTH</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#64748b;'>Your Wealth & Creative Architect</p>", unsafe_allow_html=True)
    
    # Tools Section (The Boxes)
    st.markdown("---")
    st.write("🛠️ **TOOLS**")
    with st.container():
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("📊 Forex Strategy"): st.session_state.p = "Bhai, Forex strategy batao."
            if st.button("🚀 AI Branding"): st.session_state.p = "AI brand growth ideas?"
        with col_b:
            if st.button("🎵 EDM Melodies"): st.session_state.p = "EDM melody ideas do."
            if st.button("💻 Python Code"): st.session_state.p = "Help with Python code."

with right_col:
    st.markdown("<div style='padding-top: 10px;'></div>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#22d3ee;'>New Conversation</h4>", unsafe_allow_html=True)
    
    # Chat Logic
    if "m" not in st.session_state: st.session_state.m = []
    
    chat_space = st.container(height=450)
    with chat_space:
        for msg in st.session_state.m:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Chat Input
    prompt = st.chat_input("Ask Quantm AI anything...")
    if "p" in st.session_state: prompt = st.session_state.pop("p")

    if prompt:
        st.session_state.m.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            res = client.models.generate_content(model='gemini-2.0-flash', contents=prompt, config={'system_instruction': SYSP})
            st.markdown(res.text)
            st.session_state.m.append({"role": "assistant", "content": res.text})
