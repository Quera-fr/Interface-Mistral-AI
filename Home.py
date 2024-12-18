import streamlit as st

# Création d'un titre
st.title('Interface-Mistral-AI')

# Création d'un sous-titre
st.subheader("Mistral AI")

# Création d'une zone de texte
st.write("Introduction à mistral AI")


if st.checkbox('Afficher le contenu'):
  st.write("""
  
  # Titre
  ## Sous-titre
  
  **Text**
  
    `print("Hello World")`
  
  """)

# Zone de saisie de texte
user_name = st.text_input("Quel est votre nom ?")

# Création d'un bouton
if st.button("Press OK"):
  st.write(user_name)


# Image
st.sidebar.image('https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png')

# Video
st.sidebar.video("https://www.youtube.com/watch?v=sgnrL7yo1TE")

# Cration d'un slider 
st.slider("Quel est votre age ?", [18, 99])

# Lecture d'un fichier csv avec pandas
