from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort


from schemas import TeamSchema
from . import bp
from db import teams

@bp.route('/')
class Teams(MethodView):
#SHOW TEAMS    
    def get(self):
        return {"teams": teams}


#EDIT TEAMS
    @bp.arguments(TeamSchema)
    def post(self, team_data):
        teams[uuid4().hex] = team_data
        return team_data, 201

@bp.route('/<team_id>')
class Team(MethodView):
#SHOW TEAM
    def get(self, team_id):
        try:
            team = teams[team_id]
            return team, 200
        except KeyError:
            abort(404, message="Team not found")

#EDIT TEAM
    @bp.arguments(TeamSchema)
    def put(self, team_data, team_id):
        if team_id in teams:
            team = teams[team_id]
            if team_data["user_id"] != team["user_id"]:
                abort(400, message="Cannot edit another Driver's Team")
            team["teamname"] = team_data["teamname"]
            return team, 200
        abort(404, message="Team not found")

#DELETE TEAM
    def delete(self, team_id):
        try:
            deleted_team = teams.pop(team_id)
            return {"message":f'{deleted_team} was deleted'}, 202
        except KeyError:
            abort(404, message="Team not found")