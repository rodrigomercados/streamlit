import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Sales Dashboard",page_icon=":bar_chart:", layout="wide")

df=pd.read_excel(
	io='Libro1.xlsx',
	engine='openpyxl',
	sheet_name='Hoja1',
	skiprows=0,
	usecols='A:C',
	nrows=3)
