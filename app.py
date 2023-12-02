import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
# Set the main heading using st.title()
st.title("AlgoVistaHub - Data Science and Machine Learning")

# Introductory text
st.write("Welcome to the AlgoVistaHub Data Science and Machine Learning Hub. Explore the wonders of data-driven insights!")

df = pd.read_csv('census.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

#sidebar title
st.sidebar.title("India's Data Viz")

#sidebar box
selected_state = st.sidebar.selectbox('Select a State', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))

secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.markdown('###### Bubble Size Represents Primary Parameter')
    st.markdown('###### Color Represents Secondary Parameter')
    if selected_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat="Latitude", size=primary, color=secondary, size_max=35, lon="Longitude", zoom=3,
                                mapbox_style="carto-positron", width= 700,height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
    else:
        state_df= df[df['State']== selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", size=primary, color=secondary, size_max=35, lon="Longitude", zoom=3,
                                mapbox_style="carto-positron", width=700, height=700,hover_name='District')
        st.plotly_chart(fig, use_container_width=True)
