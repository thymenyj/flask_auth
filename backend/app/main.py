from flask import Flask
from views.ExampleView import ExampleView
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'mysecretkey'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)


app.add_url_rule('/example', view_func=ExampleView.as_view('example'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
