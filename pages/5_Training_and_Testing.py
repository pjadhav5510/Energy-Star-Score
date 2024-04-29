
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
             background: url("https://static-00.iconduck.com/assets.00/training-icon-2048x2046-pm3vlakf.png");
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

st.header(':blue[Training and Testing]', divider='red')
st.text('')
st.write('''Our features in machine learning must always be split into two sets: 
We gave our model a training set and the answers during training so that it could learn a mapping between the features and the target.
The testing set that we used to evaluate the learned mapping of the model. Since the model has never seen the answers on the testing set, it produced predictions based only on the features. Using the true responses for the test set, we compared the test predictions to the true test targets to see how well our model worked in practice.
''')

st.text('')
st.write('''For training and testing our model we implemented two standard ML approaches.
1. Regression: Estimate the Energy Star Score's numerical value 
• Metrics: Rˆ2, the percentage of response variance described by the model, and Mean Absolute Error, the average divergence between forecasts and true values 
2. Classification: Using Energy Star Score intervals of 20 points, divide the buildings into 5 groups. Ascertain the class of a structure. 
• Metrics: Confusion matrix, accuracy, and f1_score (the harmonic mean of precision and recall).
''')
st.image('Homepage/Images/Picture6.png')
st.image('Homepage/Images/Picture7.png')
st.write('In the training set, there were 6622 buildings with a score, 2839 buildings with a score in the testing set, and 1858 buildings with no score. ')
