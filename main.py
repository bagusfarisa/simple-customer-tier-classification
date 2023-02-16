import streamlit as st
import pandas as pd
import membership as m


st.title("Simple Customer Tier Predictor")
st.subheader("Giving offer based on the data inputted.")


expense = st.number_input(label="Expense",value=1000000,format='%a')
income = st.number_input(label="Income",value=2000000,format='%a')

tier = m.predict_tier(expense, income)
st.write(tier)

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))