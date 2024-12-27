import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Memuat Dataset
file_path = 'DataScience_salaries_2024.csv'  # Sesuaikan path
data = pd.read_csv(file_path)

# Judul Dashboard
st.title("Dashboard Gaji Data Scientist")

# Tampilkan Dataframe
st.subheader("Tabel Data")
st.dataframe(data)

# Membuat boxplot dengan Seaborn dan Matplotlib
st.subheader("Distribusi Gaji berdasarkan Tingkat Pengalaman")
fig, ax = plt.subplots(figsize=(12, 8))
sns.boxplot(x='experience_level', y='salary', data=data, ax=ax, palette='Set2')
ax.set_title('Distribusi Gaji berdasarkan Tingkat Pengalaman', fontsize=18)
ax.set_xlabel('Tingkat Pengalaman', fontsize=14)
ax.set_ylabel('Gaji (USD)', fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)  # Menampilkan figure ke Streamlit
