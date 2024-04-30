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
st.image('Images/Picture1.png')

st.subheader('Handling missing values', divider='red')
st.write('''After acquiring the precise column datatypes, we carry out the analysis by looking at each column's percentage of missing values. 
This function calculates the percentage of missing data and the number of missing values for each column. ''')
st.image('Images/Picture3.png')
st.write('We also delt with missing data in columns, we removed 11 columns which had missing data in it.')

st.subheader('Handling outliers', divider='red')
st.write('''To evaluate this subjective statistic, we looked to Energy Use Intensity (EUI), which is calculated by dividing the overall energy use by the structure's square footage. As EUI is not self-reported, it offers a more objective measurement of energy efficiency. Unlike the percentile-based Energy Star Score, the absolute values of the EUI should essentially follow a normal distribution, possibly with outliers at extreme ends. ''')
st.text('')
st.image('Images/EUI_with_outliers.png')
st.text('')
st.write('''We analysed the site EUI unit and noticed we have another problem which is outliers.
We removed outliers by using the interquartile range method:''')

code = '''
    # Calculate first and third quartile 
    first_quartile = data['Site EUI (kBtu/ft2)'].describe()['25%'] 
    third_quartile = data['Site EUI (kBtu/ft?)'].describe()['75%']

    # Interquartile range 
    iqr = third_quartile - first_quartile

    # Remove outliers 
    data = data[(data['Site EUI (kBtu/ft2)'] > (first_quartile - 3 * iqr)) & (data['Site EUI (kBtu/ft2)'] < (third_quartile + 3 * iqr))]
'''

st.code(code, language='python')

st.write('''The below picture in data visualization, which has a long tail on the right after the outliers are eliminated, is almost normally distributed and seems less suspicious (it has a positive skew). Our goal is to estimate the Energy Star Score even though this metric might be more objective. Even if the score was not a good predictor, we nonetheless made an effort to do so.''')



st.header(':blue[Data Visualizations]', divider='red')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with st.container():
    with col1:
        #st.text('')
        st.image('Images/scores.png')
        st.text('')
        st.write('Our first plot has already revealed some surprising (and suspicious) information! As the Energy Star Score is a percentile rank, we would expect to see a completely flat distribution with each score making up 1% of the distribution (about 90 buildings).')

    with col2:
        st.image('Images/EUI.png')
        st.text('')
        st.write('This plot looks a little less suspicious and is close to normally distributed with a long tail on the right side (it has a positive skew).')

with st.container():
    
    with col3:
        st.text('')

        st.image('Images/density.png')
        st.text('')
        st.write('From this graph, we can see that the building type does have an effect on the score (the negative scores on the graph are an artifact of the kernel density estimation procedure).')


    with col4:
        st.text('')
        st.image('Images/density_borough.png')
        st.text('')
        st.write('The borough of the building does not seem to make as significant a difference in the distribution of the score as does the building type.')

st.image('Images/parisplot.png',use_column_width ='always')
st.text('')
st.write('')
