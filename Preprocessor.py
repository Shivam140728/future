import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Detailed Cases (Registered) sexual Assault 2001-2008.csv")

# multiselect feature
def multiselect(title,option_list):
    selected = st.sidebar.multiselect(title,option_list)
    select_all = st.sidebar.checkbox("Select all", value = True, key = title)
    if select_all:
        selected_options = option_list
    else:
        selected_options = selected
    return selected_options