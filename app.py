import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def get_UN_data():
  AWS_BUCKET_URL = "https://streamlit-demo-data.s3-us-west-2.amazonaws.com"
  df = pd.read_csv(AWS_BUCKET_URL + "agri.csv.gz")
  return df.set_index("Region")

df = get_UN_data()

countries = st.multiselect("Chose countries", list(df.index),["China"])
data = df.loc[countries]
data /= 1000000.0
st.write("### Gross Agricultural Production ($B), data.sort_index())
         
