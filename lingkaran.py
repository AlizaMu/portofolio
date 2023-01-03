import streamlit as st


st.write("""
# Aplikasi Luas Lingkaran
Ini adalah aplikasi menghitung luas lingkaran sederhana menggunakan Streamlit
""")

jari_jari = st.number_input("Masukkan Jari-jari", 0)

hitung = st.button("Hitung Luas")

if hitung:
    luas = 22/7 * jari_jari * jari_jari
    st.success(f"Luas Lingkarannya adalah {luas}")
    st.ballons()
