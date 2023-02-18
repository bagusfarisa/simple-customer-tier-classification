import streamlit as st
import pandas as pd
import membership as m


st.title('Simple Customer Tier Predictor')
st.subheader('Give a deal based on income & expense.')

income = st.number_input(label='Income',value=2000000,format='%a')
expense = st.number_input(label='Expense',value=1000000,format='%a')

tier = m.predict_tier(expense, income)
discount, requirement = m.show_offer(tier)
discount = discount * 100

if income >= expense:
    st.markdown(f'Predicted tier: **{tier}**')
    st.success(f'''
    **Deal for you:**

    Get a {discount}% discount {requirement}
    ''')
else:
    st.warning('''
    **Warning**
    
    Income must be greater than expense.''')