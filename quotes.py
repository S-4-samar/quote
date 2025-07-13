import streamlit as st
import random

st.set_page_config(page_title="💖 Love Quote Generator", layout="centered")

st.markdown("""
    <style>
    body {
        background: radial-gradient(circle at center, #1a1a1a, #000);
        overflow: hidden;
        font-family: 'Poppins', sans-serif;
        margin: 0;
    }

    /* Sidebar Blue Outer Glow */
    section[data-testid="stSidebar"] {
        background: black !important;
        border-right: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff, 0 0 45px #00ffff;
    }

    /* About Box Flex with Red Inset Neon */
    .about-box {
        padding: 20px;
        margin: 20px 10px;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.6);
        box-shadow: inset 0 0 15px red, inset 0 0 30px red;
        color: white;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    /* Base Elements */
    .background-stars span {
        position: absolute;
        color: #fff;
        font-size: 8px;
        text-shadow: 0 0 3px #0ff, 0 0 6px #0ff, 0 0 12px #0ff;
        animation: blink 1.5s infinite alternate;
    }

    @keyframes blink {
        0% { opacity: 0.2; }
        100% { opacity: 1; }
    }

    h1 {
        text-align: center;
        color: white;
        font-size: 28px;
    }

    @media screen and (max-width: 600px) {
        .about-box {
            margin: 10px;
            padding: 15px;
            font-size: 14px;
        }
        h1 {
            font-size: 22px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
with st.sidebar:
    st.markdown('<div class="about-box">', unsafe_allow_html=True)
    st.markdown("## About this App", unsafe_allow_html=True)
    st.markdown("""
    I’ve created this app at **11 PM**.  
    Honestly... just felt like making something a little extra sweet and a little extra cheeky.  
    """, unsafe_allow_html=True)

    st.markdown("""
    <hr style="border-top: 1px solid rgba(255, 255, 255, 0.2);">
    <p>🔥 Are you a campfire?<br><em>Because you’re hot and I want s’more.</em></p>
    <p>❄️ If kisses were snowflakes...<br><em>I’d send you a blizzard.</em></p>
    <p>📶 Is your name WiFi?<br><em>Because I’m feeling a connection.</em></p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Background stars
background_stars = ""
for _ in range(80):
    while True:
        left = random.randint(0, 100)
        top = random.randint(0, 100)
        if not (40 < left < 60 and 35 < top < 65):
            background_stars += f"<span style='left:{left}vw; top:{top}vh;'>★</span>"
            break
st.markdown(f"<div class='background-stars'>{background_stars}</div>", unsafe_allow_html=True)

st.markdown("<h1>My Friend 👦🏻</h1>", unsafe_allow_html=True)

quotes = [
    "🌹 Every moment with you is like a beautiful dream I never want to wake up from.",
    "💌 You’re my favorite notification every day.",
    "💕 I didn’t choose you — my heart did.",
    "🌸 With you, I’ve found my forever.",
    "✨ You make my heart smile.",
    "❤️ You are the poem I never knew how to write, and this life is the story I always wanted to tell with you.",
    "🎀 You + Me = Infinite Love.",
    "🔥 I don’t need a blanket... I’ve got your body heat.",
]

if st.button("💌 Show Me a Message"):
    st.markdown(f"<div class='quote-box'>{random.choice(quotes)}</div>", unsafe_allow_html=True)
    st.balloons()

with open("tumheho.mp3", "rb") as audio_file:
    st.audio(audio_file, format="audio/mp3")
