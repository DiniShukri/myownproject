# import streamlit as st
# import numpy as np
# import pandas as pd

# df = pd.read_csv('Advertising.csv')

# st.header("My first Project")

# st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
# show = st.checkbox('I agree the terms and conditions')
# if show:
#     st.write(df)
    
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris flower** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    adsTV = st.sidebar.slider('TV', 0, 100, 50)
    adsRadio = st.sidebar.slider('Radio', 2.0, 4.4, 3.4)
    adsNews = st.sidebar.slider('Newspaper', 1.0, 6.9, 1.3)
    data = {'TV': adsTV,
            'Radio': adsRadio,
            'Newspaper': adsNew}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

df_train = pd.read_csv('Advertising.csv')
X = df_train[['TV','Radio','Newspaper']]
Y = df_train['Sales']

clf = LinearRegression()
clf.fit(X, Y)

prediction = clf.predict(df)

st.subheader('Prediction')
st.write(prediction)
