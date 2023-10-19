import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Exemple d'iframe dans Streamlit")

url = "https://kitao.github.io/pyxel/wasm/launcher/?run=estebe2000.streamlitnsi.app"

# Récupérer le contenu HTML de la page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire le titre de la page
titre = soup.title.string if soup.title else "Titre non disponible"

# Afficher le titre
st.subheader(f"Titre : {titre}")

# Afficher l'iframe
st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)