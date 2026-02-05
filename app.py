
import streamlit as st
import random
import time
from themes import THEMES

# --- Configuration ---
st.set_page_config(
    page_title="Generative Time's Up",
    page_icon="🎨",
    layout="centered"
)

# --- State Management ---
if 'game_state' not in st.session_state:
    st.session_state.game_state = 'START' # START, THEME_REVEAL, GENERATION, GUESSING, RESULT
if 'current_theme' not in st.session_state:
    st.session_state.current_theme = ""

# --- Helper Functions ---
def load_css():
    with open("style.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def next_state(state):
    st.session_state.game_state = state
    st.rerun()

def start_game():
    st.session_state.current_theme = random.choice(THEMES)
    next_state('THEME_REVEAL')

# --- UI Components ---

def render_start():
    st.title("⚡ GEN AI TIME'S UP ⚡")
    st.markdown("""
        <div class='info-box'>
            <h3>Règles</h3>
            <p>1. <b>Démarrer</b> : Obtenez un thème secret.</p>
            <p>2. <b>Générer</b> : Créez une image avec une IA.</p>
            <p>3. <b>Deviner</b> : Montrez l'image, les autres devinent le thème.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("NOUVELLE MANCHE"):
        start_game()

def render_theme_reveal():
    st.title("🤫 THÈME SECRET")
    
    # Placeholder for timer if we want auto-hide later
    
    st.markdown(f"<h1 class='theme-reveal'>{st.session_state.current_theme}</h1>", unsafe_allow_html=True)
    st.caption("Mémorisez ceci ! Ça va disparaître.")
    
    if st.button("CACHER & COMMENCER À GÉNÉRER"):
        next_state('GENERATION')

def render_generation():
    st.title("🎨 PHASE DE GÉNÉRATION")
    st.markdown("""
        <div class='info-box'>
            <p><b>Allez sur votre générateur d'images IA préféré (Midjourney, DALL-E, etc.)</b></p>
            <p>Générez une image basée sur le thème que vous venez de voir.</p>
            <p>Ne montrez le thème à personne !</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.warning("Le thème est caché. Ne trichez pas sauf si vous avez oublié !")
    
    if st.expander("J'ai oublié le thème (Cliquer pour voir)"):
        st.write(st.session_state.current_theme)

    if st.button("J'AI L'IMAGE - PRÊT À FAIRE DEVINER"):
        next_state('GUESSING')

def render_guessing():
    st.title("🤔 PHASE DE DÉCOUVERTE")
    st.markdown("""
        <div class='info-box'>
            <p>Montrez votre image générée aux autres joueurs.</p>
            <p>Peuvent-ils deviner le thème ?</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("RÉVÉLER LA RÉPONSE"):
        next_state('RESULT')

def render_result():
    st.title("✨ LE THÈME ÉTAIT ✨")
    st.markdown(f"<h1 class='theme-reveal'>{st.session_state.current_theme}</h1>", unsafe_allow_html=True)
    
    if st.button("REJOUER"):
        st.session_state.current_theme = ""
        next_state('START')

# --- Main App Flow ---
load_css()

if st.session_state.game_state == 'START':
    render_start()
elif st.session_state.game_state == 'THEME_REVEAL':
    render_theme_reveal()
elif st.session_state.game_state == 'GENERATION':
    render_generation()
elif st.session_state.game_state == 'GUESSING':
    render_guessing()
elif st.session_state.game_state == 'RESULT':
    render_result()

