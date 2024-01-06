import streamlit as st

# Fonction pour la calculatrice de base
def calculator():
    st.header("Calculatrice de base")
    # Inclure ici le code de la calculatrice

# Fonction pour le convertisseur d'unités
def unit_converter():
    st.header("Convertisseur d'unités")
    # Inclure ici le code du convertisseur d'unités

# Fonction pour le générateur de mots de passe
def password_generator():
    st.header("Générateur de mots de passe")
    # Inclure ici le code du générateur de mots de passe

# Fonction pour le suivi des dépenses
def expense_tracker():
    st.header("Suivi des dépenses")
    # Inclure ici le code du suivi des dépenses

# Fonction pour le quiz interactif
def interactive_quiz():
    st.header("Quiz interactif")
    # Inclure ici le code du quiz interactif

# Fonction pour le générateur de graphiques
def chart_generator():
    st.header("Générateur de graphiques")
    # Inclure ici le code du générateur de graphiques

# Fonction pour le convertisseur de devises
def currency_converter():
    st.header("Convertisseur de devises")
    # Inclure ici le code du convertisseur de devises

# Fonction pour l'horloge mondiale
def world_clock():
    st.header("Horloge mondiale")
    # Inclure ici le code de l'horloge mondiale

# Fonction pour le journal de bord
def journal():
    st.header("Journal de bord")
    # Inclure ici le code du journal de bord

# Interface principale
st.title("Projets en Streamlit")

# Liste des projets
projects = {
    "Calculatrice de base": calculator,
    "Convertisseur d'unités": unit_converter,
    "Générateur de mots de passe": password_generator,
    "Suivi des dépenses": expense_tracker,
    "Quiz interactif": interactive_quiz,
    "Générateur de graphiques": chart_generator,
    "Convertisseur de devises": currency_converter,
    "Horloge mondiale": world_clock,
    "Journal de bord": journal
}

# Sélection du projet à afficher
selected_project = st.sidebar.selectbox("Sélectionnez un projet :", list(projects.keys()))

# Appel de la fonction correspondant au projet sélectionné
if selected_project in projects:
    projects[selected_project]()
