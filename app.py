import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x:x.split()[0])

# create a text header above the dataframe
st.header('Data viewer') 
# display the dataframe with streamlit
st.dataframe(df)

st.header('Vehicle types by manufacturer')
# create a plotly histogram figure
fig = px.histogram(df, x='manufacturer', color='type')
# display the figure with streamlit
st.write(fig)

st.header('Histogram of `condition` vs `model_year`')
fig = px.histogram(df, x='model_year', color='condition')
st.write(fig)

st.header('Compare price distribution between manufacturers')
# get a list of car manufacturers
manufac_list = sorted(df['manufacturer'].unique())
# get user's input from dropdown menu
manufacturer_1 = st.selectbox(
                              label='select manufacturer 1', #title of select box
                              options=manufac_list, #options listed in the select box
                              index=manufac_list.index('chevrolet') #default preselected option
)
manufacturer_2 = st.selectbox(
                              label='select manufacturer 2', 
                              options=manufac_list, #options listed in the select box
                              index=manufac_list.index('hyundai') #default preselected option
)
                              
# filter the dataframe
mask_filter = (df['manufacturer'] == manufacturer_1) | (df['manufacturer'] == manufacturer_2)
df_filtered = df[mask_filter]

# add a checkbox if a user wants to normalize the histogram
normalize = st.checkbox('Normalize histogram', value=True)
if normalize:
    histnorm ='percent'
else:
    histnorm = None
    
# create a plotly histogram figure
fig = px.histogram(df_filtered, 
                      x='price',
                      nbins=30,
                      color='manufacturer',
                      histnorm=histnorm,
                      barmode='overlay')
   
# display the figure with stream lit
st.write(fig)
