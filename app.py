#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:38:18 2022

@author: aa
"""

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')
data = data.iloc[:,0:32]
data2 = data.iloc[:,1:]
st.title("Breat Cancer Data")

page = st.sidebar.selectbox(
    "Breat Cancer Dataset",
    ("Dataset", "Diagnosis", "Features")
)

if page == "Dataset":
    st.write("Although breast cancer is the most common gynecological cancer, most breast lumps are not cancer. In fact, more than 80 percent of breast lumps end up being benign. However, can we identify breast cancer from a breast lump?")
    st.write("We developed an analysis and prediction algorithm to predict Breast Cancer. You can view our work through: ")
    st.write("This is a Dashboard to offer a general view to our data.")
    st.write("Here is our dataset of breat cancer.")
    if st.button('Show Data'):
        st.dataframe(data)
elif page == "Diagnosis":
    with st.container():
        st.write("Counts of Diagnosis in the dataset:")
        fig = plt.figure(figsize=(10, 4))
        sns.countplot(x = "diagnosis", data = data)
        st.pyplot(fig)
elif page == "Features":
    option = st.selectbox(
        'Select feature to view:',
        ('radius_mean',  'texture_mean','perimeter_mean','area_mean','smoothness_mean','compactness_mean',
        'concavity_mean','concave points_mean','symmetry_mean','fractal_dimension_mean','radius_se',
        'texture_se','perimeter_se','area_se','smoothness_se','compactness_se','concavity_se',
        'concave points_se','symmetry_se','fractal_dimension_se','radius_worst','texture_worst',
        'perimeter_worst','area_worst','smoothness_worst','compactness_worst','concavity_worst',
        'concave points_worst','symmetry_worst','fractal_dimension_worst'))
    fig2 = plt.figure(figsize=(10, 4))
    sns.boxplot(y=option , x='diagnosis',hue = "diagnosis", data = data)
    st.pyplot(fig2)


