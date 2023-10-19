import streamlit as st

st.title("Exemple d'iframes dans Streamlit")

# Lire les URLs à partir du fichier texte
with open("urls.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()  # Supprimer les espaces et les sauts de ligne

    a = url.split("=")
    b = a[1].split(".")
    titre = b[0]

    # Afficher le titre
    st.subheader(f"Titre : {titre}")

    # Afficher l'iframe
    st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)