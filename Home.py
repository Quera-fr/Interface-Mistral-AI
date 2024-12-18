import streamlit as st

# Création d'un titre
st.title('Interface-Mistral-AI')

# Création d'un sous-titre
st.subheader("Mistral AI")

# Création d'une zone de texte
st.write("Introduction à mistral AI")

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
  

# Cration d'un slider 

# Lecture d'un fichier csv avec pandas
