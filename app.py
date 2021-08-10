import streamlit as st
from main import show_predict_page
from client import show_client_page
from explore import show_explore_page
from PIL import Image

def main():


    menu = ["Acceuil", "Prédiction d'un client", "Prédiction de plusieurs clients", "Exploration des données"]
    choice = st.sidebar.selectbox("MENU", menu)

    if choice == "Acceuil":

        st.title(""" Bienvenue sur l'AppWeb  permettant de prédire le départ des clients d'une banque """)
        st.write("""### DESCRIPTION""")
        st.write("Cette application est destinée aux responsables de banque  qui souhaiterais réduire le nombre de clients qui quittent leurs services de carte de crédit. Vous pouvez anticiper le départ des clients afin de leur fournir de  meilleurs services et ainsi les retenir.")
        image = Image.open('image.png')
        st.image(image, width=None)


    elif choice == "Prédiction d'un client":
        show_predict_page()
    elif choice == "Prédiction de plusieurs clients":
        show_client_page()
    else:
        show_explore_page()

if __name__ == '__main__':
    main()




