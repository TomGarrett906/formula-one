from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class DriverModel(db.Model):

    __tablename__ = "Drivers"
    driver_id = db.Column(db.Integer, primary_key=True)   
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False, )
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    teamname = db.Column(db.String)
    country = db.Column(db.String)
    team_id = db.Column(db.Integer, db.ForeignKey('Teams.team_id'))

    

    def __repr__(self):
        return f"<Driver: {self.username}>"
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def from_dict(self, dict):
        password = dict.pop("password")
        self.hash_password(password)
        for k,v in dict.items():
            setattr(self, k, v)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
