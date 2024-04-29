
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
             background: url("https://static.thenounproject.com/png/3681378-200.png");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

# side_bg = 'Homepage/Images/density.png'
# sidebar_bg(side_bg)

#df = pd.read_csv('Downloads/Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')

st.header(':blue[Conclusion]', divider='red')
st.text('')
st.write('''The building type, floor area, natural gas usage, electricity intensity, and site energy use intensity are the ideal indicators to consider when computing the Energy Star rating, according to our created model for accurately estimating a building's Energy Star Score.
''')

st.text('')
st.write(''':red[Recap from our learnings:]
         
• If a trained model is provided with the required data, it may accurately determine the Energy Star Score of a new building. 
         
• Offices, dormitories, and non-refrigerated warehouses have higher energy star ratings than senior care institutions and hotels; multi-family housing has scores in the middle.


• The site energy use intensity, the electricity intensity, and the natural gas usage all have a negative link with the Energy Star Score.

• A random forest regression trained on the training data achieved an average absolute error of 9 points on a hold-out testing set, which was much better than the baseline measure.

''')
