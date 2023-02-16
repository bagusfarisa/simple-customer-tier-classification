import streamlit as st
import pandas as pd
import membership as m
import matplotlib.pyplot as plt
import numpy as np
import math


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

X = pd.DataFrame({
    'first column': [1, 2, 0, 4],
    'second column': [10, 20, 20, 100]
    })


def k_distances(X, n=None, dist_func=None):
    """Function to return array of k_distances.

    X - DataFrame matrix with observations
    n - number of neighbors that are included in returned distances (default number of attributes + 1)
    dist_func - function to count distance between observations in X (default euclidean function)
    """
    if type(X) is pd.DataFrame:
        X = X.values
    k=0
    if n == None:
        k=X.shape[1]+2
    else:
        k=n+1

    if dist_func == None:
        # euclidean distance square root of sum of squares of differences between attributes
        dist_func = lambda x, y: math.sqrt(
            np.sum(
                np.power(x-y, np.repeat(2,x.size))
            )
        )

    Distances = pd.DataFrame({
        "i": [i//10 for i in range(0, len(X)*len(X))],
        "j": [i%10 for i in range(0, len(X)*len(X))],
        "d": [dist_func(x,y) for x in X for y in X]
    })
    return np.sort([g[1].iloc[k].d for g in iter(Distances.groupby(by="i"))])

fig = plt.figure()
d = k_distances(X)
plt.plot(d)
plt.ylabel("k-distances")
plt.grid(True)
plt.show()


st.pyplot(fig)