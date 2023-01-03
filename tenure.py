import pickle
import streamlit as st
import joblib

# load model
random_forest = joblib.load(open('random_forest.joblib'))
#judul web
st.title('Prediksi Masa Berlaku Kartu Kredit')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    frekuensi_pembaruan_saldo = st.number_input('Frekuensi Pembaruan Saldo')

with col2 :
    jumlah_trx_pembelian = st.number_input('Jumlah Tranksaksi Pembelian')

with col1 :
    limit_kredit = st.number_input('Limit Kredit')

with col2 :
    jumlah_pembayaran = st.number_input('Jumlah Pembayaran')

with col1 :
    frekuensi_uang_muka = st.number_input('Frekuensi Uang Muka')


# code untuk prediksi
pred_masaberlaku = ''

# membuat tombol untuk prediksi
if st.button('Prediksi Masa Berlaku'):
    pred_masaberlaku = random_forest.predict([[frekuensi_pembaruan_saldo, jumlah_trx_pembelian, limit_kredit, jumlah_pembayaran, frekuensi_uang_muka]])

    if(pred_masaberlaku[0] == 6):
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 6 Bulan'
    elif(pred_masaberlaku[0] == 7):
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 7 Bulan'
    elif(pred_masaberlaku[0] == 8):
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 8 Bulan'
    elif(pred_masaberlaku[0] == 9):
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 9 Bulan'
    elif(pred_masaberlaku[0] == 10):
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 10 Bulan'
    elif(pred_masaberlaku[0] == 11):
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 11 Bulan'
    else:
        pred_masaberlaku = 'Masa Berlaku Kartu Kredit adalah 12 Bulan'
        
    st.success(pred_masaberlaku)
