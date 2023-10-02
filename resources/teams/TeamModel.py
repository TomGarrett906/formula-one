from app import db


class TeamModel(db.Model):

    __tablename__ = "teams"
    team_id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'))


    def __init__(self, teamname, driver_id):
        self.teamname = teamname
        self.driver_id = driver_id 

    def __repr__(self):
        return f"<Team: {self.teamname}>"

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
