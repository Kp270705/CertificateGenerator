import bcrypt
from db.extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    name = db.Column(db.String(150), nullable=0)
    password = db.Column(db.String(150), nullable=0, unique=1)
    confirm_password = db.Column(db.String(150), nullable=0, unique=1)
    email = db.Column(db.String(150), nullable=0)
    # fav_color = db.Column(db.String(30), nullable=1)
    
    print(f" confirm pass{confirm_password}")
    
    # used to initialise the db's data:
    def __init__(self, name, email, password, confirm_password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()
        self.confirm_password = confirm_password
        # self.fav_color = fav_color

    # used to check password:
    def check_password(self, pasword):
        return bcrypt.checkpw(pasword.encode('utf-8'), self.password.encode('utf-8'))