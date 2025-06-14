from flask import Blueprint
from .health import health_bp

bp = Blueprint('main', __name__)

# Register health check route
bp.register_blueprint(health_bp)
