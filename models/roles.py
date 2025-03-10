from utils.db import db
from .usuarios import Usuario

class Rol(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, pirmay_key=True, autoimcrement=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)
    
    usuarios = db.relationship('Usuario', backref='rol', lazy=True)

    def __repr__(self):
        return f"<Rol {self.nombre}>"
    