from utils.db import db
from .usuarios import Usuario
from datetime import datetime

class Token(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    token = db.Column(db.String(255), nullable=False, unique=True)
    expiracion = db.Column(db.DateTime, nullable=False, default=lambda: datetime.utcnow())

    def __repr__(self):
        return f"<Token {self.token[:10]}...>"