import streamlit as st
import pickle
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

