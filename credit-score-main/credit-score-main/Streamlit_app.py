import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

# Load the trained KMeans model from the pickle file
with open('kmeans_credit_model.pkl', 'rb') as model_file:
    kmeans_model = pickle.load(model_file)

# Set up the page configuration
st.set_page_config(page_title="Credit Score Calculator", page_icon=":money_with_wings:", layout="wide")

# Set up a sidebar with additional information and inputs
st.sidebar.title("About")
st.sidebar.info(
    """
    This application helps you calculate your credit score based on various personal financial factors, and segments you into different credit categories.
    Please enter your details to get an estimate of your credit score and segmentation.
    """
)

st.sidebar.image("credit-score.jpg", use_column_width=True)

# Streamlit App Title with Header Image
st.title("💳 Credit Score Calculator & Customer Segmentation")
st.markdown("""
    ---
    """)
st.markdown("""
    This app calculates your credit score based on various financial factors and segments you into different credit categories.
    *Simply enter your details below to get started!*
""")

# Customizing layout with columns to improve aesthetic appeal
col1, col2 = st.columns([1, 2])

# Input fields are placed in the first column for better user flow
with col1:
    st.header("📋 Enter Your Details")

    # User inputs for calculating the credit score
    payment_history = st.slider("Payment History (as percentage, 0 to 100)", 0, 100, 50)
    credit_utilization_ratio = st.slider("Credit Utilization Ratio (as percentage, 0 to 100)", 0, 100, 30)
    number_of_credit_accounts = st.number_input("Number of Credit Accounts", min_value=1, value=5)
    education_level = st.selectbox("Education Level", ['High School', 'Bachelor', 'Master', 'PhD'])
    employment_status = st.selectbox("Employment Status", ['Unemployed', 'Employed', 'Self-Employed'])

# Add an image and additional information about credit scores in the second column
with col2:
    st.image("money-unite.jpg", use_column_width=True)
    st.markdown("""
    #### What factors affect your credit score?
    - **Payment History**: A record of on-time or missed payments.
    - **Credit Utilization**: The ratio of credit used versus total available credit.
    - **Number of Credit Accounts**: Total number of credit accounts you hold.
    - **Education Level**: Level of education, as it may influence credit worthiness.
    - **Employment Status**: Current employment status.
    """)

# Mapping categorical features to numeric values
education_level_mapping = {'High School': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
employment_status_mapping = {'Unemployed': 0, 'Employed': 1, 'Self-Employed': 2}

education_level_numeric = education_level_mapping[education_level]
employment_status_numeric = employment_status_mapping[employment_status]

# Calculate credit score
credit_score = (
    (payment_history * 0.35) +
    (credit_utilization_ratio * 0.30) +
    (number_of_credit_accounts * 0.15) +
    (education_level_numeric * 0.10) +
    (employment_status_numeric * 0.10)
)

# Display the calculated credit score
st.markdown("""
    ---
    """)
st.header("📊 Credit Score & Segment Results")

# Show calculated credit score in a visually appealing metric box
st.metric(label="Calculated Credit Score", value=f"{credit_score:.2f}")

# Create a DataFrame for prediction
input_data = pd.DataFrame({'Credit Score': [credit_score]})

# Predict the segment using the KMeans model
segment = kmeans_model.predict(input_data)[0]

# Mapping the segments to categories
segment_mapping = {2: 'Very Low', 0: 'Low', 1: 'Good', 3: 'Excellent'}
segment_label = segment_mapping.get(segment, "Unknown")

# Display the segment using colored messages for more appeal
if segment_label == "Very Low":
    st.error(f"### Your Credit Segment: {segment_label} 😟")
elif segment_label == "Low":
    st.warning(f"### Your Credit Segment: {segment_label} 🟠")
elif segment_label == "Good":
    st.success(f"### Your Credit Segment: {segment_label} 😊")
else:
    st.balloons()
    st.success(f"### Your Credit Segment: {segment_label} 🎉")

# Additional explanation on credit segment
st.markdown("""
    ---
    """)
st.header("💡 Credit Segment Analysis")
st.markdown("""
    - **Very Low**: You may need significant improvements in your financial profile to improve your credit score.
    - **Low**: Improvement is necessary, but you are on the right track. Focus on reducing credit utilization and timely payments.
    - **Good**: You have a decent credit score. Continue maintaining good financial practices.
    - **Excellent**: Your financial profile is excellent! Keep up the great work.
""")

# Add footer information
st.markdown("""
    ---
    ##### Disclaimer: This credit score calculator is for educational purposes only and does not guarantee any specific results.
""")
