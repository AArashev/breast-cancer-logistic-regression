
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    classifier = LogisticRegression(random_state=0)
    classifier.fit(X_train, y_train)
    return classifier
