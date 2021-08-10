import streamlit as st
import pandas as pd
import numpy as np
from pickle import load
import sqlite3


def connecte_data():
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute('SELECT Total_Relationship_Count, Total_Revolving_Bal, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio, Attrition_Flag FROM Dataset')
    data = cur.fetchall()
    cur.close()
    return data


def aleatoire(nbre):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute('SELECT Total_Relationship_Count, Total_Revolving_Bal, Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio, Attrition_Flag FROM Dataset ORDER BY RANDOM() LIMIT "{}"'.format(nbre))
    data = cur.fetchall()
    return data

def show_client_page():
    st.title("PREDICTION DU DEPART DE PLUSIEURS CLIENT")
    row = connecte_data()
    with st.beta_expander('Voir le Dataset'):
        data = pd.DataFrame(row, columns=["Total_Relationship_Count", "Total_Revolving_Bal", "Total_Amt_Chng_Q4_Q1", "Total_Trans_Amt", "Total_Trans_Ct", "Total_Ct_Chng_Q4_Q1", "Avg_Utilization_Ratio", "Attrition_Flag"])
        st.dataframe(data)

    val = st.number_input('Nombre de client', min_value=2, max_value=30, step=1)
    button = st.button("Prédiction")
    if button:
        result = aleatoire(val)
        resultat = pd.DataFrame(result, columns=["Nombre total de produits détenus par le client", "Solde renouvelable total sur la carte de crédit", "Changement du montant de la transaction", "Montant total de la transaction", "Nombre total de transactions", "Changement du nombre de transactions", "Taux d'utilisation moyen de la carte", "Resultats ciblés"])
        #st.dataframe(resultat)
        liste = []
        for i in range(resultat.shape[0]):
            X = resultat.iloc[i, :-1]
            X = np.array(X).reshape(1, -1)
            model = load(open('model.plk', 'rb'))
            prediction = model.predict(X)
            if prediction == 1:
                 msg='Compte ouvert'
            else:
                 msg = 'Compte fermé'
            liste.append(msg)
        #st.write(liste)
        data2 = pd.DataFrame(liste, columns=["Predictions"])
        #st.dataframe(data2)
        #with st.beta_expander('Voir le Dataset et le resultat'):
        final = pd.concat([resultat,data2 ], axis = 1)
        st.dataframe(final)












