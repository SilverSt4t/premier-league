import streamlit as st
import pandas as pd
import io
from prediction_logic import preprocess_data, train_model, predict_result

st.set_page_config(page_title="Premier League Predictor", layout="centered")

st.markdown("<h1 style='text-align: center;'>⚽ Premier League Predictor ⚽</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Pilih File CSV", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ Data telah dimuat!")

        df_processed, le = preprocess_data(df)
        model = train_model(df_processed)

        col1, col2 = st.columns([1, 1])
        with col1:
            lihat_klasemen = st.button("📋 Lihat Klasemen")
        with col2:
            prediksi = st.button("🔮 Prediksi Pertandingan")

        if lihat_klasemen:
            st.markdown("---")
            st.markdown("<h2 style='text-align: center;'>🏆 Klasemen Saat Ini 🏆</h2>", unsafe_allow_html=True)
            output = io.StringIO()
            output.write("\n\t\tKlasemen Liga Inggris ⚽\n")
            output.write("\t===============================\n")
            output.write("\tPos\tTim\t\tPoin\n")
            output.write("\t-------------------------------\n")
            for i, row in df.iterrows():
                output.write(f"\t{i+1}\t{row['Team']}\t\t{row['Points']}\n")
            output.seek(0)
            st.text(output.read())

        if prediksi:
            st.markdown("---")
            st.markdown("<h2 style='text-align: center;'>🔮 Prediksi Pertandingan 🔮</h2>", unsafe_allow_html=True)
            teams = sorted(df['home_team'].unique())
            home_team = st.selectbox("Pilih Tim Tuan Rumah", teams)
            away_team = st.selectbox("Pilih Tim Tamu", teams)
            if st.button("Prediksi!"):
                if home_team == away_team:
                    st.warning("⚠️ Tim tidak boleh sama!")
                else:
                    result = predict_result(model, home_team, away_team, le)
                    label_map = {'H': 'Tuan Rumah', 'A': 'Tamu', 'D': 'Seri'}
                    hasil = label_map.get(result, result)
                    st.success(f"✅ Prediksi: {hasil} menang!")

    except Exception as e:
        st.error(f"❌ Gagal membaca file CSV: {e}")
else:
    st.warning("⚠️ Belum ada file CSV yang dimuat!")
    st.button("📋 Lihat Klasemen", disabled=True)
    st.button("🔮 Prediksi Pertandingan", disabled=True)