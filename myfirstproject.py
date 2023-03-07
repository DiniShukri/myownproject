import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('Advertising.csv')

st.header("My first Project")



st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
if show:
    st.write(pd.df())
    )
