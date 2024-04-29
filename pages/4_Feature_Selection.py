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
             background: url("https://static.thenounproject.com/png/1214184-200.png");
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

st.header(':blue[Feature Selection and Feature Engineering]', divider='red')
st.text('')
st.write('''In this project, the feature engineering procedures that follow were implemented: 
1. Only the two category variables (borough and property use type) and the numerical variables ought to be selected.
2. Include the log transformation of the numerical variables. 
3. Give the category variables a code.
''')
st.text('')
st.image('Images/Picture4.png')

#st.subheader('Handling missing values', divider='red')
st.write('''One column represents the score, and there were 109 unique features in the observations (buildings). Because of their high correlation, several of these features are repeated, and not all of them are probably important for score prediction. We thus eliminated such observations.''')
st.image('Images/Picture5.png')
st.write('''Our final dataset has 64 features (one of the columns is the target). Because the categorical variables are only one-hot encoded, this is still a considerable quantity. Furthermore, models like random forests perform implicit feature selection, which is the automatic selection of characteristics that are relevant during training, while models like linear regression may have problems with a large number of features. We will keep all of the features for the time being and keep an eye on the model's performance, even if there are still phases in the feature selection process.''')
