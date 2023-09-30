from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort


from schemas import DriverSchema, EditDriverSchema, TeamSchema
from . import bp
from db import drivers, teams


@bp.route('/')
class Drivers(MethodView):
#SHOW DRIVERS
    @bp.response(200, DriverSchema(many=True))
    def get(self):
        return drivers.values()

#ADD DRIVERS 
    @bp.arguments(DriverSchema)
    @bp.response(201, DriverSchema)
    def post(self, driver_data):
        drivers[uuid4().hex] = driver_data
        return driver_data

#DELETE DRIVERS
    @bp.arguments(DriverSchema)
    def delete(self, driver_data):    
        for i, driver in enumerate(drivers):
            if driver["username"] == driver_data["newusername"]:
                drivers.pop(i)
        return {"message":f'{driver_data["username"]} was deleted'}, 202

 
@bp.route('/<user_id>')
class Driver(MethodView):
#SHOW DRIVER
    @bp.response(200, DriverSchema)      
    def get(self,user_id):
        try:
            driver = drivers[user_id]
            return driver
        except KeyError:
            abort(404, message="Driver not found")

#EDIT DRIVER
    @bp.arguments(EditDriverSchema)
    @bp.response(201, EditDriverSchema)          
    def put(self,driver_data, user_id):
        try:
            driver = drivers[user_id]
            if driver["password"] != driver_data["password"]:
                abort(400, message="Invalid Password")
            driver |= driver_data
            if "newpassword" in driver_data:
                newpassword = driver.pop("newpassword")
                driver["password"] = newpassword
            return driver
        except KeyError:
            abort(404, message="Driver not found")

#SHOW DRIVERS TEAM  
@bp.get('/<user_id>/team')
@bp.response(200, TeamSchema(many=True)) 
def get_drivers_team(user_id):
    print("user_id:", user_id,'\n')
    print("drivers:", drivers,'\n')
    print("teams:", teams,'\n')
    
    if user_id not in drivers:
        abort(404, message="Driver not found")
    drivers_team = [team for team in teams.values() if team['user_id'] == user_id]
    return drivers_team

    # try:
    #     driver = drivers[driver_id]
    #     return driver, 200
    # except KeyError:
    #     return {"message": "driver not found"}, 400