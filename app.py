import streamlit as st # python -m streamlit run app.py
import pickle
import numpy as np
import base64
##bg 

# -------------------- VIDEO BACKGROUND -------------------- #
def set_bg_video():
    video_file = open("138962-770800093.mp4", "rb")
    video_bytes = video_file.read()
    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background: transparent;
        }}

        #bg-video {{
            position: fixed;
            top: 0;
            left: 0;
            min-width: 100vw;
            min-height: 100vh;
            object-fit: cover;
            z-index: -1;
        }}

        .overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.3);
            z-index: -1;
        }}
        "<h1 style='color:black; text-align:center;'>☀ SOLAR POWER PREDICTION MODEL</h1>",

        /* Transparent container */
        .block-container {{
            background: rgba(245, 245, 245, 1);
            padding: 2rem;
            border-radius: 20px;
            color: white;
        }}

        /* Sidebar styling */
        section[data-testid="stSidebar"] {{
            background: rgba(245, 245, 245, 1);
        }}

        /* Button styling */
        div.stButton > button {{
            background: linear-gradient(45deg, #FFA000, #FF6F00);
            color: white;
            font-weight: bold;
            border-radius: 12px;
            padding: 0.6rem 1.5rem;
            border: none;
            transition: 0.3s;
        }}

        div.stButton > button:hover {{
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(0,0,0,0.4);
        }}

        /* Result box */
        .result-box {{
            background: rgba(255, 193, 7, 0.9);
            padding: 15px;
            border-radius: 15px;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            color: black;
        }}
        </style>

        <div class="overlay"></div>

        <video autoplay muted loop id="bg-video">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

set_bg_video()

##
st.title('SOLAR POWER PREDICTION MODEL')

AMBIENT_TEMPERATURE=st.sidebar.slider('Ambient Temperature: ',min_value=0.0,max_value=100.0,value=5.0,step=0.1)
MODULE_TEMPERATURE=st.sidebar.slider('Module Temperature:',min_value=0.0,max_value=100.0,value=5.0,step=0.1)
IRRADIATION=st.sidebar.slider('IR Radiation: ',min_value=0.0,max_value=10.0,value=5.0,step=0.1)
hour=st.sidebar.slider('Hour: ',min_value=0,max_value=24,value=5)
day=st.sidebar.slider('Day: ',min_value=0,max_value=31,value=5)
month=st.sidebar.slider('Month: ',min_value=0,max_value=12,value=5)

new_data=[[AMBIENT_TEMPERATURE,MODULE_TEMPERATURE,IRRADIATION,hour,day,month]]

with open('model.pkl','rb') as file:
    model = pickle.load(file)
if st.sidebar.button('Predict'):
    pred =model.predict(new_data)[0]
    if pred==0:
        st.subheader('Power Level: Low')
    elif pred==1:
        st.subheader('Power Level: Medium')




