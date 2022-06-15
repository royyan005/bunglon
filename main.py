import streamlit as st # pip install streamlit==0.82.0
import requests
import os

port = os.getenv('PORT', default=8000)

def get_data(url):
	resp = requests.get(url)
	return resp.json()

base_url = "https://bade.kopas.id/translator?versi=2&mode=2&bahasa={}&text={}"


st.set_page_config(page_title='TRANSLASI BAHASA BATAK', layout='wide', initial_sidebar_state='expanded')


Languages = {'Batak':'batak_simalungun','Indonesia':'indonesia'}


st.title("TRANSLASI BAHASA BATAK")

with st.form(key="search form"):

    search_term = st.text_input("Enter your text here")
    # text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")

    option1 = st.selectbox('Input language',
                      ('Batak', 'Indonesia'))

    value1 = Languages[option1]
    # value2 = Languages[option2]

    submit_search = st.form_submit_button(label='Search')

    if submit_search:
        if search_term == "":
            st.warning('Please **enter text** for translation')

        else:
            # Create Search Query
            search_url = base_url.format(value1,search_term)
			# st.write(search_url)
            data = get_data(search_url)
            # st.success(data)
            # for i in range(len(data['response']['daerah'])):
            #     st.success(i)
            #     result = data['response']['daerah'][i]['k']
            #     resultfinal = result + result
            st.success("dalam bahasa {} artinya {}".format(value1,data['response']['daerah'][0]['k']))
            # translate = translator.translate(text,lang_src=value1,lang_tgt=value2)
            # st.info(str(translate))
