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
    st.image("https://thumbs.dreamstime.com/b/keyboard-smashed-angry-user-destroyed-which-will-never-work-again-80297247.jpg", width=200, caption="HSKeyboard")
    
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


# Ajouter un pied de page ou des informations de contact supplémentaires ici si nécessaire

