import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
file_path = 'data.csv'  # Path to your CSV file
data = pd.read_csv(file_path)

# Get symptom names from the columns (ignoring the 'prognosis' column)
symptom_names = list(data.columns[:-1])

# Step 1: Data Preprocessing
# Encode the target labels (prognosis)
label_encoder = LabelEncoder()
data['prognosis'] = label_encoder.fit_transform(data['prognosis'])

# Separate features and target label
X = data.drop(columns=['prognosis'])
y = data['prognosis']

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 2: Model Training
# Train the SVM model with RBF kernel
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train_scaled, y_train)

# Step 3: Model Evaluation
# Make predictions on the test set
y_pred = svm_model.predict(X_test_scaled)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

classification_rep = classification_report(y_test, y_pred, target_names=label_encoder.classes_)
print("\nClassification Report:\n", classification_rep)

# Step 4: Interactive Command-line Classification
# Function to classify user input based on symptoms
def classify_symptoms(symptoms):
    symptoms_array = np.array(symptoms).reshape(1, -1)  # Reshape input for model
    symptoms_scaled = scaler.transform(symptoms_array)  # Scale the input
    prediction = svm_model.predict(symptoms_scaled)  # Predict using SVM model
    
    # Convert prediction to the corresponding disease label
    predicted_disease = label_encoder.inverse_transform(prediction)[0]
    return predicted_disease

# Simulate an interactive classification in command-line style
def interactive_classification():
    symptoms = []  # Initialize the symptoms array
    print("Enter symptoms as binary values (0 or 1 for each symptom):")
    
    # Display symptoms in batches of 20
    for i in range(0, len(symptom_names), 20):  # Process 20 symptoms at a time
        print(f"\nSymptoms {i+1} to {min(i+20, len(symptom_names))}:")
        for j in range(i, min(i + 20, len(symptom_names))):  # Handle up to 20 symptoms per batch
            while True:
                try:
                    value = int(input(f"{symptom_names[j]} (0 or 1): "))  # Ask for user input for each symptom
                    if value in [0, 1]:
                        symptoms.append(value)
                        break
                    else:
                        print("Invalid input, please enter 0 or 1.")
                except ValueError:
                    print("Please enter a valid number (0 or 1).")

    # Classify based on user input
    result = classify_symptoms(symptoms)
    print(f"\nPredicted disease: {result}")