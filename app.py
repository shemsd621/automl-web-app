import streamlit as st
import pandas as pd
# from pydantic_settings import BaseSettings


# import profiling capability
# import pandas_profiling
# renders profile report inside streamlit
# from streamlit_pandas_profiling import st_profile_report

with st.sidebar:
    st.image("https://i.pinimg.com/736x/89/05/f0/8905f050a1392a36cec87ec52cb829df.jpg")
    st.title("AutoStreamML")
    # for navigation
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info("This application allows you to build an automated pipeline using Streamlit, Pandas Profiling and Pycaret")

# if os.path.exists("irisdata.csv"):
    # df = pd.read_csv("irisdata.csv", index_col=None)

if choice == "Upload":
    st.title("Upload Your Data for Modelling")
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file, index_col=None)
        df.to_csv("irisdata.csv", index=None)
        st.dataframe(df)

if choice == "Profiling":
    st.title("Automated Exploratory Data Analysis")
    profile_report = df.profile_report()
    st_profile_report(profile_report)

if choice == "Modelling":
    pass

if choice == "Download":
    pass
