import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read data from google sheet!")
# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

st.write(df)
st.button('update!')