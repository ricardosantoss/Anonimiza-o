import streamlit as st
import pandas as pd

# Carregar os dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("anonimizados.csv")

df = carregar_dados()

st.title("🔍 Comparador de Petições - Original vs. Anonimizado")
st.markdown("Este app mostra lado a lado o conteúdo original e o texto anonimizado.")

# Busca por termo
termo = st.text_input("🔎 Buscar termo no conteúdo (original ou anonimizado):")

# Aplicar filtro
if termo:
    mask = df['conteudo'].str.contains(termo, case=False, na=False) | df['conteudo_anonimizado'].str.contains(termo, case=False, na=False)
    filtrado = df[mask]
else:
    filtrado = df.copy()

# Escolher arquivo
arquivo_selecionado = st.selectbox("📂 Escolha o documento:", filtrado['arquivo'].tolist())

# Exibir conteúdos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Original")
    texto_original = filtrado[filtrado['arquivo'] == arquivo_selecionado]['conteudo'].values[0]
    st.text_area("Texto original", texto_original, height=500)

with col2:
    st.subheader("🛡️ Anonimizado")
    texto_anon = filtrado[filtrado['arquivo'] == arquivo_selecionado]['conteudo_anonimizado'].values[0]
    st.text_area("Texto anonimizado", texto_anon, height=500)
