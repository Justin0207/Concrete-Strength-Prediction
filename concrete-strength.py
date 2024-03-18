# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 06:51:53 2024

@author: HP
"""


import streamlit as st
import pickle
import base64
import pandas as pd


model = pickle.load(open(r'C:\Users\HP\Desktop\DS\Concrete strength\concrete_model_.pkl', 'rb'))

st.header('Concrete Strength Prediction App')


def set_background(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         .st-emotion-cache-sxs2aw{{
             background: None}}
         </style>
         """,
         unsafe_allow_html=True
     )

set_background(r'C:\Users\HP\Downloads\concrete(1).avif') 


cement = st.number_input('Cement (kg/m3)', value = None, min_value = 0.0, step = 0.1)

slag = st.number_input('Blast Furnace Slag (kg/m3)', value = None, min_value = 0.0, step = 0.1)

ash = st.number_input('Fly Ash (kg/m3)', value = None, min_value = 0.0, step = 0.1)

water = st.number_input('Water Volume (kg/m3)', value = None, min_value = 0.0, step = 0.1)

superplastic = st.number_input('Superplasticizer Content (kg/m3)', value = None, min_value = 0.0, step = 0.1)

coar_agg = st.number_input('Coarse Aggregate Content (kg/m3)', value = None, min_value = 0.0, step = 0.1)

fine_agg = st.number_input('Fine Aggregate Content (kg/m3)', value = None, min_value = 0.0, step = 0.1)

age = st.number_input('Age of Concrete', value = None, min_value = 0, step = 1)


if st.button('Predict Concrete Strength'):
    
    output = {
        'cement':[cement],
        'slag': [slag],
        'ash': [ash],
        'water': [water],
        'superplastic': [superplastic],
        'coarseagg': [coar_agg],
        'fineagg': [fine_agg],
        'age': [age]}
    temp_df = pd.DataFrame(output)
    try:
        value = model.predict(temp_df)
        st.success('Estimated Strength: %.2f MPa' %value[0])
    except ValueError:
        st.error('Missing or Null Inputs')
        st.stop()
        