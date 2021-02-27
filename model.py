import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import  pickle
import math
import warnings
warnings.filterwarnings('ignore')


@st.cache(allow_output_mutation=True)
def load_pickle():
    return pickle.load(open("EDA.pickle",'rb'))
def load_data():
    return pd.read_csv("adult.csv")


EDA_Pickle=pickle.load(open("EDA.pickle",'rb'))

# Data
df = pd.read_csv("adult.csv")
cat_cols=df.select_dtypes(exclude=np.number).columns
num_cols=df.select_dtypes(include=np.number).columns

# Sidebar
st.sidebar.header("**Walkthrough**")
data=st.sidebar.button("Data")
eda=st.sidebar.button("EDA")
viz=st.sidebar.button("Visualization")


# Main Area

if not (data or eda):
    st.header("Overview")
    st.image("/Users/i327885/Desktop/DS_ML/Assignments/ML2/Presentation/Solutions/UI/main.gif")

if data:
    st.header("Dataset")
    st.write("""
    **Rows:** """ + str(df.shape[0])+""" **Attributes:** """+str(df.shape[1]))
    st.dataframe(df)

if eda:
    st.write("Visualizations")
    for viz in EDA_Pickle.keys():
        st.header("")
        st.write(EDA_Pickle[viz])