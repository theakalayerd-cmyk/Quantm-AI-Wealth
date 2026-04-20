import streamlit as st
from google import genai

# --- PAGE CONFIG ---
st.set_page_config(page_title="Quantm AI Wealth", page_icon="💠", layout="wide")

# --- ENGINE ---
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except:
    st.error("Bhai, Secrets mein key check karo!")
    st.stop()

SYSP = "You are Quantm AI Wealth Architect by the_aka. Tone: Witty, high-level mentor (Hinglish mix)."

# --- THE "REPLIT" COLOR INJECTION ---
st.markdown("""
    <style>
    /* Main Dark Background */
    .stApp { background-color: #06090f; color: #e2e8f0; }
    header, footer { visibility: hidden; }

    /* Sidebar - Deep Dark */
    section[data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 2px solid #1e293b;
    }

    /* Glowing Title Effect */
    .replit-title {
        font-size: 38px; font-weight: 900;
        background: linear-gradient(135deg, #ffffff 30%, #22d3ee 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 0px 15px rgba(34, 211, 238, 0.4));
        margin-bottom: 5px;
    }

    /* Tool Buttons with Neon Glow */
    .stButton>button {
        background: #111827; 
        color: #94a3b8;
        border: 1px solid #1e293b;
        border-radius: 10px;
        padding: 12px;
        font-weight: 600;
        transition: 0.4s all;
    }
    .stButton>button:hover {
        border-color: #22d3ee;
        color: #22d3ee;
        box-shadow: 0px 0px 20px rgba(34, 211, 238, 0.3);
        transform: scale(1.02);
    }

    /* Chat Container Neon Border */
    [data-testid="stChatMessage"] {
        background: #0d1117;
        border: 1px solid #1e293b;
        border-radius: 12px;
        margin-bottom: 10px;
    }
    
    /* Elite Button (Gradient) */
    .elite-btn {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white; border: none; padding: 10px;
        border-radius: 8px; text-align: center; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Left Panel) ---
with st.sidebar:
    st.markdown("<h2 style='color:#22d3ee; text-shadow: 0 0 10px #22d3ee55;'>💠 QUANTM AI</h2>", unsafe_allow_html=True)
    st.caption("by the_aka | v1.0.5")
    st.markdown("---")
    st.write("📂 **FILES**")
    st.markdown("<p style='color:#64748b; font-size:14px;'>📁 app.py<br>📁 requirements.txt</p>", unsafe_allow_html=True)
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    if st.button("⭐ Go Elite — ₹199/mo"): 
        st.balloons()
    st.markdown("<p style='font-size:10px; color:#475569;'>QUANTM AI CORE ACTIVE</p>", unsafe_allow_html=True)

# --- MAIN CANVAS ---
left_col, right_col = st.columns([1, 1.3], gap="large")

with left_col:
    st.markdown("<h1 class='replit-title'>QUANTM AI WEALTH</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#94a3b8; font-size:16px;'>Your Wealth & Creative Architect</p>", unsafe_allow_html=True)
    
    st.markdown("<br><h4 style='color:#22d3ee;'>🛠️ TOOLS</h4>", unsafe_allow_html=True)
    # The Grid Layout for Tools
    t1, t2 = st.columns(2)
    with t1:
        if st.button("📊 Forex Strategy"): st.session_state.p = "Bhai, Forex strategy batao."
        if st.button("🚀 AI Branding"): st.session_state.p = "AI brand growth ideas?"
    with t2:
        if st.button("🎵 EDM Melodies"): st.session_state.p = "EDM melody ideas do."
        if st.button("💻 Python Code"): st.session_state.p = "Help with Python code."

with right_col:
    st.markdown("<h4 style='color:#22d3ee; margin-top:10px;'>New Conversation</h4>", unsafe_allow_html=True)
    
    if "m" not in st.session_state: st.session_state.m = []
    
    # Smooth Chat History Area
    chat_space = st.container(height=480, border=True)
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
