
import pandas as pd

def load_data(filepath):
    dataset = pd.read_csv(filepath)
    return dataset

def preprocess_data(dataset):
    X = dataset.iloc[:, 1:-1].values  # Selecting feature columns
    y = dataset.iloc[:, -1].values    # Selecting target column
    return X, y
