import numpy as np
import joblib
import streamlit as st

# Loaded california data
obj = joblib.load('winequality.joblib')
model=obj['model']
col=obj['columns']


# california app
st.title('winequality app')
In=[]
for i in col:
    v = st.number_input(f"Enter {i} value:")
    In.append(v)
if st.button('click'):
    out=model.predict([In])
    st.success(f"The fixed acidity value is: {out}")
