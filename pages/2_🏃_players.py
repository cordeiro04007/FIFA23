import streamlit as st
import requests

@st.cache_data
def load_image(url):
  headers = {"User-Agent": "Mozilla/5.0"}
  req = requests.get(url, headers=headers)
  return req.content

st.set_page_config(
   page_title="Players",
   page_icon='🏃',
   layout = 'wide'
)

df_fifa = st.session_state['data']

clubes = df_fifa["Club"].unique()
club_option = st.sidebar.selectbox('Clube:', clubes)

df_clubes = df_fifa[(df_fifa['Club']==club_option)]

jogadores = df_clubes["Name"].unique()
jogador_option = st.sidebar.selectbox('Jogador:', jogadores)

df_jogadores = df_fifa[df_fifa['Name']==jogador_option].iloc[0]
# df_jogadores

st.image(load_image(df_jogadores['Photo']))
st.title(df_jogadores['Name'])

st.markdown(f"**Clube**: {df_jogadores['Club']}")
st.markdown(f"**Posição**: {df_jogadores['Position']}")

col1, col2, col3, col4 = st.columns(4)
with col1: 
   st.markdown(
  f"**Idade**: {df_jogadores['Age']} anos")
with col2:
   st.markdown(
  f"**Altura**: {df_jogadores['Height(cm.)']/100} m")
with col3:
   st.markdown(
  f"**Peso**: {df_jogadores['Weight(lbs.)']*0.4535:.2f} kgs")
st.divider()

st.subheader(f"Overall {df_jogadores['Overall']}")
st.progress(int(df_jogadores['Overall']))

col5, col6, col7, col8 = st.columns(4)
col5.metric(
  f"**Valor de mercado**:", f"£ {df_jogadores['Value(£)']:,}")
col6.metric(
  f"**Remuneração semanal**:", f"£ {df_jogadores['Wage(£)']:,}")
col7.metric(
  f"**Cláusula de contrato**", f"£ {df_jogadores['Release Clause(£)']:,}")