import pandas as pd
import numpy as np
import streamlit as st
from pickle import load


def show_predict_page():
    html_temp = """
                <div style = "background-color:#72d8d8;padding:10px, margin:10px">
                <h1 style = "color:white;text-align:center;">PREDICTION DU DEPART D'UN CLIENT</h1>
                </div>
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    model = load(open('model.plk', 'rb'))
    Ratio = ('0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1')
    count = ('1', '2', '3', '4', '5', '6')
    Total_Trans_Amt = st.slider('Montant total de la transaction', 4.20, 5.39, 4.85)
    Total_Trans_Ct = st.slider('Nombre total de transactions', 10, 140, 56)
    Total_Revolving_Bal = st.slider('Solde renouvelable total sur la carte de crédit')
    Total_Ct_Chng_Q4_Q1 = st.slider('Changement du nombre de transactions')
    Total_Amt_Chng_Q4_Q1 = st.slider('Changement du montant de la transaction')
    Avg_Utilization_Ratio = st.selectbox("Taux d'utilisation moyen de la carte", Ratio)
    Total_Relationship_Count = st.selectbox('Nombre total de produits détenus par le client', count)

    values = [Total_Trans_Amt, Total_Trans_Ct, Total_Revolving_Bal, Total_Ct_Chng_Q4_Q1, Total_Amt_Chng_Q4_Q1,
              Avg_Utilization_Ratio, Total_Relationship_Count]

    colum = ['Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Revolving_Bal', 'Total_Ct_Chng_Q4_Q1', 'Total_Amt_Chng_Q4_Q1',
             'Avg_Utilization_Ratio', 'Total_Relationship_Count']

    data = pd.DataFrame(np.array([values]).reshape(1,7), columns=colum)


    ok = st.button('Prédiction')

    if ok:
        st.subheader('Les caractéristiques du client sont:')
        st.write(data)
        prediction = model.predict(data)
        st.subheader('Le compte du client sera')
        #st.write(prediction[0])
        if prediction == 1:
            st.write(' Ouvert')
        else:
            st.write(' Fermé')











