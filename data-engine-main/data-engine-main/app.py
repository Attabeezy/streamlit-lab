import streamlit as st
from data_processing import load_data, preprocess_data
from generative_model import generate_text
from visualization import plot_data, display_summary
from logging_config import log_event

st.title("Data Engine: Real-Time Generative AI")

# File upload
file = st.file_uploader("Upload Data File", type=['csv', 'xlsx', 'json'])
if file:
    log_event("File uploaded: {}".format(file.name))  # Log file upload
    data = preprocess_data(load_data(file))

    st.subheader("Uploaded Data")
    st.write(data.head())

    st.subheader("Data Visualization")
    plot_data(data)

    display_summary(data)

    st.subheader("Generative AI Insights")
    prompt = st.text_input("Enter a prompt for data analysis insight:")
    if st.button("Generate Insight"):
        generated_text = generate_text(prompt)
        st.write(generated_text)
        log_event("Generated insight for prompt: {}".format(prompt))  # Log AI generation

    st.download_button(
        label="Download Analysis Report",
        data=data.to_csv(index=False),
        file_name='report.csv',
        mime='text/csv'
    )
