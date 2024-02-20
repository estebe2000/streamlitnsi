import streamlit as st
import time
import random

# Chemin vers le logo et les images d'état
logo_path = "static/images/ban.png"

# Affichage du logo
st.image(logo_path)

# Affichage du message de bienvenue avec le nom du Tamagotchi
if 'tamagotchi_name' in st.session_state and st.session_state['tamagotchi_name']:
    st.title(f"Bienvenue, {st.session_state['user_name']} ! Jouons avec : {st.session_state['tamagotchi_name']}")

# Définition des valeurs par défaut des statistiques du Tamagotchi sur une échelle de 0 à 100
if 'stats' not in st.session_state:
    st.session_state.stats = {
        'Faim': 50,
        'Santé': 100,
        'Bonheur': 80,
        'Propreté': 70,
    }

if 'matches' not in st.session_state:
    st.session_state.matches = 17  # Initialisation du jeu des allumettes avec 17 allumettes

# Fonction pour diminuer aléatoirement les statistiques
def decrease_stats():
    for stat in st.session_state.stats.keys():
        st.session_state.stats[stat] = max(0, st.session_state.stats[stat] - random.randint(1, 2))

# Fonction pour augmenter la statistique, ne dépassant pas 100
def increase_stat(stat, amount):
    st.session_state.stats[stat] = min(100, st.session_state.stats[stat] + amount)

# Vérification si une stat est à zéro
def check_game_over():
    return any(stat == 0 for stat in st.session_state.stats.values())

# Jeu de pile ou face
def play_coin_toss(user_choice):
    outcomes = ['pile', 'face']
    result = random.choice(outcomes)
    st.write(f"Résultat: {result.upper()}")
    if user_choice == result:
        st.success("Vous avez gagné ! Le bonheur de votre Tamagotchi augmente.")
        increase_stat('Bonheur', 10)
    else:
        st.error("Vous avez perdu. Essayez encore !")

# Jeu de pierre-papier-ciseaux
def play_rock_paper_scissors(user_choice):
    choices = ['pierre', 'papier', 'ciseaux']
    result = random.choice(choices)
    st.write(f"Le Tamagotchi choisit: {result.upper()}")
    if user_choice == result:
        st.info("Égalité !")
    elif (user_choice == 'pierre' and result == 'ciseaux') or \
         (user_choice == 'papier' and result == 'pierre') or \
         (user_choice == 'ciseaux' and result == 'papier'):
        st.success("Vous avez gagné ! Le bonheur de votre Tamagotchi augmente.")
        increase_stat('Bonheur', 10)
    else:
        st.error("Vous avez perdu. Essayez encore !")

# Nouvelle fonction pour le jeu des allumettes
def play_matches_game(user_choice):
    st.session_state.matches -= user_choice
    st.write(f"Il reste {st.session_state.matches} allumette(s).")
    if st.session_state.matches <= 0:
        st.error("Vous avez retiré la dernière allumette. Vous avez perdu !")
        # Réinitialisation du jeu des allumettes pour une nouvelle partie
        st.session_state.matches = 17
    else:
        # Logique pour le tour de l'IA (si vous souhaitez ajouter une IA)
        ai_choice = random.randint(1, min(3, st.session_state.matches))
        st.session_state.matches -= ai_choice
        st.write(f"Le Tamagotchi retire {ai_choice} allumette(s). Il reste {st.session_state.matches} allumette(s).")
        if st.session_state.matches <= 0:
            st.success("Le Tamagotchi a retiré la dernière allumette. Vous avez gagné !")
            increase_stat('Bonheur', 20)  # Augmentation du bonheur en cas de victoire
            st.session_state.matches = 17  # Réinitialisation du jeu pour une nouvelle partie

# Interface utilisateur pour le jeu des allumettes
with st.expander("Jouer au jeu des allumettes"):
    if st.session_state['user_name']:  # S'assurer qu'un utilisateur est défini avant de jouer
        user_choice = st.selectbox("Combien d'allumettes voulez-vous retirer ?", (1, 2, 3), key='matches_game')
        if st.button('Retirer les allumettes'):
            play_matches_game(user_choice)

with st.expander("Jouer à pile ou face"):
    if st.session_state['user_name']:  # S'assurer qu'un utilisateur est défini avant de jouer
        user_choice = st.radio("Choisissez pile ou face:", ('pile', 'face'), key='coin_toss')
        if st.button('Lancer la pièce'):
            play_coin_toss(user_choice)

with st.expander("Jouer à pierre-papier-ciseaux"):
    if st.session_state['user_name']:  # S'assurer qu'un utilisateur est défini avant de jouer
        user_choice = st.radio("Choisissez pierre, papier ou ciseaux:", ('pierre', 'papier', 'ciseaux'), key='rps')
        if st.button('Jouer'):
            play_rock_paper_scissors(user_choice)

# Mise à jour des statistiques si 3 secondes se sont écoulées depuis la dernière mise à jour
if 'last_update' not in st.session_state or time.time() - st.session_state.last_update > 10:
    decrease_stats()
    st.session_state.last_update = time.time()

if check_game_over():
    st.markdown("<h1 style='color: red; font-size: 50px;'>PERDU</h1>", unsafe_allow_html=True)
else:
    # Affichage des statistiques et des barres de progression
    for stat in st.session_state.stats:
        col1, col2 = st.columns([2, 3])
        col1.text(f'{stat}: {st.session_state.stats[stat]}')
        col2.progress(st.session_state.stats[stat] / 100)

    # Rerun le script pour actualiser les statistiques
    time.sleep(60)
    st.rerun()
