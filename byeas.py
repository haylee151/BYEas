import streamlit as st
import pandas as pd
from ctgan import CTGANSynthesizer
from ctgan import load_demo
import numpy as np
from sdv.tabular import CTGAN
import matplotlib.pyplot as plt
from collections.abc import Iterable
from table_evaluator import load_data, TableEvaluator
import pathlib
from PIL import Image
import time
import json

st.set_page_config(page_title=None, page_icon=None, layout='centered', initial_sidebar_state='auto')

splash = st.empty()
#Logo
col1, col2, col3 = st.beta_columns([1,6,1])

with col1:
    st.write("")

with col2:
    st.image("https://i.imgur.com/xS0j6sT.jpg", width=200)

with col3:
    st.write("")
#

#Uploading File
uploaded_file = st.sidebar.file_uploader("Choose a file", accept_multiple_files=False,type=['csv'])

#Highlight Columns
def highlight_cols(s):
    color = 'yellow'
    return 'background-color: %s' % color

##@st.cache(suppress_st_warning=True)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, nrows=400)
    st.write(""" ## 1. Your Uploaded Data """)
    st.dataframe(df)
    st.write(""" Dataset shape: """, df.shape)
    listcol = (df.columns)
    options = st.sidebar.selectbox("Select Column",listcol)

    if options:
        detailed = df[options].value_counts().index.tolist() 
        bias = st.sidebar.checkbox("Balance Column Calculator") 
        condition = st.sidebar.selectbox('Select Condition', detailed)
        if hasattr(condition, '__iter__'):
            st.write('')
        else:
            st.write()

    sample_size = st.sidebar.number_input('Select the Number of Samples', 1)
    ctgan_button = st.sidebar.button("Run to Generate Data")

if not uploaded_file: 
    splash.text("Please Load Data in sidebar...")
else:
    if options:
        st.write(""" ## 2. Data Visualizations """)
        f = (df[options].value_counts())
        st.bar_chart(f)
    try:
        if bias:
            st.write("""## Balance Column Calculator """)
            value_columns = df[options].value_counts()

            df2 = pd.DataFrame(data=value_columns)
            df2= max(value_columns)-df2

            data_list = df2[options].tolist()
            all_columns = df[options].value_counts().index
            
            condition_list = []
            for allcolumn in all_columns:
                conditions = {options: allcolumn}
                condition_list.append(conditions)

            list1 = data_list
            list2 = condition_list

            for a,conditions in zip(list1, list2):
                y = a,conditions
                st.write(a,"samples of:",str(conditions)[1:-1])

    except:
        st.error("Please Select Column")

#CTGAN
    if ctgan_button:
        st.write("""## 3. Synthetic Data """)
        with st.spinner("Processing Your Data..."):
            model = CTGAN()
            model.fit(df)

            conditions = {
            options: condition
            }
        
            new_ctgan_data = model.sample(sample_size, conditions=conditions)
            st.write("Generated Synthentic data:")
            st.write(new_ctgan_data.style.applymap(highlight_cols, subset=pd.IndexSlice[:, [options]]))
            st.write(""" Dataset shape: """, new_ctgan_data.shape)
            frames = [df, new_ctgan_data]
            result = pd.concat(frames)

            st.write(""" ## Combined Data:""")
            st.write("Your Original Data and Synthetic Data:")
            st.write(result)
            st.write(""" Dataset shape: """, result.shape)

            STREAMLIT_STATIC_PATH = pathlib.Path(st.__path__[0]) / 'static'
            DOWNLOADS_PATH = (STREAMLIT_STATIC_PATH / "downloads")
            if not DOWNLOADS_PATH.is_dir():
                DOWNLOADS_PATH.mkdir()
            st.markdown("Download from [downloads/myresults.csv](downloads/myresults.csv)")
            result.to_csv(str(DOWNLOADS_PATH / "myresults.csv"), index=False)    
            f = (result[options].value_counts())
            st.bar_chart(f)

        




        
      