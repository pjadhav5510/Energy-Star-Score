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
             background: url("https://static.thenounproject.com/png/5537187-200.png");
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
st.header(':blue[Feature Importance]', divider='red')

st.write('''We interpreted an ensemble of decision trees basically using what are known as feature importances. These could be considered the variables that most reliably predict the objective. Even though the real details of the feature importance are highly complex, we used the relative values to compare the features and determine which are more relevant to our circumstance. 

It is very easy to extract the feature importances from a trained ensemble of trees using scikit-learn. We kept the feature importances in a dataframe so that we could review and show them.
         
We extracted the top 10 features. ''')

code = '''Index       Feature	                                            Importance
0	    Site EUI (kBtu/ft²)	                                    0.403532
1	    Weather Normalized Site Electricity Intensity 	    0.263059
2	    Water Intensity (All Water Sources) (gal/ft²)	    0.071286
3	    Property Id	                                            0.035165
4	    Largest Property Use Type_Non-Refrigerated War	    0.031924
5	    DOF Gross Floor Area	                            0.027900
6	    log_Water Intensity (All Water Sources) (gal/ft²)	    0.026058
7	    Order	                                            0.024592
8	    log_Direct GHG Emissions (Metric Tons CO2e)	            0.023655
9	    Year Built	                                            0.022100'''

st.code(code, language='python')

st.write('''The two most significant characteristics are, by a significant margin, the Weather Normalized Site Electricity Intensity, or kWh/ft², and the Site Energy Use Intensity, or EUI (kBtu/ft²). The relative relevance then sharply declines, suggesting that we do not need to keep every attribute in order to produce a model that performs almost as well.

For a visual comparison, let's graph the feature importances.''')

st.image('Images/download (2).png')
