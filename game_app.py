import streamlit as st

st.title("Exemple d'iframes dans Streamlit")

urls = [
    "https://kitao.github.io/pyxel/wasm/launcher/?run=estebe2000.streamlitnsi.app",
    # Ajoutez d'autres URLs ici
]

for url in urls:
    a = url.split("=")
    b = a[1].split(".")
    titre = b[0]

    # Afficher le titre
    st.subheader(f"Titre : {titre}")

    # Afficher l'iframe
    st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)