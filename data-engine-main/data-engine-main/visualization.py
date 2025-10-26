import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

def plot_data(data):
    """Plot data using Plotly."""
    fig = px.line(data, x=data.index, y=data.columns)
    st.plotly_chart(fig)

def display_summary(data):
    """Display summary statistics of the data."""
    st.write("Summary Statistics")
    st.write(data.describe())
