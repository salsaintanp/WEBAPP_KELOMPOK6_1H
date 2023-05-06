# library yang digunakan

import PIL
import streamlit as st
import requests
import pandas as pd
import time

from PIL import Image
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Membuat menu pada tampilan
with st.sidebar :
   selected = option_menu (
       menu_title='Main Menu',
       options=['Halaman Utama','Tabel Golongan Kelarutan', 'Golongan Hidrokarbon','Golongan Alkohol','Golongan Asam Karboksilat','Golongan Aldehida','Golongan Keton','Golongan Ester','Golongan Amina', 'Golongan Karbohidrat'] )

# Mengatur warna background

base="light"
backgroundColor="#d3fff3"
secondaryBackgroundColor="#fffcb3"


# Halaman Homescreen
if selected == 'Halaman Utama':
    st.markdown("<h1 style='text-align: center; color: red;'>APLIKASI UJI KELARUTAN</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: red;'>(Created by : Kelompok 6-1H)</h3>", unsafe_allow_html=True)
    st.markdown('----')
    st.markdown("<h5 style='text-align: center; color: black;'> Aplikasi yang dapat membantu anda untuk menentukan golongan kelarutan senyawa. </h5>", unsafe_allow_html=True)

    #Menampilkan Animasi pada homescreen
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_1 = 'https://assets6.lottiefiles.com/packages/lf20_hgjskqs0.json'
    lottie_anime_json = load_lottie_url(lottie_animation_1)
    st_lottie(lottie_anime_json, key = 'hello')
    
    #Menampilkan informasi seputar kelarutan
    col1, col2, col3, = st.columns([1,2,1])
    col1.markdown(' # Zat Terlarut?')
    col1.markdown (':green[Zat Terlarut] adalah zat yang dilarutkan ke dalam pelarut. Umumnya, pelarut jumlahnya akan lebih banyak daripada zat terlarutnya. Hal itu supaya zat terlarut bisa tercampur secara homogen.')
    col2.markdown("<h1 style='text-align: center; color:green;'>Apa Itu Kelarutan? </h1>", unsafe_allow_html=True)
    col2.markdown(':green[Kelarutan] atau solubilitas adalah kemampuan suatu zat kimia tertentu, zat terlarut (solute), untuk larut dalam suatu pelarut (solvent) Kelarutan dinyatakan dalam jumlah maksimum zat terlarut yang larut dalam suatu pelarut pada kesetimbangan.')
    col3.markdown(' # Pelarut? ')
    col3.markdown(':green[Pelarut] adalah suatu zat yang melarutkan zat terlarut (cairan, padat atau gas yang berbeda secara kimiawi), menghasilkan suatu larutan. Pelarut biasanya berupa cairan tetapi juga bisa menjadi padat, gas, atau fluida superkritis.')
    
# Menampilkan Tabel Golongan Kelarutan
if selected == 'Tabel Golongan Kelarutan':
    st.markdown("<h2 style='text-align: center; color: green;'> Tabel Klasifikasi Golongan</h2>", unsafe_allow_html=True)
    st.markdown('----')
    def load_data():
        return pd.DataFrame(
              {
            "Kode Golongan": ['S2','SA','SB','S1','A1','A2','B','N','I'],
            "Keterangan": ['Garam-garam asam organik (RCOONa,RSO3Na),asam-asam amino','Asam asam karboksilat yang memiliki atom C≤5','Amina-amina satu gugus fungsi dengan atom C≤6','Alokohol,aldehid,keton,ester,nitril dan amida dengan atom C≤5','Asam-asam organik kuat dengan atom C≥6','Asam-asam organik lemah yang memiliki atom C≥5,ß-diketon,sulfonamida','Amina alifatik dengan atom C≥8,anilin(hanya satu gugus fenil terikat ke N','Alkohol,aldehid,ester dengan satu gugus fungsi,eter dengan jumlah 5<C<9','Hidrokarbon jenuh,haloalkana,arilhalida,diarileter,senyawa aromatik'],
        }
    )

    st.checkbox("Tampilkan tabel dengan format lebar", value=False, key="use_container_width")
    df = load_data()
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
    
