import streamlit as st
import pandas as pd

st.title("Sales & Revenue Dashboard")

st.write("My first sales dashboard")

df = pd.read_csv("sales_data.csv")

st.dataframe(df)
