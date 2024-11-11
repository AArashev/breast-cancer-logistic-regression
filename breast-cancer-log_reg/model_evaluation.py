
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

def evaluate_model(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    return cm, accuracy

def display_confusion_matrix(cm):
    plt.figure(figsize=(8, 6))
    ConfusionMatrixDisplay(cm).plot()
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def cross_validate_model(classifier, X_train, y_train):
    accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=10)
    return accuracies.mean(), accuracies.std()
