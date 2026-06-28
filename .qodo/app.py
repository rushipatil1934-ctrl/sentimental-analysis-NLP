import streamlit as st
import pandas as pd 
import joblib 

model = joblib.load("sentiment_analyses.ipynb")
scaler = joblib.load("sentiment_analyses.ipynb")
expected_columns = joblib.load("sentiment_analyses.ipynb")

st.title("sentiment_analyses")
st.markdown("provide the following detailes")

sentiments = st.slider