import requests
import streamlit as st
from PIL import Image
import io
import pandas as pd
import os
from urllib.parse import urlparse, parse_qs

# Méthode 1: Moyenne des composantes RGB
def average_grayscale(image):
    pixels = image.convert('RGB')
    new_image = Image.new("RGB", image.size)
    new_pixels = new_image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel_value = pixels.getpixel((i,j))
            avg = sum(pixel_value) // 3
            new_pixels[i,j] = (avg, avg, avg)
            
    return new_image

# Méthode 2: Pondération des composantes RGB
def weighted_grayscale(image):
    pixels = image.convert('RGB')
    new_image = Image.new("RGB", image.size)
    new_pixels = new_image.load()
    
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels.getpixel((i,j))
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            new_pixels[i,j] = (gray, gray, gray)
            
    return new_image


# Fonction pour créer une image inversée (négative)
def invert_pixels(image):
    pixels = image.convert('RGB')
    new_image = Image.new("RGB", image.size)
    new_pixels = new_image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels.getpixel((i, j))
            new_pixels[i, j] = (255 - r, 255 - g, 255 - b)

    return new_image

# Fonction pour créer une image miroir
def mirror_pixels(image):
    pixels = image.convert('RGB')
    new_image = Image.new("RGB", image.size)
    new_pixels = new_image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            new_pixels[image.size[0] - i - 1, j] = pixels.getpixel((i, j))

    return new_image


def compress_image(image, max_width=800):
    # Redimensionnement proportionnel pour que la largeur ne dépasse pas max_width
    base_width = image.size[0]
    base_height = image.size[1]
    new_height = int((max_width / base_width) * base_height)
    
    # Utilisez Image.LANCZOS pour le redimensionnement
    image = image.resize((max_width, new_height), Image.LANCZOS)
    
    # Ajuster les DPI pour le web (72 DPI est souvent utilisé pour le web)
    image.info['dpi'] = (72, 72)
    
    return image

def get_image_size_and_bytes(image):
    # Obtenir les dimensions de l'image
    dimensions = image.size  # (largeur, hauteur)
    
    # Obtenir le poids (taille du fichier) de l'image
    byte_io = io.BytesIO()
    image.save(byte_io, format='PNG')
    image_size = len(byte_io.getvalue()) / 1024  # Taille en kilo-octets
    byte_io.close()
    
    return dimensions, image_size

# Titre de l'application
st.title('Mon Petit Site en Streamlit')

# Utilisation d'un état pour suivre la page actuelle
if 'page' not in st.session_state:
    st.session_state['page'] = 'Accueil'

# Création de la barre de navigation en haut
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('Accueil'):
        st.session_state['page'] = 'Accueil'
with col2:
    if st.button('Convert'):
        st.session_state['page'] = 'Convert'
with col3:
    if st.button('Compress'):
        st.session_state['page'] = 'Compress'
with col4:
    if st.button('Infos'):
        st.session_state['page'] = 'Infos'

# Affichage du contenu en fonction de la page sélectionnée
if st.session_state['page'] == 'Accueil':
    st.header('Page d\'Accueil')
    st.write('Bienvenue sur la page d\'accueil de mon site.')

    # Affichage d'un message
    st.subheader('Message du jour :')
    st.write('Bonjour, bienvenue sur mon site !!!')

    # Affichage d'une image
    st.subheader('Image du jour :')
    image = Image.open("./image.jpg")  # Remplacez par le chemin vers votre image
    st.image(image, caption='Image du jour', use_column_width=True)

    # Affichage des 100 premières décimales de Pi
    # Les 100 premières décimales de Pi
    pi_100_decimals = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

    # Utilisation dans le code Streamlit
    st.write(f"Pi avec {len(pi_100_decimals.split('.')[1])} décimales : {pi_100_decimals}")

    # Ajout d'un tableau
    st.subheader('Tableau du jour :')
    df = pd.DataFrame({
        'Nom': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22],
        'Ville': ['Paris', 'Lyon', 'Marseille']
    })
    st.table(df)

    



