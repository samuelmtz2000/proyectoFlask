from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

engine = create_engine('')
