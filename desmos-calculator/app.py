import streamlit as st
import sympy as sp

# Define function to plot on Desmos calculator
def plot_desmos(expression):
    # Render Desmos iframe
    desmos_url = f"https://www.desmos.com/calculator?embed&expressions=[{{'latex':'{expression}'}}]"
    desmos_html = f'<iframe src="{desmos_url}" width="100%" height="500px"></iframe>'

    # Display Desmos calculator in Streamlit
    st.markdown(desmos_html, unsafe_allow_html=True)

# Streamlit app layout
st.title("Desmos Calculator in Streamlit")

# Input for mathematical expression
expression_input = st.text_input("Enter a mathematical expression", value="x^2")

# Button to generate plot
if st.button("Plot on Desmos"):
    plot_desmos(expression_input)
