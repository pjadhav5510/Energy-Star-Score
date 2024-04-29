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
             background: url("https://static.thenounproject.com/png/5004205-200.png");
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

st.header(':blue[Data Cleaning]', divider='red')
st.text('')
st.write('''Upon examining the unprocessed data, we observed many issues. Our task was clear: predict the score column, even though there were sixty columns, many of which we were unaware of. Even for an expert in building energy research like me, there were certain column meanings that remained ambiguous while others were obvious. However, because machine learning models determine the significance of features on their own, this ambiguity isnt always an issue. But understanding the problem makes interpretation easier, so it seemed sensible to read the columns.

We made the independent decision to look into it. A set of data revealed potential evidence for "Local Law 84". According to an internet search, buildings greater than 50,000 square feet are required by law to submit energy figures once a year. Further research turned up a PDF detailing every column. 

While it was not necessary to analyze every column, it was important to know what our prediction target was. A building's score, which in Portfolio Manager was defined as a percentile value ranging from 1 to 100, where 100 signified the best energy efficiency, indicated how energy-efficient it was in comparison to other buildings. This grade ensured uniform distribution throughout all buildings. ''')
st.text('')

st.subheader('Convert Data to appropriate format', divider='red')
st.text('')
st.write('''We may convert the "Not Available" items in the numerical columns to numeric data types by replacing them with np.nan, which can be thought of as floats. From the columns that include numerical values (such square footage or energy use), we will next generate numeric datatypes.''')
st.image('Images/picture1.png')

st.subheader('Handling missing values', divider='red')
st.write('''After acquiring the precise column datatypes, we carry out the analysis by looking at each column's percentage of missing values. 
This function calculates the percentage of missing data and the number of missing values for each column. ''')
st.image('Images/picture3.png')
st.write('We also delt with missing data in columns, we removed 11 columns which had missing data in it.')
