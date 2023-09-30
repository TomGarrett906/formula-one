from marshmallow import Schema, fields

class TeamSchema(Schema):
    id = fields.Str(dump_only=True)
    teamname = fields.Str(required=True)
    user_id = fields.Str(required=True)

class DriverSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    firstname = fields.Str()
    lastname = fields.Str()
    teamname = fields.Str()
    country = fields.Str()

class EditDriverSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(required=True)
    newpassword = fields.Str()
    firstname = fields.Str()
    lastname = fields.Str()
    teamname = fields.Str()
    country = fields.Str()
