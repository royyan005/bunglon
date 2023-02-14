import streamlit as st # pip install streamlit==0.82.0
import requests
import os
import base64
from  PIL import Image
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

st.image('logo.png')

#sidebar
with st.sidebar:
    choose = option_menu("App Gallery", ["Translasi", "About", "History" , "Contact"],
                         icons=['translate', 'house','book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
logo = Image.open(r'logo.png')
profile = Image.open(r'background.png')
if choose == "About":
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Creator</p>', unsafe_allow_html=True)    
    with col2:               # To display brand log
        st.image(logo, width=130 )
    
    st.write("Please visit My Data Talk's Medium blog at: https://medium.com/@insightsbees")    
    st.image(profile, width=700 )

    

elif choose == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Please Enter Email') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')

elif choose == "Translasi":
    base_url = "https://bade.kopas.id/translator?versi=2&mode={}&bahasa={}&text={}"

    Languages = {'Lampung':'lampung_a','Indonesia':'indonesia'}

    st.header("TRANSLASI BAHASA LAMPUNG DIALEK A")  

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
                

                
#side bar end


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

