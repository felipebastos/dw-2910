from backend.ext.database import db

from datetime import datetime

class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    remetente = db.Column(db.String(20), nullable=False, default="Anônimo")
    data = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String(100), nullable=False)
