import streamlit as st

st.title("Exemple d'iframe dans Streamlit")

# Afficher une iframe
url = "https://kitao.github.io/pyxel/wasm/launcher/?run=estebe2000.streamlitnsi.app"
st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)

