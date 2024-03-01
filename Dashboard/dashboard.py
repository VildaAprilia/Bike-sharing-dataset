import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit App
st.title('Dashboard Pengaruh Hari Libur')

with st.sidebar:
    st.subheader('Bike Sharing :sparkles:')
    st.image("https://www.naikmotor.com/wp-content/uploads/2020/07/e-bike.jpg")
    st.header("Filter dan Pengaturan")
    show_summary = st.checkbox("Tampilkan Ringkasan Informasi")
    show_visualizations_holiday = st.checkbox("Tampilkan data hari libur dengan jumlah sewa sepeda harian")
    show_visualizations_season = st.checkbox("Tampilkan data pengaruh musim terhadap jumlah sewa sepeda harian")
# Load data
url = "https://raw.githubusercontent.com/VildaAprilia/Bike-sharing-dataset/master/Dashboard/all_data.csv"
bike_df = pd.read_csv(url)

# Group data for holiday vs non-holiday
seasonal_data = bike_df.groupby('holiday_day')['cnt_day'].mean()
holiday_names = ['Libur', 'Tidak Libur']

# Group data for seasons
plt.figure(figsize=(10, 6))
sns.boxplot(x="season_day", y="cnt_day", data=bike_df)
plt.title("Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian ")
plt.xlabel("Musim (1: Springer, 2: Summer, 3: Fall, 4: Winter)")
plt.ylabel("Jumlah Sewa Sepeda Harian")
season_plot = plt.gcf()

# Show summary DataFrame information if checked
if show_summary:
    st.subheader("Ringkasan Informasi Dataset")
    st.write("""
    Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan kembali lagi ke posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang mencakup lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena peran pentingnya dalam masalah lalu lintas, lingkungan dan kesehatan.
    Fitur ini mengubah sistem bike sharing menjadi jaringan sensor virtual yang dapat digunakan untuk mendeteksi mobilitas dalam kota. Oleh karena itu, diharapkan sebagian besar peristiwa penting di kota dapat dideteksi melalui pemantauan data ini.
    
    
    """)

#Show Visualization holiday DataFrame information if checked
if show_visualizations_holiday:
    # Display bar chart for holiday vs non-holiday
    st.subheader('Pengaruh Hari Libur Terhadap Jumlah Sewa Sepeda Harian')
    st.bar_chart(seasonal_data)

#Show visualization season DataFrame information if checked
if show_visualizations_season:
    # Display boxplot for seasons
    st.subheader('Pengaruh Musim Terhadap Jumlah Sewa Sepeda Harian')
    st.pyplot(season_plot)

# Estetika tambahan
st.caption('Copyright (c) Vilda Aprilia 2024')
