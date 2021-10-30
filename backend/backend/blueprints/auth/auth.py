from flask import Blueprint, json, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity

from backend.ext.database import db

from backend.blueprints.auth.models import Usuario

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/')
def root():
    return 'Hello from auth'

@bp.post('/login')
def login():
    username = request.form["nome"]
    password = request.form["senha"]

    quem = Usuario.query.filter_by(nome=username).first()

    if quem and quem.senha == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    return "No user", 404

@bp.post('/register')
def registro():
    username = request.form["nome"]
    password = request.form["senha"]

    quem = Usuario.query.filter_by(nome=username).first()

    if not quem:
        novo = Usuario()
        novo.nome = username
        novo.senha = password

        db.session.add(novo)
        db.session.commit()

        return jsonify({'status': 'success'})
    return jsonify({'status': 'failed'})

def init_app(app):
    app.register_blueprint(bp)