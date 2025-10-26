import pandas as pd

def load_data(file):
    """Load data from the uploaded file."""
    if file.name.endswith('.csv'):
        return pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        return pd.read_excel(file)
    elif file.name.endswith('.json'):
        return pd.read_json(file)
    else:
        raise ValueError("Unsupported file format")

def preprocess_data(data):
    """Preprocess data: handle missing values and apply transformations."""
    data.fillna(method='ffill', inplace=True)  # Forward fill for missing values
    return data.apply(lambda x: x * 0.01 if x.dtype in ['float64', 'int64'] else x)  # Example transformation
