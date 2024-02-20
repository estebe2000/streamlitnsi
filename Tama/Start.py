# Ceci est un fichier placeholder pour app.py 
import streamlit as st

# Chemin vers le logo, ajusté selon votre dossier statique
logo_path = "static/images/logo.png"

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(logo_path)  # Ajustez la largeur selon la taille de votre logo


# Initialisation des variables de session si elles n'existent pas
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''
if 'tamagotchi_name' not in st.session_state:
    st.session_state['tamagotchi_name'] = ''

# Fonction pour enregistrer les noms sans appeler st.rerun()
def save_names():
    st.session_state['user_name'] = user_name
    st.session_state['tamagotchi_name'] = tamagotchi_name

# Affichage des champs de saisie seulement si les noms n'ont pas encore été saisis
if st.session_state['user_name'] == '' or st.session_state['tamagotchi_name'] == '':
    with st.form("names_form"):
        user_name = st.text_input("Votre nom", value=st.session_state['user_name'])
        tamagotchi_name = st.text_input("Nom de votre Tamagotchi", value=st.session_state['tamagotchi_name'])
        submitted = st.form_submit_button("Commencer")

    if submitted:
        save_names()
        # Au lieu de rerun, afficher un message ou rediriger l'utilisateur
        st.success(f"Bienvenue, {st.session_state['user_name']} ! Votre Tamagotchi, {st.session_state['tamagotchi_name']}, est prêt.")
else:
    st.write(f"Bienvenue, {st.session_state['user_name']} !")
    st.write(f"Voici votre Tamagotchi : {st.session_state['tamagotchi_name']}")

