import streamlit as st
import time
st.write("Progress")
pro=st.progress(0)
for i in range (101):
  time.sleep(0.01)
  pro.progress(i)
st.balloons()
st.snow()


