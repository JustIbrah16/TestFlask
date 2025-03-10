from flask import Flask
from flask_cors import CORS
from utils.db import db


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type", "Authorization"]}})

app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/testflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

db.init_app(app)

