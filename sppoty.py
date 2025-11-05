import streamlit as st
import pandas as pd
import random

st.title("📊 Análise de Dados Musicais - Spotify & YouTube")

# Upload CSV existente ou criar novo
uploaded_file = st.file_uploader("Faça upload do CSV de músicas", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(columns=["Artist", "Track", "Stream", "Views", "Url_youtube"])

st.subheader("Adicionar nova música")
artist = st.text_input("Nome do artista")
track = st.text_input("Nome da música")
url = st.text_input("Link do YouTube da música")

if st.button("Adicionar música"):
    if artist and track and url:
        stream = random.randint(1000000, 200000000)
        views = random.randint(500000, 100000000)
        new_row = {"Artist": artist, "Track": track, "Stream": stream, "Views": views, "Url_youtube": url}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"Música '{track}' adicionada!")
    else:
        st.error("Preencha todos os campos")

st.subheader("🎵 Dados Musicais")
st.dataframe(df)

if not df.empty:
    st.subheader("Top 5 artistas com mais músicas")
    top_artistas = df['Artist'].value_counts().head(5)
    st.table(top_artistas)

    st.subheader("Top 5 músicas com mais views no YouTube")
    top_views = df.sort_values("Views", ascending=False).head(5)[["Track", "Artist", "Views"]]
    st.table(top_views)

    st.subheader("Top 5 artistas com mais streams no Spotify")
    top_streams = df.groupby("Artist")["Stream"].sum().sort_values(ascending=False).head(5).reset_index()
    top_streams.columns = ["Artista", "Total_Streams"]
    st.table(top_streams)

st.subheader("Exportar CSV atualizado")
csv = df.to_csv(index=False).encode("utf-8")
st.download_button("📥 Baixar CSV", data=csv, file_name="musicas_atualizado.csv", mime="text/csv")
