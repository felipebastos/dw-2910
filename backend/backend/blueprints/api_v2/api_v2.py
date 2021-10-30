from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.ext.database import db
from backend.ext.auth import jwt

from backend.blueprints.api_v2.models import Mensagem

bp = Blueprint('api_v2', __name__, url_prefix='/api_v2')
api = Api(bp)

class ConverasList(Resource):
    @jwt_required()
    def get(self):
        msgs = []
        for msg in Mensagem.query.all():
            msgs.append({'remetente': msg.remetente, 'data': msg.data, 'texto':msg.texto})

        return jsonify({'mensagens': msgs})


class Conversas(Resource):
    @jwt_required()
    def post(self):
        nova = Mensagem()
        nova.remetente = request.form['rem']
        nova.texto = request.form['n_message']

        db.session.add(nova)
        db.session.commit()

        return jsonify({'status': 'success'})

api.add_resource(ConverasList, '/')
api.add_resource(Conversas, '/put')

def init_app(app):
    app.register_blueprint(bp)