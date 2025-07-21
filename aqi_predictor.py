import pickle
import numpy as np

# Load model (ensure model.pkl is available)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_aqi(features):
    features = np.array(features).reshape(1, -1)
    return model.predict(features)[0]