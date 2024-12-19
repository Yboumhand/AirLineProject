from flask import Flask
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__) #la variable app importée dans le fichier run.py
app.config['SECRET_KEY'] = 'a0328ff97a140cd069e8d064c47b6caf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) # instance of the database we have created

# from mon_app import routes