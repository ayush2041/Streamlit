import streamlit as st
import pandas as pd 

st.title("Product details dashboard")

file = st.file_uploader("Upload your csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)


if file:
    st.header("Summary stats")
    st.write(df.describe())