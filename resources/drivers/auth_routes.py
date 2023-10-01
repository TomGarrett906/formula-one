from flask.views import MethodView
from flask_jwt_extended import create_access_token
from flask_smorest import abort

from schemas import DriverSchema, AuthDriverSchema
from sqlalchemy.exc import IntegrityError
from . import bp
from .DriverModel import DriverModel


@bp.post('/register')
@bp.arguments(DriverSchema)
@bp.response(201, DriverSchema)       
def register(driver_data):
        driver = DriverModel()
        driver.from_dict(driver_data)
        try:
            driver.save()
            return driver_data
        except IntegrityError:
            abort(400, message='This Username or Email is taken')    


@bp.post('/login')
@bp.arguments(AuthDriverSchema)
def login(login_info):
    if 'username' not in login_info and 'email' not in login_info:
        abort(400, message='Plese include Username or Email')
    if 'username' in login_info:
        driver = DriverModel.query.filter_by(username=login_info['user_name']).first()
    else:
        driver = DriverModel.query.filter_by(email=login_info['user_name']).first()
    if driver and driver.check_password(login_info['password']):
        access_token = create_access_token(indentity=driver.id)
        return {'access_token': access_token}
    abort(400, message='Invalid Usernaem or password')
             