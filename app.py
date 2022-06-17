import streamlit as st # pip install streamlit==0.82.0
import requests
import os

def get_data(url):
	resp = requests.get(url)
	return resp.json()

base_url = "https://bade.kopas.id/translator?versi=2&mode={}&bahasa={}&text={}"


st.set_page_config(page_title='TRANSLASI BAHASA BATAK', layout='wide', initial_sidebar_state='expanded')


Languages = {'Batak':'batak_simalungun','Indonesia':'indonesia'}


st.title("TRANSLASI BAHASA BATAK")

with st.form(key="search form"):

    search_term = st.text_input("Masukkan teks anda disini")
    # text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

    option1 = st.radio('Bahasa asal', ('Batak', 'Indonesia'))
    option2 = st.radio('Bahasa tujuan', ('Batak', 'Indonesia'))

    value1 = Languages[option1]
    value2 = Languages[option2]

    submit_search = st.form_submit_button(label='Translasi')

    if submit_search:
        if search_term == "":
            st.warning('Mohon masukkan teks untuk translasi')

        elif value1 == value2:
            st.warning('Tidak bisa mentranslasi bahasa yang sama')

        elif value1 == "batak_simalungun":
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
            st.success("dalam bahasa {} artinya {}".format(value2,resultfinal))
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
            st.success("dalam bahasa {} artinya {}".format(value2,resultfinal))
            # translate = translator.translate(text,lang_src=value1,lang_tgt=value2)
            # st.info(str(translate))