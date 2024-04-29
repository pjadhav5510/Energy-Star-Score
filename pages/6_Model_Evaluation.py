
import streamlit as st

st.set_page_config(
    page_title='Energy Star Score',
    layout='wide'
)

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
             background: url("https://cdn-icons-png.flaticon.com/512/9926/9926288.png");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

st.header(':blue[Model Evaluation]', divider = 'red')

st.text('')

st.write('''For our supervised regression model, we developed, test, and refined several machine-learning techniques. The goal was to identify the model with the most potential for future improvement (e.g., hyperparameter tuning). 
We are used the mean absolute error to compare the models.
''')
st.write('We will compare five different machine learning models using the great Scikit-Learn library')
st.write('1. Linear Regression')
st.write('2. Support Vector Machine Regression')
st.write('3. Random Forest Regression')
st.write('4. Gradient Boosting Regression')
st.write('5. K-Nearest Neighbors Regression')
st.text('')

st.image('Images/Picture8.png')


st.subheader('Results', divider='red')
st.write('''
Linear Regression: MAE = 12.2343
         
Support Vector Machine: MAE = 9.4543
         
Random Forest Regression: MAE = 8.0858
         
Gradient Boosted Regression: MAE = 11.0164
         
K-Nearest Neighbors Regression: MAE = 14.0863
''')

st.subheader('MAE score comparison', divider = 'red')

st.image('Images/mae.png')


st.subheader('R2 score comparison', divider = 'red')

st.image('Images/r2.png')

st.write('''The random forest performed better than the gradient-boosting regressor in terms of MAE score, although both are almost similar when it comes to R2 score, Given that we primarily used the default hyperparameters, We must acknowledge that this is not the most equitable comparison. The performance is greatly impacted by the hyperparameters, particularly when using the Support Vector Regressor. Because performance is less dependent on model settings, the random forest and gradient boosting methods are excellent for beginners. Still, given that every model performs noticeably better than the baseline, we can draw the conclusion that machine learning is useful from these results.''')
