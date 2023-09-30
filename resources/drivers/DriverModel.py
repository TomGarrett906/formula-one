from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class DriverModel(db.Model):

    __tablename__ = "Drivers"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False, )
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    teamname = db.Column(db.String)
    country = db.Column(db.String)

    def __repr__(self):
        return f"<Driver: {self.username}>"
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)