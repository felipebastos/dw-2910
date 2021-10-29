from flask import Blueprint, json, jsonify


bp = Blueprint('api_v1', __name__, url_prefix='/api_v1')


@bp.route('/')
def root():
    return jsonify({'mensagem': 'Hello from api_v1'})


def init_app(app):
    app.register_blueprint(bp)