from flask import request
from uuid import uuid4

from app  import app
from db import drivers, teams

@app.get('/driver')
def get_drivers():
    return {"drivers": drivers}, 200

@app.get('/driver/<driver_id>')
def get_driver(driver_id):
    try:
        driver = drivers[driver_id]
        return driver, 200
    except KeyError:
        return {"message": "driver not found"}, 400

        
@app.post('/driver')
def post_driver():
    driver_data = request.get_json()
    drivers[uuid4().hex] = driver_data
    return driver_data, 201
     
@app.put('/driver/<driver_id>')
def put_driver(driver_id):
    driver_data = request.get_json()
    try:
        driver = drivers[driver_id]
        driver["name"] = driver_data["newname"]
        return driver, 200
    except KeyError:
        return {"message": "driver not found"}, 400

@app.delete('/driver')
def delete_driver():
    driver_data = request.get_json()
    for i, driver in enumerate(drivers):
        if driver["name"] == driver_data["name"]:
            drivers.pop(i)
    return {"message":f'{driver_data["name"]} was deleted'}, 202

@app.get('/driver/<driver_id>/team')
def get_drivers_team(driver_id):
    if driver_id not in drivers:
        return {"message": "driver not found"}, 400
    drivers_team = [team for team in teams.values() if team['driver_id'] == driver_id]
    return drivers_team, 200

    # try:
    #     driver = drivers[driver_id]
    #     return driver, 200
    # except KeyError:
    #     return {"message": "driver not found"}, 400