elif st.session_state['page'] == 'Convert':
    st.header('Page de Conversion')
    uploaded_file = st.file_uploader("Envoyez une image", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        input_image = Image.open(uploaded_file)
        st.image(input_image, caption='Image envoyée', use_column_width=True)
        
        option = st.selectbox(
            'Que voulez-vous faire ?',
            ('Choisissez une option', 'Inverser les couleurs', 'Convertir en noir et blanc', 'Image miroir')
        )

        # Tampon pour l'image à télécharger
        buffer = io.BytesIO()

        if option == 'Inverser les couleurs':
            transformed_image = invert_pixels(input_image)
            transformed_image.save(buffer, format="PNG")
            st.image(transformed_image, caption='Image Inversée', use_column_width=True)
        
        elif option == 'Convertir en noir et blanc':
            method = st.selectbox("Choisissez une méthode de conversion", ["Moyenne", "Pondération"])
            if method == "Moyenne":
                transformed_image = average_grayscale(input_image)
            else:
                transformed_image = weighted_grayscale(input_image)
            transformed_image.save(buffer, format="PNG")
            st.image(transformed_image, caption='Image en noir et blanc', use_column_width=True)
        
        elif option == 'Image miroir':
            transformed_image = mirror_pixels(input_image)
            transformed_image.save(buffer, format="PNG")
            st.image(transformed_image, caption='Image Miroir', use_column_width=True)

        # Bouton de téléchargement pour l'image transformée
        if option != 'Choisissez une option':
            buffer.seek(0)
            st.download_button(
                label="Télécharger l'image transformée",
                data=buffer,
                file_name=f"{option}_image.png",
                mime="image/png"
            )
       

elif st.session_state['page'] == 'Compress':
    st.header('Page de Compression')
    st.write('Ici, vous pouvez compresser des fichiers.')
    
    uploaded_file = st.file_uploader("Choisissez une image", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        input_image = Image.open(uploaded_file)
        
        dimensions, image_size = get_image_size_and_bytes(input_image)
        st.write(f"Dimensions de l'image originale : {dimensions[0]} x {dimensions[1]} pixels")
        st.write(f"Taille de l'image originale : {image_size:.2f} kilo-octets")
        
        st.image(input_image, caption='Image Originale', use_column_width=True)
        
        # Appeler la fonction de compression
        compressed_image = compress_image(input_image)
        
        compressed_dimensions, compressed_image_size = get_image_size_and_bytes(compressed_image)
        st.write(f"Dimensions de l'image compressée : {compressed_dimensions[0]} x {compressed_dimensions[1]} pixels")
        st.write(f"Taille de l'image compressée : {compressed_image_size:.2f} kilo-octets")
        
        # Afficher l'image compressée
        st.image(compressed_image, caption='Image Compressée', use_column_width=True)
        # Bouton pour télécharger l'image compressée
        buffer = io.BytesIO()
        compressed_image.save(buffer, format="PNG")
        buffer.seek(0)
        st.download_button(
            label="Télécharger l'image compressée",
            data=buffer,
            file_name="compressed_image.png",
            mime="image/png"
        )

elif st.session_state['page'] == 'Infos':
    st.header('Page d\'Infos')

    # Fichier pour stocker les URL
    url_file_path = "urls.txt"

    # Charger le fichier contenant les URL
    uploaded_file = st.file_uploader("Choisir un fichier texte contenant des URL", type=["txt"])

    if uploaded_file is not None:
        # Lire le contenu du fichier
        content = uploaded_file.read().decode("utf-8")
        
        # Séparer les URL par des sauts de ligne
        urls = content.strip().split("\n")
        
        for i, url in enumerate(urls):
            # Parse l'URL pour extraire les paramètres
            parsed_url = urlparse(url)
            params = parse_qs(parsed_url.query)
            
            # Trouver le nom à afficher
            name = params.get("run", ["Inconnu"])[0]
            
            # Afficher le titre et l'URL dans un iframe
            st.write(f"Nom: {name}")
            st.write(f"URL {i+1}: {url}")
            st.markdown(f'<iframe src="{url}" width="800" height="600"></iframe>', unsafe_allow_html=True)

    # Champ de saisie pour une nouvelle URL
    new_url = st.text_input("Entrer une nouvelle URL:")

    # Bouton pour ajouter la nouvelle URL
    if st.button("Ajouter URL"):
        # Ajouter la nouvelle URL au fichier
        with open(url_file_path, "a") as f:
            f.write(new_url + "\n")
        st.success(f"URL ajoutée avec succès : {new_url}")