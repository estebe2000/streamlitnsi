import streamlit as st
import requests

st.title("Exemple d'iframe dans Streamlit")

url = "https://kitao.github.io/pyxel/wasm/launcher/?run=estebe2000.streamlitnsi.app"

# Récupérer le contenu HTML de la page
response = requests.get(url)
content = response.text

# Extraire le titre de la page en recherchant la balise <title>
start_index = content.find("<title>") + len("<title>")
end_index = content.find("</title>", start_index)
titre = content[start_index:end_index] if start_index != -1 and end_index != -1 else "Titre non disponible"

# Afficher le titre
st.subheader(f"Titre : {titre}")

# Afficher l'iframe
st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)