#Bagan Klasifikasi Kelarutan

    
# Halaman Golongan Hidrokarbon
if selected == 'Golongan Hidrokarbon':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Hidrokarbon</h2>", unsafe_allow_html=True) 
    st.markdown('----')
    
    #Pelarut hidrokarbon
    
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan hidrokarbon
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button hidrokarbon
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    
    # Penentuan Kelarutan Hidrokarbon
    if pilihan_pelarut=='Air'and number>=1:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] :blue[(silahkan lanjutkan uji dengan pelarut NaOH)] ')
    elif pilihan_pelarut=='NaOH'and number>=1:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] :blue[(silahkan lanjutkan uji dengan pelarut HCl)] ')
    elif pilihan_pelarut=='HCl'and number>=1:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut H2SO4)] ')
    elif pilihan_pelarut=='H2SO4'and number>=1 :
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] Hidrokarbon masuk kedalam golongan kelarutan :red[I]')
    
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello')  

    
#Golongan Alkohol
if selected  == 'Golongan Alkohol':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Alkohol</h2>", unsafe_allow_html=True)
    st.markdown('----')
     
    
    #Pelarut alkohol
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan alkohol
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button alkohol
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    # Kelarutan alkohol S1
    if pilihan_pelarut=='Air'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] :blue[(silahkan lanjutkan uji dengan pelarut Eter)]')
    elif pilihan_pelarut=='Eter'and 1<=number:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Alkohol masuk kedalam golongan kelarutan :red[S1]')    
    
    elif pilihan_pelarut=='Air'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] ')
    elif pilihan_pelarut=='NaOH'and 1<=number:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] :blue[(silahkan lanjutkan uji dengan pelarut NaOH)]')
    elif pilihan_pelarut=='HCl'and 1<=number:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] :blue[(silahkan lanjutkan uji dengan pelarut NaOH)]')
    elif pilihan_pelarut=='H2SO4'and 1<=number :
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Alkohol masuk kedalam golongan kelarutan :red[N]')
    
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
         
#Golongan Asam Karboksilat
if selected == 'Golongan Asam Karboksilat':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Asam Karboksilat</h2>", unsafe_allow_html=True)
    st.markdown('----')
    
    #Pelarut Asam Karboksilat
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan Asam Karboksilat
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button Asam Karboksilat
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    # Kelarutan Asam Karboksilat
    if pilihan_pelarut=='Air'and 1<=number<=10:
        st.success (f'Hasil uji kelarutan adalah :red[LARUT] :blue[(silahkan lanjutkan uji dengan pelarut Eter)]')
    elif pilihan_pelarut=='Eter'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Asam Karboksilat masuk kedalam golongan kelarutan :red[SA]')
    
    elif pilihan_pelarut=='Air'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut NaOH)] ')
    elif pilihan_pelarut=='NaOH'and 1<=number:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT]Asam Karboksilat masuk kedalam golongan kelarutan :red[A1]')
   
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
    
