import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache
def read():
    df = pd.read_csv('Dataset.csv', sep=(';'), na_values='Unknown')
    df = df.drop('CLIENTNUM', axis = 1)
    return df

df = read()

def show_explore_page():
    st.title("Visualisation des données banquaires")
    st.subheader('Dataset')
    st.write(df)
    st.subheader('Tableau descriptif')
    st.write(df.describe())

    st.subheader('Graphiques Target en fonction des variables pertinentes')
    fig = px.bar(df, x="Attrition_Flag", y="Total_Trans_Ct", color='Attrition_Flag', barmode="group")
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Total_Trans_Amt", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Total_Trans_Ct", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Total_Revolving_Bal", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Total_Ct_Chng_Q4_Q1", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Total_Amt_Chng_Q4_Q1", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Avg_Utilization_Ratio", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)

    fig = px.box(df, x="Attrition_Flag", y="Total_Relationship_Count", color='Attrition_Flag', notched=True)
    st.plotly_chart(fig)













