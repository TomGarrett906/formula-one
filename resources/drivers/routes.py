from flask import request

from app  import app
from db import drivers

@app.get('/driver')
def get_drivers():
    return {"drivers": drivers}, 200

@app.post('/driver')
def post_driver():
    driver_data = request.get_json()
    driver_data['races'] = []
    drivers.append(driver_data)
    return driver_data, 201
     
@app.put('/driver')
def put_driver():
    driver_data = request.get_json()
    driver = list(filter(lambda driver: driver["fullname"] == driver_data["fullname"], drivers))[0]
    driver["fullname"] = driver_data["nickname"]
    return driver, 202

@app.delete('/driver')
def delete_driver():
    driver_data = request.get_json()
    for i, driver in enumerate(drivers):
        if driver["fullname"] == driver_data["fullname"]:
            drivers.pop(i)
    return {"message":f'{driver_data["fullname"]} was deleted'}, 202
