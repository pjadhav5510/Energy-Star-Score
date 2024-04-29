import streamlit as st
import pandas as pd
import base64

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.unsplash.com/photo-1492086517200-9393d4eb53bf?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGNpdHklMjBuaWdodCUyMHNreXxlbnwwfHwwfHx8MA%3D%3D");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

# side_bg = 'Homepage/Images/density.png'
# sidebar_bg(side_bg)

df = pd.read_csv('Data/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')

st.header('Overview of Data', divider='red')
st.text('')
st.write('This data set includes information reported to the City by August 1, 2016 for calendar year 2015 energy and water consumption data and data from the 2016 Covered Buildings List. Metrics are calculated by the Environmental Protection Agency’s tool ENERGY STAR Portfolio Manager, and data is self-reporting by building owners. The public availability of data allows for local and national comparison of a buildings’ performance, incentivizes the most accurate benchmarking of energy usage, and informs energy management decisions.')
st.text('')
st.subheader('Dataset',divider='red')
st.text('')
st.dataframe(df)


