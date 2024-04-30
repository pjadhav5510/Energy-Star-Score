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

st.header(':blue[Future Impact and Feasibility]', divider='red')
st.text('')
st.write('''Positive implications for the future of energy-efficient construction can be derived from the analysis and performance of our model. By using precise estimation techniques, stakeholders may allocate resources wisely and prioritize improvements to improve energy performance in a range of building types. Regulators, architects, and building managers can develop regulations and interventions that explicitly target industries with lower Energy Star ratings, such as hotels and senior care facilities, with the aid of our study. As a result, energy efficiency will be distributed more fairly throughout the built environment.
''')

st.write('''Furthermore, the negative connections between Energy Star Scores and metrics like Site Energy Use Intensity, Electricity Intensity, and Natural Gas Usage demonstrate the importance of targeted actions to reduce energy consumption and diminish environmental effect. These insights can help target energy efficiency programs and incentives that aim to reduce resource-intensive building practices, which will reduce energy costs and emissions and promote sustainability.''')


