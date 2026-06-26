import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

if 'data' not in st.session_state:
    df_fifa = pd.read_csv('datasets/' \
    'CLEAN_FIFA23_official_data.csv', index_col=0)
    df_fifa = df_fifa[df_fifa['Contract Valid Until']>=datetime.today().year]
    df_fifa = df_fifa[df_fifa["Value(£)"]>0]
    df_fifa = df_fifa.sort_values(by='Overall', ascending= False)
    st.session_state['data'] = df_fifa

st.markdown('# FIFA23 OFFICIAL DATASET! ⚽')
st.sidebar.markdown('Desenvolvido por: '
'[Alex Cordeiro](https://github.com/cordeiro04007)'
)

button = st.button('Acesse os dados no Kaggle')
if button:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown("""
            O conjunto de dados de jogadores
            de futebol referente ao período de 2017 a 2023 
            fornece informações abrangentes sobre 
            jogadores profissionais. A base de dados 
            contém uma ampla gama de atributos, 
            incluindo dados demográficos, 
            características físicas, estatísticas de 
            desempenho em campo, detalhes contratuais e 
            vínculos com clubes. Com **mais de 17.000 registros**, 
            este conjunto de dados constitui um 
            recurso valioso para analistas, pesquisadores e 
            entusiastas do futebol interessados ​​em explorar 
            diversos aspectos do esporte, 
            permitindo o estudo de atributos dos jogadores, 
            métricas de desempenho, valor de mercado, 
            análises de clubes, posicionamento em campo e a 
            evolução dos atletas ao longo do tempo.
            """)

