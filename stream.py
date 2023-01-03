import pickle
import streamlit as st 

# load model
jantung_model = pickle.load(open('model_voting.sav', 'rb'))
#judul web
st.title('Prediksi Keselamatan Pasien Penyakit Jantung')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    umur = st.number_input('Umur')

with col2 :
    persentase_darah_yang_meninggalkan_jantung_tiap_kontraksi = st.number_input('Persentase Darah yang meninggalkan Jantung dalam Persentasi di setiap Kontraksi Jantung')

with col1 :
    level_creatinine = st.number_input('Level Serum Creatinine di Darah dalam mg/dL')

with col2 :
    level_sodium = st.number_input('Level Serum Sodium di Darah dalam mEq/L')

with col1 :
    jumlah_hari_untuk_follup = st.number_input('Jumlah Hari menuju Follow Up')


# code untuk prediksi
pred_keselamatan = ''

# membuat tombol untuk prediksi
if st.button('Prediksi Keselamatan'):
    pred_keselamatan = jantung_model.predict([[umur, persentase_darah_yang_meninggalkan_jantung_tiap_kontraksi, level_creatinine, level_sodium, jumlah_hari_untuk_follup]])

    if(pred_keselamatan[0] == 1):
        pred_keselamatan = 'Pasien Meninggal'
    else :
        pred_keselamatan = 'Pasien Selamat'
        
    st.success(pred_keselamatan)