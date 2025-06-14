from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
from flask_cors import CORS
from .routes import bp as main_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(main_bp)
    
    # 👇 Initialize PrometheusMetrics with the app directly
    metrics = PrometheusMetrics(app)

    return app
