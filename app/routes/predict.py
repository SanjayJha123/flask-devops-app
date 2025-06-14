from flask import Blueprint, request, jsonify
from app.utils.model import predict_value

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data.get("features", [])
    prediction = predict_value(features)
    return jsonify({"prediction": prediction})