from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import get_jwt_identity, jwt_required

from resources.drivers.DriverModel import DriverModel
from .TeamModel import TeamModel
from schemas import TeamSchema
from . import bp





@bp.route('/')
class Teams(MethodView):

#SHOW TEAMS
    @jwt_required()
    @bp.response(200, TeamSchema(many=True))    
    def get(self):
        return TeamModel.query.all()

# # #EDIT TEAMS
    @jwt_required()
    @bp.arguments(TeamSchema)
    @bp.response(200, TeamSchema)
    def post(self, team_data):
        jwt = get_jwt_identity()
        team_id = jwt['sub']
        team = TeamModel(**team_data, team_id = team_id)        
        try:        
            team.save()
            return team
        except IntegrityError:
            abort(400, message="Invalid Team ID")






@bp.route('/<team_id>')
class Team(MethodView):

# # SHOW TEAM
    @jwt_required()
    @bp.response(200, TeamSchema)
    def get(self, team_id):
        team = TeamModel.query.get(team_id)
        if team:
            return team
        abort(400, message="Invalid Team ID")

# # #EDIT TEAM
    @jwt_required()
    @bp.arguments(TeamSchema)
    @bp.response(200, TeamSchema) 
    def put(self, team_data, team_id):
        team = TeamModel.query.get(team_id)
        if team and team_data["teamname"]:
            if team.team_id == team_id():
                team.teamname = team_data["teamname"]
                team.save()
                return team
            else:
                abort(401, message='Unauthorized')
        abort(400, message="Invalid Team Data")

# # #DELETE TEAM
    def delete(self, team_id):
        team_id = get_jwt_identity()
        team = TeamModel.query.get(team_id)
        if team:
            if team.team_id == team_id:
                team.delete()
                return {'message': 'Team Deleted'}, 202            
            abort(401, message='Owner doesn\'t have rights')
        abort(400, message='Invalid Team ID')