#Golongan Aldehida
if selected == 'Golongan Aldehida':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Aldehida</h2>", unsafe_allow_html=True)
    st.markdown('----')

    #Pelarut Aldehida
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan Aldehida
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button Aldehida
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    # Kelarutan Aldehida
    if pilihan_pelarut=='Air'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT]:blue[(silahkan lanjutkan uji dengan pelarut Eter)]')
    elif pilihan_pelarut=='Eter'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Aldehida masuk kedalam golongan kelarutan :red[S1]')
                 
    elif pilihan_pelarut=='Air'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut NaOH)] ')
    elif pilihan_pelarut=='NaOH'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut HCl)] ')
    elif pilihan_pelarut=='HCl'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut H2SO4)]  ')
    elif pilihan_pelarut=='H2SO4'and 1<=number>10 :
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Aldehida masuk kedalam golongan kelarutan :red[N]')
   
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
         
     
#Golongan Keton
if selected == 'Golongan Keton':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Keton</h2>", unsafe_allow_html=True)
    st.markdown('----')
    
    #Pelarut Keton      
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan Keton
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button Keton
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    # Kelarutan Keton
    if pilihan_pelarut=='Air'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT]:blue[(silahkan lanjutkan uji dengan pelarut Eter)]  ')
    elif pilihan_pelarut=='Eter'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Keton masuk kedalam golongan kelarutan :red[S1]')
    
    elif pilihan_pelarut=='Air'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] silahkan lanjutkan uji dengan pelarut NaOH)]')
    elif pilihan_pelarut=='NaOH'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] silahkan lanjutkan uji dengan pelarut Hcl)]')
    elif pilihan_pelarut=='HCl'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] silahkan lanjutkan uji dengan pelarut H2SO4)]')
    elif pilihan_pelarut=='H2SO4'and 1<=number>10 :
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Keton masuk kedalam golongan kelarutan :red[N]') 
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
         
    
    
     
#Golongan Ester
if selected == 'Golongan Ester':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Ester</h2>", unsafe_allow_html=True)
    st.markdown('----')
    
    #Pelarut Ester    
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan Ester
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button Ester
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    # Kelarutan Ester
    if pilihan_pelarut=='Air'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT]:blue[(silahkan lanjutkan uji dengan pelarut Eter)] ')
    elif pilihan_pelarut=='Eter'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Alkohol masuk kedalam golongan kelarutan :red[S1]')
    
    elif pilihan_pelarut=='Air'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut NaOH)] ')
    elif pilihan_pelarut=='NaOH'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut HCl)] ')
    elif pilihan_pelarut=='HCl'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut H2SO4)] ')
    elif pilihan_pelarut=='H2SO4'and 1<=number>10 :
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Ester masuk kedalam golongan kelarutan :red[N]')
    
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
         
      
#Golongan Amina
if selected == 'Golongan Amina':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Amina</h2>", unsafe_allow_html=True)
    st.markdown('----')  
    
    #Pelarut Amina       
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan Amina
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button Amina
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
  
    # Kelarutan Amina
    if pilihan_pelarut=='Air'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] :blue[(silahkan lanjutkan uji dengan pelarut Eter)]')
    elif pilihan_pelarut=='Eter'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] Amina masuk kedalam golongan kelarutan :red[SB]')
    
    elif pilihan_pelarut=='Air'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] :blue[(silahkan lanjutkan uji dengan pelarut NaOH)]')
    elif pilihan_pelarut=='NaOH'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT]:blue[(silahkan lanjutkan uji dengan pelarut HCl)] ')
    elif pilihan_pelarut=='HCl'and 1<=number>10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT]Amina masuk kedalam golongan kelarutan :red[B] ')
   
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
         
      
#Golongan Karbohidrat
if selected == 'Golongan Karbohidrat':
    st.markdown("<h2 style='text-align: center; color: green;'> Uji Kelarutan Golongan Karbohidrat</h2>", unsafe_allow_html=True)
    st.markdown('----')
    
    #Pelarut Karbohidrat
           
    pilihan_pelarut = st.selectbox(
    'Pelarut apa yang akan anda gunakan?',
    ('Air','Eter','NaOH','HCl','H2SO4'))
    st.write(':blue[pelarut yang anda pilih adalah]', pilihan_pelarut)
    #Jumlah tetesan Karbohidrat
    number = st.number_input('Masukkan jumlah tetesan')
    if number<=20:
     st.write(f':blue[Jumlah tetesan adalah] {number} ')
    else :
     st.error('Maksimal 20 tetes', icon="🚨")
    # Button Karbohidrat
    tombol = st.button('Lihat hasil uji')
    with st.spinner('Memproses Hasil UJi...'):
        time.sleep(2)
    # Kelarutan Karbohidrat
    if pilihan_pelarut=='Air'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[LARUT] ')
    elif pilihan_pelarut=='Eter'and 1<=number<=10:
     st.success (f'Hasil uji kelarutan adalah :red[TIDAK LARUT] Karbohidrat masuk kedalam golongan kelarutan :red[S2]')    
  
        
    def load_lottie_url(url:str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_animation_2 = 'https://assets7.lottiefiles.com/packages/lf20_tayubg7l.json'
    lottie_anime_json_2 = load_lottie_url(lottie_animation_2)
    st_lottie(lottie_anime_json_2, key = 'hello') 
         
