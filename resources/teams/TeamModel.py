from app import db


class TeamModel(db.Model):

    __tablename__ = "Teams"
    team_id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String, nullable=False)
    drivers = db.relationship("DriverModel", backref="drivers", lazy="dynamic", cascade="all, delete")

    def __init__(self, teamname):
        self.teamname = teamname

    def __repr__(self):
        return f"<Team: {self.teamname}>"

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
