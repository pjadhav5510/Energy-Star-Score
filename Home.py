import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Energy Star Score',
    layout='wide'
)

st.image('https://i.gifer.com/Uqhe.gif',use_column_width='always')





st.header(':blue[Prediction of energy star scores of new buildings]',divider='red')
st.text('')
st.subheader('Introduction',divider='red')

st.write('The ENERGY STAR score provides a comprehensive snapshot of your building’s energy performance, taking into account the building’s physical assets, operations, and occupant behavior. It is expressed on an easy-to-understand 1 to 100 scale, where the higher the score, the better the energy performance of the building. It’ll help you identify which buildings in your portfolio to target for improvement or recognition.')

st.subheader('How the 1–100 ENERGY STAR Score is Calculated',divider='red')

st.write('Using the 1–100 ENERGY STAR score, you can understand how your building’s energy consumption measures up against similar buildings nationwide. The ENERGY STAR score allows everyone in your organization, from the maintenance tech to the CEO, to quickly understand how your building is performing. A score of 50 represents median energy performance, while a score of 75 or higher indicates your building is a top performer—and may be eligible for ENERGY STAR certification.')
st.text('')
st.write('It’s a simple but powerful tool. Based on actual, measured data, the ENERGY STAR score assesses how your building is performing as a whole, taking into account its physical attributes, its operations, and how the people inside use it. Are you open 24 hours? Do you have a high density of workers? The ENERGY STAR score is tailored to account for how your building works in the real world.')


