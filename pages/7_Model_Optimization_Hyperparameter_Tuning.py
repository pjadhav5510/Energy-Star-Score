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
             background: url("https://static.thenounproject.com/png/5930037-200.png");
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

st.header(':blue[Model Optimization]', divider='red')
st.text('')
st.write('''Model optimization is the process of adjusting a machine learning model to improve its performance on a certain task. This means adjusting several model parameters, including as hyperparameters, algorithms, and feature engineering techniques, to achieve the optimum results. Enhancing the model's effectiveness, generalizability, and precision aims to enable it to make more accurate forecasts and handle issues more successfully. Feature selection, regularization, cross-validation, hyperparameter tinkering, and ensemble approaches are a few examples of model optimization strategies. Creating a model that operates optimally on unknown data and produces reliable, accurate predictions is the ultimate goal of model optimization.
''')

st.header(':blue[Hyperparamter Tuning]', divider='red')
st.text('')
st.write('''For each model, we employed random search and cross-validation to identify the ideal hyperparameters. 

The method of choosing which hyperparameters to examine is called "random search." We listed a variety of options first, and then we chose combinations at random to test. Conversely, grid search took into account every combination we typed. In general, random search is better when we are unsure of the ideal model hyperparameters because it can help us narrow down the amount of alternatives and then utilize grid search with a more limited set of options.
         
For the gradient boosting regressor, we tuned in six different hyperparameters. These all impacted the model in various ways that are difficult to predict in advance, and the only way to figure out which combination works best for a given issue is by trying them all out.
''')

st.text('')
st.image('Homepage/Images/Screenshot 2024-04-28 204621.png')
st.text('')

st.write('''We used the outcomes of the random search to inform a grid search by creating a grid with hyperparameters close to those that performed best during the random search. However, we focus on a single choice rather than evaluating all of these alternatives again: the total number of trees in the forest (n_estimators). The impact of altering a solitary hyperparameter on performance is immediately apparent. We expected that the number of trees would significantly affect the underfitting to overfitting ratio.

Grid search was used in this instance, with a grid containing only the hyperparameter [n_estimators]. ''')

st.image('Homepage/Images/Picture9.png')

st.subheader('Checking for training and testing error', divider='red')
st.text('')
st.image('Homepage/Images/Picture10.png')

st.text('')
st.write('''The findings clearly show that our model was overfitting! The training error is significantly smaller than the testing error, indicating that although the model learned the training data quite well, it was not able to generalize to the test data as well. Thus, as the number of trees increases, so does the degree of overfitting. Both the test and training errors decrease with the number of trees, but the training error drops faster.''')

st.write('''We tried to reduce overfitting by getting more training data or by simplifying the model through regularization or hyperparameter tuning, however training error and testing error constantly varied from one another (training error is always smaller). The gradient boosting regressor can be set to reduce the number of trees, increase the minimum amount of samples at a leaf node, and decrease the maximum depth of each tree. Keeping in mind that the model may be overfitting to the training set, we used the one that performs the best for the time being.''')

st.subheader('Final Model', divider='red')



code = '''Out the of models, we selected tree-based gradient boosting model to tune its hyperparameter. 

We observed the following optimized results:

GDR Model performance on the test set: MAE = 11.0164

Tunned GDR model performance on the test set:   MAE = 9.0446.
'''

st.code(code, language='python')

st.write('''Although it takes a lot longer to run (approximately 12 times slower on my machine), the final model does perform around 10% better than the baseline model. In machine learning, trade-offs are frequently involved, such as bias vs variance, accuracy vs interpretability, and accuracy vs running time. The context ultimately determines which model is best to use. Because the training time's absolute magnitude is not substantial, despite the large relative difference, the increase in run time is not a hindrance in this case. The balance might not be the same in a different scenario, therefore we would need to take into account our goals and the constraints we are operating under.
         
To get a sense of the predictions, we can plot the distribution of true values on the test set and the predicted values on the test set.''')

st.image('Homepage/Images/Download.png')

st.text('')

st.write('''Despite the projected values' density being closer to the test values' median than to the actual peak at 100, the distribution appears to be almost identical. It seems that the model predicts values that are closer to the median and may be less reliable at forecasting the extreme values.

A residuals histogram is another diagnostic plot. The residuals should ideally be regularly distributed, which would indicate that the model is incorrect in both high and low values by the same amount.''')

st.image('Homepage/Images/download (1).png')
st.text('')
st.write('The residuals are close to normally disributed, with a few noticeable outliers on the low end. These indicate errors where the model estimate was far below that of the true value.')


