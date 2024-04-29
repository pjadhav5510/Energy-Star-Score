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
             background: url("https://media.istockphoto.com/id/959713416/photo/night-wide-shot-of-monterrey-city-in-nuevo-leon-mexico.jpg?s=612x612&w=0&k=20&c=9Pg_Vht4xhulSpzCimsFKFqzgZLov8fwv4866Sacnwo=");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()


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

st.image('Homepage/Images/parisplot.png',use_column_width ='always')
st.text('')
st.write('')
    
