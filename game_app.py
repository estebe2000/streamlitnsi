import streamlit as st

st.title("Exemple d'iframe dans Streamlit")

# Afficher une iframe
#iframe_code = """<iframe src="https://kitao.github.io/pyxel/wasm/launcher/?run=estebe2000.streamlit.appp" width="800" height="600"></iframe>"""
#st.markdown(iframe_code, unsafe_allow_html=True)
url = "st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)"
st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)


