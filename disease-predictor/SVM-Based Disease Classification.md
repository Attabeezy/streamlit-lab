## SVM-Based Disease Classification

This project implements a machine learning model using a Support Vector Machine (SVM) with an RBF kernel to classify diseases based on symptom inputs. The model is trained on a dataset of symptoms and their corresponding diseases, and an interactive command-line interface is provided for users to input symptoms and receive predictions.

**Table of Contents**

* [Overview](#overview)
* [Requirements](#requirements)
* [Dataset](#dataset)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Results](#results)
* [License](#license)

## Overview

This project aims to classify diseases using symptoms entered by the user. The model is trained on a dataset where each disease corresponds to a set of symptoms. The user provides symptoms in a binary format (0 for absent, 1 for present), and the model predicts the most likely disease.

The model uses:

* Support Vector Machine (SVC) with the RBF kernel for classification.
* StandardScaler for feature scaling.

The interactive part of the project allows users to enter symptoms via a command-line interface.

## Requirements

* Python 3.x
* Required Python libraries:
    * numpy
    * pandas
    * scikit-learn

Install these packages using:

```bash
pip install numpy pandas scikit-learn
```

## Dataset

The dataset used for training the model contains:

* 132 symptoms (features) represented as binary values.
* Multiple disease classes (target), each corresponding to a specific combination of symptoms.

The dataset is provided in a CSV file called `Training.csv`, where:

* Each row represents a data point with symptoms as columns and the disease as the target column.

## Installation

1. Clone this repository or download the files.
2. Ensure you have Python 3.x installed on your system.
3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Place the `Training.csv` file in the project directory (or specify its path in the code).

## Usage

### 1. Running the Model

Run the script to train the model and use the interactive command-line interface for classification.

```bash
python svm_disease_classifier.py
```

The user will be prompted to enter symptoms in batches of 20. Each symptom should be entered as 0 (absent) or 1 (present).

### 2. Example Interaction

```bash
Enter symptoms as binary values (0 or 1 for each symptom):

Symptoms 1 to 20:
Symptom1 (0 or 1): 1
Symptom2 (0 or 1): 0
...

Symptoms 21 to 40:
Symptom21 (0 or 1): 1
...

Predicted disease: flu
```

### 3. Model Accuracy and Performance

Once trained, the script will also print out the model's accuracy and a detailed classification report based on the test data.

## Project Structure

```
│
├── Training.csv                # Dataset for training and testing the model
├── svm_disease_classifier.py    # Main script for training, testing, and interactive classification
├── README.md                    # Project documentation
└── requirements.txt             # Required Python libraries
```

## Results

The model achieves high accuracy in predicting diseases based on the symptom data. Example metrics (accuracy, precision, recall) are provided at the end of the training phase.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
