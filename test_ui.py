import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pickle
import math
import warnings
warnings.filterwarnings('ignore')

# Data
df = pd.read_csv("adult.csv")
education_dict = dict(
    zip(df['education'].unique(), df['education.num'].apply(str).unique()))


# Sidebar
st.sidebar.header("**User Input Parameters**")
age = st.sidebar.slider("Age", df['age'].min(
), df['age'].max(), math.floor(df['age'].mean()))
workclass = st.sidebar.selectbox(
    "Workclass", list(df['workclass'].unique()[1:]))
fnlwgt = st.sidebar.slider("Final Weight", df['fnlwgt'].min(
), df['fnlwgt'].max(), math.floor(df['fnlwgt'].mean()))
education = st.sidebar.selectbox("Edication", list(
    df.sort_values(by='education.num')['education'].unique()))
education_num = education_dict[education]
maritalstatus = st.sidebar.selectbox("Marital Status", list(
    df.sort_values(by='marital.status')['marital.status'].unique()))
occupation = st.sidebar.selectbox("Occupation", list(
    df.sort_values(by='occupation')['occupation'].unique()[1:]))
relationship = st.sidebar.selectbox("Relationship", list(
    df.sort_values(by='relationship')['relationship'].unique()[1:]))
race = st.sidebar.selectbox("Race", list(
    df.sort_values(by='race')['race'].unique()))
sex = st.sidebar.selectbox("Sex", list(
    df.sort_values(by='sex')['sex'].unique()))
gain = st.sidebar.slider("Capital Gain", df['capital.gain'].min(
), df['capital.gain'].max(), math.floor(df['capital.gain'].mean()))
loss = st.sidebar.slider("Capital Loss", df['capital.loss'].min(
), df['capital.loss'].max(), math.floor(df['capital.loss'].mean()))
hoursperweek = st.sidebar.slider("Hours Per Week", df['hours.per.week'].min(
), df['hours.per.week'].max(), math.floor(df['hours.per.week'].mean()))
nativecountry = st.sidebar.selectbox("Native Country", list(
    df['native.country'].sort_values().unique()[1:]), 38)
# income=st.sidebar.selectbox("Income",list(df['income'].unique()))
# Main Area
# DataTab
data_expander = st.beta_expander("Dataset")

data_expander.header("Dataset")
data_expander.write("""
 **Rows:** """ + str(df.shape[0])+""" **Attributes:** """+str(df.shape[1]))

data_expander.dataframe(df)

df.shape

# st.dataframe(df.groupby('native.country').count()['age'])

# fig=px.bar(data_frame=df, x="native.country", y="workclass",  barmode="group")
# st.plotly_chart(fig)
# st.write(df['native.country'].value_counts().plot.pie(autopct="%1.1f%%"))
# st.pyplot()

fig, ax = plt.subplots(2, 3, figsize=(10, 8))
for i, v in enumerate(df.select_dtypes(include=np.number)):
    sns.kdeplot(data=df[v], ax=ax.flatten()[i])
plt.tight_layout()
st.pyplot(plt)

# User Input Tab
user_input_expander = st.beta_expander("User Input")
selected_data = pd.DataFrame({
    'age': [age],
    'workclass': [workclass],
    'fnlwgt': [fnlwgt],
    'education': [education],
    'education.num': education_num,
    'marital.status': [maritalstatus],
    'occupation': [occupation],
    'relationship': [relationship],
    'race': [race],
    'sex': [sex],
    'capital.gain': [gain],
    'capital.loss': [loss],
    'hours.per.week': [hoursperweek],
    'native.country': [nativecountry]
})
user_input_expander.header('Data')
user_input_expander.dataframe(selected_data)
