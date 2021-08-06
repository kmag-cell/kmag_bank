import streamlit as st
from main import show_predict_page
from client import show_client_page
from explore import show_explore_page

def main():
    st.sidebar.title("AppWeb  permettant de prédire le départ des clients d'une banque")
    st.sidebar.write("""### DESCRIPTION""")
    st.sidebar.write("""Cette application est destinée aux responsables de banque  qui souhaite réduire le nombre de clients qui quittent leurs services 
    de carte de crédit. Vous pouvez anticiper le départ des clients afin de leur fournir de 
    meilleurs services et ainsi les retenir.""")

    menu = ["Prédiction d'un client", "Prediction de plusieurs clients", "Exploration des données"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Prédiction d'un client":
        show_predict_page()
    elif choice == "Prediction de plusieurs clients":
        show_client_page()
    else:
        show_explore_page()

if __name__ == '__main__':
    main()



