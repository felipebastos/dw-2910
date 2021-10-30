from backend.ext.database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), nullable=False, unique=True)
    senha = db.Column(db.String(100), nullable=False)
