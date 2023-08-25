import joblib
def load_model():
    return joblib.load('gradient_model.pkl')

model = load_model()