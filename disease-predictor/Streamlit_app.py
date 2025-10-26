import streamlit as st
import numpy as np
import pickle

# Load the trained SVM model, scaler, and label encoder
with open('svm_model.pkl', 'rb') as f:
    svm_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Define the actual symptom names from the dataset and sort them alphabetically
symptom_names = sorted([
    'itching', 'skin rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain',
    'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 
    'spotting urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feet', 'mood swings', 
    'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 
    'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 
    'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 
    'constipation', 'abdominal pain', 'diarrhoea', 'mild fever', 'yellow urine', 'yellowing of eyes', 
    'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 
    'blurred and distorted vision', 'phlegm', 'throat irritation', 'redness of eyes', 'sinus pressure', 
    'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 
    'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 
    'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 
    'brittle nails', 'swollen extremities', 'excessive hunger', 'extra-marital contacts', 'drying and tingling lips', 
    'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 
    'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 
    'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 
    'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 
    'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic patches', 'watering from eyes', 
    'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 
    'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 
    'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload (duplicate)', 
    'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus-filled pimples', 
    'blackheads', 'scarring', 'skin peeling', 'silver-like dusting', 'small dents in nails', 'inflammatory nails', 
    'blister', 'red sore around nose', 'yellow crust ooze'
])

# Streamlit UI Enhancements
st.markdown(
    """
    <style>
    body {
        background-color: #f2f2f2;
    }
    .stButton button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
        font-weight: bold;
    }
    .symptom-col {
        font-size: 14px;
        font-family: 'Arial', sans-serif;
        color: #333;
        background-color: #fff;
        border: 1px solid #ddd;
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
    }
    .welcome {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #3f51b5;
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔍 Disease Prediction Based on Symptoms")

# Welcome message
st.markdown("""
    <div style='padding: 10px; border-radius: 10px; background-color: #e7f3fe; border: 1px solid #b3d4fc;'>
        <h3 class="welcome">Welcome to the Disease Prediction App! 🎉</h3>
        <p class="welcome">
            This application helps you predict possible diseases based on your symptoms. 😊
            <br>
            Please select your symptoms from the list below or use the search feature to quickly find them. 
            <br>
            After selecting, click the "Predict" button in the sidebar to get your results! 🚀
        </p>
    </div>
""", unsafe_allow_html=True)

# Multiselect widget to choose symptoms
selected_symptoms = st.multiselect(
    "🔎 Search and select your symptoms:", symptom_names)

# Display the list of symptoms in alphabetical order, in 3 columns
st.write("### Available symptoms:")
col1, col2, col3 = st.columns(3)

# Split the symptoms evenly across the 3 columns and apply styling
for i, symptom in enumerate(symptom_names):
    if i % 3 == 0:
        col1.markdown(f"<div class='symptom-col'>{symptom}</div>", unsafe_allow_html=True)
    elif i % 3 == 1:
        col2.markdown(f"<div class='symptom-col'>{symptom}</div>", unsafe_allow_html=True)
    else:
        col3.markdown(f"<div class='symptom-col'>{symptom}</div>", unsafe_allow_html=True)

# Move the prediction button to the sidebar
with st.sidebar:
    if len(selected_symptoms) < 3:
        st.warning("⚠️Select at least 3 symptoms⚠️")
    else:
        if st.button('Predict Now! 🚀'):
            # Convert the selected symptoms into binary form (1 if selected, else 0)
            symptoms_input = [1 if symptom in selected_symptoms else 0 for symptom in symptom_names]
            
            symptoms_array = np.array(symptoms_input).reshape(1, -1)
            symptoms_scaled = scaler.transform(symptoms_array)
            prediction = svm_model.predict(symptoms_scaled)
            predicted_disease = label_encoder.inverse_transform(prediction)[0]
            st.sidebar.success(f"⚕️ Predicted Disease: **{predicted_disease}**")
