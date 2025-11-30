import streamlit as st
import pandas as pd 
from core import C_data_sorted
import seaborn as sns 

st.header("Board Game Geek New Ranking")
st.text("This is your new personalized ranking")
st.write(C_data_sorted)


fixed_column = "Bayes Rating"   

st.title("Correlation")
st.text("Check che correlation with any parameter")
st.write(f"Fixed Column: **{fixed_column}**")

#User choice
columns = list(C_data_sorted.columns)
columns.remove(fixed_column) 
columns.remove("ID")
columns.remove("Name")
selected_column = st.selectbox(
    "Select your column:",
    columns
)

#correlation calc
if selected_column:
    correlation = C_data_sorted[[fixed_column, selected_column]].corr().iloc[0,1]
    st.metric(
        label=f"Correlation between {fixed_column} e {selected_column}",
        value=f"{correlation:.3f}"
    )
st.text("correlation value meaning:\n-1 perfect negative correlation\n-1 perfect positive correlation\n-0 no correlation")