import joblib
from sklearn.datasets import load_iris


def load_model(filename):
    model = joblib.load(filename)
    print(f"Model loaded from '{filename}'")
    return ModelWrapper(model)


class ModelWrapper:
    def __init__(self, model):
        self.model = model
        self.target_names = load_iris().target_names

    def predict(self, data_dict):
        features = [list(data_dict.values())]
        pred_idx = self.model.predict(features)[0]
        return self.target_names[pred_idx]
