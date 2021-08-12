import streamlit as st
import pandas as pd
from pickle import load
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode, JsCode
model = load(open('model.plk', 'rb'))
def show_explore_page():
    html_temp = """
                       <div style = "background-color:#72d8d8;padding:10px, margin:10px">
                       <h1 style = "color:white;text-align:center;">CHARGER LES DONNEES</h1>
                       </div>
                       """
    st.markdown(html_temp, unsafe_allow_html=True)
    type_fichier = st.file_uploader(" ", type=["csv", "xls", "txt"])
    if type_fichier is not None:
        with st.beta_expander('Voir les Données'):
            data = pd.read_csv(type_fichier, na_values=["Unknown"], sep=";")
            colonne = ['CLIENTNUM', 'Attrition_Flag','Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Revolving_Bal', 'Total_Ct_Chng_Q4_Q1', 'Total_Amt_Chng_Q4_Q1',
             'Avg_Utilization_Ratio', 'Total_Relationship_Count']
            dat = data[colonne]

            update_mode_value = GridUpdateMode.MODEL_CHANGED
            gb = GridOptionsBuilder.from_dataframe(dat)

            gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)

            gb.configure_selection(selection_mode='multiple', use_checkbox=True, groupSelectsChildren=True)

            gb.configure_grid_options(domLayout='normal')
            gridOptions = gb.build()

            grid_response = AgGrid(dat,
                                   gridOptions=gridOptions,
                                   width='100%',
                                   update_mode=update_mode_value,
                                   enable_enterprise_modules='Enable Enterprise Modules'
                                   )

            dat = grid_response['data']
            selected = grid_response['selected_rows']
            selected_dat = pd.DataFrame(selected)
            #st.write(selected)
            ok = st.button('Prédiction')

            if ok:
                X = selected_dat.drop(
                    ["CLIENTNUM", "Attrition_Flag"], axis=1)
                st.subheader('Les caractéristiques du client sont:')
                AgGrid(X)
                prediction = model.predict(X)
                liste = []
                for i in prediction:
                    if i == 1:
                        msg = "Compte ouvert"
                    elif i == 0:
                        msg = "Compte fermé"

                    liste.append(msg)

                st.subheader("Résultats:")

                final = pd.concat([X, pd.DataFrame(liste, columns=["Predictions"])], axis=1)
                AgGrid(final)
























    # def fetch_data(df):
    #     dummy_data = {
    #         "CLIENTNUM": data['CLIENTNUM'],
    #         "Total_Trans_Amt": data['Total_Trans_Amt'],
    #         "Total_Revolving_Bal": data['Total_Revolving_Bal'],
    #         "Total_Ct_Chng_Q4_Q1": data['Total_Ct_Chng_Q4_Q1'],
    #         "Total_Amt_Chng_Q4_Q1": data['Total_Amt_Chng_Q4_Q1'],
    #         "Avg_Utilization_Ratio": data['Avg_Utilization_Ratio'],
    #         "Total_Relationship_Count": data['Total_Relationship_Count'],
    #         "Total_Trans_Ct": data['Total_Trans_Ct'],
    #          }
    #
    #     return pd.DataFrame(dummy_data)

        # gb = GridOptionsBuilder.from_dataframe(pd.DataFrame(dummy_data))
        # gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
        # gb.configure_selection(selection_mode='multiple', use_checkbox=True, groupSelectsChildren=True)
        # gb.configure_grid_options(domLayout='normal')
        # gridOptions = gb.build()
        # grid_response = AgGrid(
        #     dummy_data,
        #     gridOptions=gridOptions,
        #     width='100%',
        # )


    # if selection_mode:
    #
    #     model = load(open('model.plk', 'rb'))
    #     ok = st.button('Prédiction')
    #
    #     if ok:
    #         st.subheader('Les caractéristiques du client sont:')
    #         st.write(data)
    #         prediction = model.predict(data)
    #         st.subheader('Le compte du client sera')
    #         # st.write(prediction[0])
    #         if prediction == 1:
    #             st.write(' Ouvert')
    #         else:
    #             st.write(' Fermé')














