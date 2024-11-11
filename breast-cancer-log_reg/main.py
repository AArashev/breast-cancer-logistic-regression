# -*- coding: utf-8 -*-
"""main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13zMlLnqvGgE9wKKIMKrKEHA6PGiEtgKg
"""

# Import custom modules
from data_preprocessing import load_data, preprocess_data
from feature_engineering import scale_features
from model_training import train_model
from model_evaluation import evaluate_model, display_confusion_matrix, cross_validate_model
from visualization import plot_feature_distributions, plot_correlation_heatmap, plot_boxplots

def main():
    # Load and preprocess data
    dataset = load_data('/content/breast_cancer dataset.csv')
    X, y = preprocess_data(dataset)

    # Visualize data
    plot_feature_distributions(dataset)
    plot_correlation_heatmap(dataset)
    plot_boxplots(dataset)

    # Split the dataset
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Scale features
    X_train_scaled, X_test_scaled = scale_features(X_train, X_test)

    # Train model
    classifier = train_model(X_train_scaled, y_train)

    # Evaluate model
    cm, accuracy = evaluate_model(classifier, X_test_scaled, y_test)
    print("Confusion Matrix:\n", cm)
    print(f"Accuracy: {accuracy * 100:.2f}%")
    display_confusion_matrix(cm)

    # Cross-validation
    mean_accuracy, std_dev = cross_validate_model(classifier, X_train_scaled, y_train)
    print(f"Cross-Validation Accuracy: {mean_accuracy * 100:.2f}%")
    print(f"Standard Deviation: {std_dev * 100:.2f}%")

# Run the main function
main()

from google.colab import drive
drive.mount('/content/drive')