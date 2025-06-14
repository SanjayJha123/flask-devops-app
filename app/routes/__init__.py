from .health import health_bp
from .auth import auth_bp
from .predict import predict_bp

def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(predict_bp)