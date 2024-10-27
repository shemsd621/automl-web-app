import streamlit as st
import pandas as pd

with st.sidebar:
    st.image("https://i.pinimg.com/736x/89/05/f0/8905f050a1392a36cec87ec52cb829df.jpg")
    st.title("AutoStreamML")
    # for navigation
    choice = st.radio("Navigation", ["Upload", "Profiling", "ML", "Download"])
    st.info("This application allows you to build an automated pipeline using Streamlit, Pandas Profiling and Pycaret")

if choice == "Upload":
    st.title("Upload Your Data for Modelling")
    file = st.file_uploader("Upload Your Dataset Here")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)

if choice == "Profiling":
    pass

if choice == "ML":
    pass

if choice == "Download":
    pass
