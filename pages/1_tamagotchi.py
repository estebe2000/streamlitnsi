import streamlit as st
import time
import random

# Chemin vers le logo et les images d'état
logo_path = "static/images/ban.png"
images_path = {
    'perfect': "static/images/perfect.png",
    'Faim': "static/images/faim.png",
    'Santé': "static/images/sante.png",
    'Bonheur': "static/images/bonheur.png",
    'Propreté': "static/images/proprete.png",
}

# Affichage du logo
st.image(logo_path)

# Affichage du message de bienvenue avec le nom du Tamagotchi
if 'tamagotchi_name' in st.session_state and st.session_state['tamagotchi_name']:
    st.title(f"Bienvenue, {st.session_state['user_name']} ! Voici votre Tamagotchi : {st.session_state['tamagotchi_name']}")

# Définition des valeurs par défaut des statistiques du Tamagotchi sur une échelle de 0 à 100
if 'stats' not in st.session_state:
    st.session_state.stats = {
        'Faim': 50,
        'Santé': 100,
        'Bonheur': 80,
        'Propreté': 70,
    }

# Fonction pour diminuer aléatoirement les statistiques
def decrease_stats():
    for stat in st.session_state.stats.keys():
        st.session_state.stats[stat] = max(0, st.session_state.stats[stat] - random.randint(1, 2))

# Fonction pour augmenter la statistique, ne dépassant pas 100
def increase_stat(stat, amount):
    st.session_state.stats[stat] = min(100, st.session_state.stats[stat] + amount)

# Boutons pour augmenter les statistiques
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button('Nourrir'):
        increase_stat('Faim', 10)
with col2:
    if st.button('Soigner'):
        increase_stat('Santé', 10)
with col3:
    if st.button('Jouer'):
        increase_stat('Bonheur', 10)
with col4:
    if st.button('Laver'):
        increase_stat('Propreté', 10)
with col5:
    if st.button('rien'):
        pass

# Fonction pour choisir l'image à afficher en fonction des statistiques
def choose_image():
    if all(value > 50 for value in st.session_state.stats.values()):
        return images_path['perfect']
    else:
        # Trouver la stat la plus basse et son nom
        lowest_stat = min(st.session_state.stats, key=st.session_state.stats.get)
        return images_path[lowest_stat]

# Mise à jour des statistiques et vérification de la condition de fin
if 'last_update' not in st.session_state or time.time() - st.session_state.last_update > 10:
    decrease_stats()
    st.session_state.last_update = time.time()

# Vérification si une stat est à zéro pour terminer le jeu
if any(stat == 0 for stat in st.session_state.stats.values()):
    st.error("PERDU")
else:
    # Affichage des statistiques et des barres de progression
    for stat in st.session_state.stats:
        col1, col2 = st.columns([2, 3])
        col1.text(f'{stat}: {st.session_state.stats[stat]}')
        col2.progress(st.session_state.stats[stat] / 100)

    # Choix et affichage de l'image en fonction de l'état de santé
    image_to_show = choose_image()
    st.image(image_to_show)

    # Rerun le script pour actualiser les statistiques
    time.sleep(10)
    st.rerun()
