import streamlit as st
import requests
import base64
### CONFIGURANDO LAYOUT PÁGINA ###
st.set_page_config(
   page_title="Teams",
   page_icon='⚽',
   layout = 'wide'
)

### FUNÇÃO PARA RENDERIZAR A IMAGEM PÁGINA ###
@st.cache_data
def load_image_64(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()

def preprocess_row(url):
    if isinstance(url, str) and url.startswith("http"):
        return load_image_64(url)
    return url

### CÓDIGO ###
df_fifa = st.session_state['data']

clubes = df_fifa["Club"].unique()
club_option = st.sidebar.selectbox('Clube:', clubes)

df_filtered = df_fifa[(df_fifa['Club']== club_option)].set_index('Name')

st.image(load_image_64(df_filtered.iloc[0]['Club Logo']))
st.markdown(f'## {club_option}')

columns = [
  'Age', 'Photo','Club Logo','Flag','Overall','Value(£)',
  'Wage(£)','Joined','Height(cm.)','Weight(lbs.)',
  'Contract Valid Until','Release Clause(£)'
]

df_filtered["Photo"] = df_filtered["Photo"].apply(preprocess_row)
df_filtered["Flag"] = df_filtered["Flag"].apply(preprocess_row)
df_filtered["Club Logo"] = df_filtered["Club Logo"].apply(preprocess_row)

df_columns_filtered = st.dataframe(
  df_filtered[columns],
  column_config= {
    'Overall':st.column_config.ProgressColumn(
      'Overall',format = '%d', min_value=0, max_value=100
      ),
      'Wage(£)':st.column_config.ProgressColumn(
      'Weekly Wage',format = '£%f', min_value=0, max_value=df_filtered['Wage(£)'].max(),
      ),
      'Photo': st.column_config.ImageColumn(),
      'Flag': st.column_config.ImageColumn(),
      'Club Logo': st.column_config.ImageColumn()
    }
    )

