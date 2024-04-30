
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

st.subheader('Baseline Naive Model', divider='red')

st.write('''Additionally, we construct a baseline model that is naive in order for our models to be chosen as the best ones. Establishing a naive baseline is essential when building machine learning models. If the models we create can't beat a naive estimate, we might have to admit that machine learning isn't the ideal answer for this problem. This could be the consequence of using the wrong models, requiring more data, or having a simpler solution that doesn't require machine learning. In order to prevent building a machine learning model and then discovering it is unable to handle the problem, it is imperative to establish a baseline.''')

st.write('''A decent naive baseline for a regression problem is to predict the target's training set median value for every case in the test set. This lowers the threshold for our models and is simple to implement.
To compute the MEA as evaluation metrics for the naïve baseline model, we developed the following function:''')

code = '''
    def mae(y_true, y_pred):
    return np.mean(abs(y_true - y_pred))
'''

st.code(code, language='python')

st.write('''This showed that the average estimate we made for our test set is about 25 points off. The average error resulting from a naive technique is roughly 25% because the scores vary from 1 to 100. With our models, we had a low baseline to beat.''')

st.subheader('Splitting into training and testing', divider='red')

st.write('''Our features in machine learning must always be split into two sets: 
We gave our model a training set and the answers during training so that it could learn a mapping between the features and the target.
The testing set that we used to evaluate the learned mapping of the model. Since the model has never seen the answers on the testing set, it produced predictions based only on the features. Using the true responses for the test set, we compared the test predictions to the true test targets to see how well our model worked in practice.
''')

st.text('')
st.write('''For training and testing our model we implemented two standard ML approaches.
         
• Regression: Estimate the Energy Star Score's numerical value 

• Metrics: Rˆ2, the percentage of response variance described by the model, and Mean Absolute Error, the average divergence between forecasts and true values 
''')
st.image('Images/Picture6.png')
st.image('Images/Picture7.png')
st.write('In the training set, there were 6622 buildings with a score, 2839 buildings with a score in the testing set, and 1858 buildings with no score. ')
