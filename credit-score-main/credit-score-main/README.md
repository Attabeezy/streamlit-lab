# Credit Scoring Analysis and Segmentation

This repository provides a detailed workflow for credit scoring analysis using Python and data visualization tools. The script leverages Pandas, Plotly, and Scikit-Learn to perform data processing, visualize important metrics, and segment customers based on their credit scores. This project can help analyze credit risk and group customers into categories based on credit scores, making it useful for financial institutions aiming to assess creditworthiness.

## Table of Contents
- [Requirements](#requirements)
- [Project Overview](#project-overview)
- [Data Exploration](#data-exploration)
- [Credit Scoring Calculation](#credit-scoring-calculation)
- [Customer Segmentation](#customer-segmentation)
- [Visualizations](#visualizations)
- [Usage](#usage)

## Requirements

Ensure you have the following libraries installed:

```bash
pip install pandas plotly scikit-learn
```

## Project Overview

The script reads a CSV file, `credit_scoring.csv`, containing customer data, processes the data, calculates credit scores using a FICO-based formula, and performs customer segmentation using KMeans clustering.

## Data Exploration

1. **Data Preview**: The first few rows and summary statistics of the dataset are displayed for initial inspection.
2. **Feature Distribution**: Visualizations are created for features such as the `Credit Utilization Ratio` and `Loan Amount`.

```python
# Example data preview
print(data.head())
print(data.info())
print(data.describe())
```

## Credit Scoring Calculation

Using a FICO-based formula, credit scores are computed as a weighted sum of key features:
- **Payment History**: 35%
- **Credit Utilization Ratio**: 30%
- **Number of Credit Accounts**: 15%
- **Education Level**: 10%
- **Employment Status**: 10%

Mappings for categorical variables like `Education Level` and `Employment Status` are applied before calculating the credit scores.

```python
education_level_mapping = {'High School': 1, 'Bachelor': 2, 'Master': 3, 'PhD': 4}
employment_status_mapping = {'Unemployed': 0, 'Employed': 1, 'Self-Employed': 2}
```

## Customer Segmentation

The KMeans clustering algorithm segments customers based on their credit scores into four categories: `Very Low`, `Low`, `Good`, and `Excellent`.

```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, n_init=10, random_state=42)
data['Segment'] = kmeans.labels_
```

## Visualizations

Using Plotly, several charts are generated to understand the data better:

- **Box Plot**: Credit Utilization Ratio
- **Histogram**: Loan Amount Distribution
- **Correlation Heatmap**: For numerical features
- **Scatter Plot**: Customer segmentation based on credit scores

### Example Scatter Plot

```python
fig = px.scatter(data, x=data.index, y='Credit Score', color='Segment',
                 title='Customer Segmentation based on Credit Scores')
fig.show()
```

## Usage

1. Clone this repository.
2. Replace `credit_scoring.csv` with your dataset in the same structure.
3. Run the script to see the data analysis and visualizations.
