from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def load_data():
    iris = load_iris()
    return iris.data, iris.target


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model


def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"Model saved to '{filename}'")


if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model, "iris_model.joblib")
