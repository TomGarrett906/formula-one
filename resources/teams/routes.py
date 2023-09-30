from flask import request
from uuid import uuid4

from app  import app
from db import teams

@app.get('/team')
def get_teams():
    return {"teams": teams}


@app.get('/team/<team_id>')
def get_team(team_id):
    try:
        team = teams[team_id]
        return team, 200
    except KeyError:
        return {"message": "team not found"}, 400


@app.post('/team')
def post_team():
    team_data = request.get_json()
    teams[uuid4().hex] = team_data
    return team_data, 201

@app.put('/team/<team_id>')
def put_team(team_id):
    team_data = request.get_json()
    if team_id in teams:
        team = teams[team_id]
        team["teamname"] = team_data["teamname"]
        return team, 200
    return {"message": "Team not found"}, 400


@app.delete('/team/<team_id>')
def delete_team(team_id):
    try:
        deleted_team = teams.pop(team_id)
        return {"message":f'{deleted_team} was deleted'}, 202
    except KeyError:
        return {"message": "Team not found"}, 400