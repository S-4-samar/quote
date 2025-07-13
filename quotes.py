import streamlit as st
import random

st.set_page_config(page_title="💖 Love Quote Generator", layout="centered")

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background: radial-gradient(circle at center, #1a1a1a, #000);
        overflow: hidden;
        font-family: 'Poppins', sans-serif;
        margin: 0;
    }
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
    div.stButton > button {
        width: 100%;
        max-width: 300px;
        background: linear-gradient(to right, #0ff, #08f);
        color: white;
        font-size: 18px;
        padding: 12px 20px;
        border-radius: 50px;
        transition: all 0.3s ease-in-out;
        box-shadow: 0px 4px 15px rgba(0, 255, 255, 0.5);
        margin: auto;
        display: block;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0px 6px 20px rgba(0, 255, 255, 0.8);
        cursor: pointer;
    }
    .quote-box {
        padding: 20px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.05);
        color: white;
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff, 0 0 40px #00ffff;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        text-shadow: 0 0 5px #0ff, 0 0 10px #0ff;
    }
    h1 {
        text-align: center;
        color: white;
        font-size: 28px;
        text-shadow: 0 0 5px #0ff, 0 0 10px #0ff;
    }
    canvas {
        transform: scale(0.5);
    }

    /* Sidebar Outer Neon Blue */
    section[data-testid="stSidebar"] {
        background: black !important;
        border-right: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff, 0 0 45px #00ffff;
        padding: 0;
    }

    /* Sidebar Inner Box Red Neon */
    .about-box {
        padding: 20px;
        margin: 15px;
        border-radius: 15px;
        background: rgba(0, 0, 0, 0.5);
        box-shadow: inset 0 0 15px red;
        color: #fff;
        text-shadow: 0 0 5px red;
    }

    @media screen and (max-width: 600px) {
        .quote-box {
            font-size: 16px;
            padding: 16px;
        }
        h1 {
            font-size: 22px;
        }
        div.stButton > button {
            font-size: 16px;
            padding: 12px;
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
    <div style='margin-top: 20px;'>
        <h2>Some Jokes 4 You:</h2>
        <p>🔥 Are you a campfire?<br><em>Because you’re hot and I want s’more.</em></p>
        <p>❄️ If kisses were snowflakes...<br><em>I’d send you a blizzard.</em></p>
        <p>📶 Is your name WiFi?<br><em>Because I’m feeling a connection.</em></p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Neon stars background
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
    "🌷 You are my sunshine on a cloudy day.",
    "💖 Together is my favorite place to be.",
    "🌼 In you, I’ve found the love of my life and my closest, truest friend.",
    "🎀 You + Me = Infinite Love.",
    "🔥 I don’t need a blanket... I’ve got your body heat.",
    "😈 My favorite place in the world? Right next to you... or maybe on top of you.",
    "💋 One kiss from you, and I forget the rest of the world exists.",
    "👀 Let’s skip the small talk and get to the part where I’m wrapped around you.",
    "😏 Your voice turns me on more than any song ever could.",
    "❤️‍🔥 I can’t decide what I crave more... your lips or your hands.",
    "💥 My bed feels empty without you in it... should we fix that?",
    "⚡ I was trying to concentrate... then I remembered how good you look without clothes.",
    "🖤 Just thinking about last night has me blushing... and wanting a repeat.",
    "🔥 Your name should come with a warning label: 'Highly Addictive, Handle With Care.'"
]

if st.button("💌 Show Me a Message"):
    selected_quote = random.choice(quotes)
    st.markdown(f"<div class='quote-box'>{selected_quote}</div>", unsafe_allow_html=True)
    st.balloons()
    st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

with open("tumheho.mp3", "rb") as audio_file:
    st.audio(audio_file, format="audio/mp3")
