from app import db

class OwnerModel(db.Model):

    __tablename__ = "owners"
    owner_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    teamname = db.Column(db.String)
    country = db.Column(db.String)

    

    def __repr__(self):
        return f"<Owner: {self.ownername}>"
        
    def add_driver(self, driver):
        if driver not in self.drivers:
            self.drivers.append(driver)
            return True
        return False

    def remove_driver(self, driver):
        if driver in self.drivers:
            self.drivers.remove(driver)
            return True
        return False
    
    def add_team(self, team):
        if team not in self.teams:
            self.teams.append(team)
            return True
        return False

    def remove_team(self, team):
        if team in self.teams:
            self.teams.remove(team)
            return True
        return False