import streamlit as st # pip install streamlit==0.82.0
import requests
import os

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('background.png')  

def get_data(url):
	resp = requests.get(url)
	return resp.json()

base_url = "https://bade.kopas.id/translator?versi=2&mode={}&bahasa={}&text={}"





Languages = {'Lampung':'lampung_a','Indonesia':'indonesia'}



st.header("TRANSLASI BAHASA LAMPUNG DIALEK A")  
st.image('logo.png')

with st.form(key="search form"):

    search_term = st.text_input("Masukkan teks anda disini")
    # text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

    option1 = st.radio('Bahasa asal', ('Lampung', 'Indonesia'))
    option2 = st.radio('Bahasa tujuan', ('Lampung', 'Indonesia'))

    value1 = Languages[option1]
    value2 = Languages[option2]

    submit_search = st.form_submit_button(label='Translasi')

    if submit_search:
        if search_term == "":
            st.warning('Mohon masukkan teks untuk translasi')

        elif value1 == value2:
            st.warning('Tidak bisa mentranslasi bahasa yang sama')

        elif value1 == "lampung_a":
            mode = 1
            # Create Search Query
            search_url = base_url.format(mode, value1, search_term)
            # st.write(search_url)
            data = get_data(search_url)
            # st.success(data)
            resultfinal = ""
            for i in range(len(data['response']['indonesia'])):
                result = data['response']['indonesia'][i]['k']
                resultfinal = resultfinal + " " + result
                
            # st.success(resultfinal)
            st.success("dalam bahasa {} artinya {}".format(option2,resultfinal))
            # translate = translator.translate(text,lang_src=value1,lang_tgt=value2)
            # st.info(str(translate))
        
        elif value1 == "indonesia":
            mode = 2
            # Create Search Query
            search_url = base_url.format(mode, value2, search_term)
            # st.write(search_url)
            data = get_data(search_url)
            # st.success(data)
            resultfinal = ""
            for i in range(len(data['response']['daerah'])):
                # st.write(i)
                result = data['response']['daerah'][i]['k']
                resultfinal = resultfinal + " " + result
                
            # st.success(resultfinal)
            st.success("dalam bahasa {} artinya {}".format(option2,resultfinal))
            # translate = translator.translate(text,lang_src=value1,lang_tgt=value2)
            # st.info(str(translate))
            