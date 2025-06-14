import numpy as np
from sklearn.linear_model import LinearRegression

# Dummy model for prediction
model = LinearRegression()
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model.fit(X, y)

def predict_value(features):
    X_input = np.array(features).reshape(-1, 1)
    return model.predict(X_input).tolist()