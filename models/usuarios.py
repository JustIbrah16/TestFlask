from utils.db import db
from .roles import Rol
from .tokens import Token

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    estado = db.Column(db.Boolean, default=True, nullable=False)
    reset_token = db.Column(db.String(100), nullable=True)
    reset_token_expiration = db.Column(db.DateTime, nullable=True)

    fk_rol = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)

    tokens = db.relationship('Token', backref='usuario', lazy=True, cascade='all, delete')

    def __repr__(self):
        return f"<Usuario {self.username}>"
    
