from flask.views import MethodView
# from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from schemas import DriverSchema, EditDriverSchema, TeamSchema, AuthDriverSchema
from . import bp
from .DriverModel import DriverModel
from resources.teams.TeamModel import TeamModel  
from db import drivers, teams





@bp.route('/')
class Drivers(MethodView):

#SHOW DRIVERS
    @bp.response(200, DriverSchema(many=True))
    def get(self):
         return DriverModel.query.all()        

#ADD DRIVER 
    @bp.arguments(DriverSchema)
    @bp.response(201, DriverSchema)
    def post(self, driver_data):
        driver = DriverModel()
        driver.from_dict(driver_data)
        try:
            driver.save()
            return driver_data
        except IntegrityError:
            abort(400, message="Username or Email already taken")

#DELETE DRIVER
    # @jwt_required()
    @bp.arguments(AuthDriverSchema)
    def delete(self, driver_data, driver_id):    
        # driver_id = get_jwt_identity()
        driver = DriverModel.query.get(driver_id)
 
        if driver and driver.username == driver_data['user_name'] and driver.check_password(driver_data['password']):
            driver.delete()
            return {"message": f"{driver_data['username']} deleted"}, 202
        abort(400, message="Username or Password Invalid")
 





@bp.route('/<driver_id>')
class Driver(MethodView):
    @bp.response(200, DriverSchema)
    def get(self, driver_id):
        driver = None
        if driver_id.isdigit():
            driver = DriverModel.query.get(driver_id)
        else:
            driver = DriverModel.query.filter_by(username=driver_id).first()
        if driver:
            return driver
        abort(400, message='Please enter valid username or id')

#EDIT DRIVER
    # @jwt_required()
    @bp.arguments(EditDriverSchema)
    @bp.response(202, EditDriverSchema)          
    def put(self,driver_data, driver_id):
        driver = DriverModel.query.get_or_404(driver_id, description="Driver not found")
        if driver and driver.check_password(driver_data["password"]):
            try:
                driver.from_dict(driver_data)
                driver.save()
                return driver
            except KeyError:
                abort(400, message="Username or Email already taken")






#SHOW DRIVER'S TEAM  
@bp.get('/<driver_id>/team')
@bp.response(200, TeamSchema(many=True)) 
def get_drivers_team(driver_id):
    if driver_id not in drivers:
        abort(404, message="Driver not found")
    drivers_team = [team for team in teams.values() if team['driver_id'] == driver_id]
    return drivers_team