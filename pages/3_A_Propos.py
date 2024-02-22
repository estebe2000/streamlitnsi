import streamlit as st

# Configuration de la page
st.set_page_config(page_title="À propos du Créateur", page_icon=":smiley:", layout="wide")

# CSS personnalisé pour styliser la page
st.markdown("""
<style>
.bold {
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Entête
st.title("À propos du Créateur")

# Conteneur pour la présentation
col1, col2 = st.columns([1, 2])

# Colonne de l'image et des informations de base
with col1:
    # Image du créateur (remplacez l'URL par une image pertinente)
    st.image("https://1000logos.net/wp-content/uploads/2020/09/Konami-Logo-1986-500x313.png", width=200, caption="HSKeyboard")
    
    # Informations de base
    st.markdown("""
    **Nom:** HSKeyboard  
    **Âge:** 23  
    **Nationalité:** Français  
    """)
    
    # Compétences
    st.markdown("""
    **Compétences:**  
    - Python  
    - Streamlit  
    - Développement Web  
    - Intelligence Artificielle  
    """, unsafe_allow_html=True)

# Colonne de la biographie
with col2:
    st.markdown("""
    **Biographie:**  
    HSKeyboard, ancien élève du lycée Jean Prevost à Montivilliers, a bénéficié d'une expérience formidable en passant par l'excellente classe de NSI (Numérique et Sciences Informatiques) sous la houlette de Monsieur PYTEL. Cette période a été déterminante dans sa trajectoire, lui permettant de développer une passion profonde pour le développement logiciel, en particulier pour le Python et les technologies web modernes. Spécialisé dans le développement d'applications interactives et l'intelligence artificielle, HSKeyboard cherche constamment à repousser les limites de la créativité et de l'efficacité. En dehors du codage, HSKeyboard aime explorer les dernières tendances technologiques, jouer aux échecs, et contribuer à des projets open source.
    """, unsafe_allow_html=True)


# Configuration de la session state pour le Code Konami
if 'konami_sequence' not in st.session_state:
    st.session_state.konami_sequence = []

# Définition de la séquence du Code Konami
konami_code = ['up', 'up', 'down', 'down', 'left', 'right', 'left', 'right', 'b', 'a']

# Fonction pour vérifier la séquence du Code Konami
def check_konami(input):
    st.session_state.konami_sequence.append(input)
    # Vérifier si la séquence correspond au Code Konami
    if st.session_state.konami_sequence[-len(konami_code):] == konami_code:
        st.balloons()
        st.write("May the Force be with you")
        st.session_state.konami_sequence = []  # Réinitialiser la séquence

# Widgets pour saisir le Code Konami
st.write("???")
cols = st.columns(5)
with cols[0]:
    st.button("↑", key="up1", on_click=check_konami, args=('up',))
    st.button("↓", key="down1", on_click=check_konami, args=('down',))
with cols[1]:
    st.button("↑", key="up2", on_click=check_konami, args=('up',))
    st.button("↓", key="down2", on_click=check_konami, args=('down',))
with cols[2]:
    st.button("←", key="left", on_click=check_konami, args=('left',))
    st.button("→", key="right", on_click=check_konami, args=('right',))
with cols[3]:
    st.button("←", key="left2", on_click=check_konami, args=('left',))
    st.button("→", key="right2", on_click=check_konami, args=('right',))
with cols[4]:
    st.button("B", on_click=check_konami, args=('b',))
    st.button("A", on_click=check_konami, args=('a',))

# Note: Les boutons sont placés pour simuler visuellement la disposition du Code Konami,
# mais l'utilisateur doit cliquer dans l'ordre correct.

