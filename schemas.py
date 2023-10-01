from marshmallow import Schema, fields

class DriverSchema(Schema):
    driver_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    firstname = fields.Str()
    lastname = fields.Str()
    teamname = fields.Str()
    country = fields.Str()

class TeamSchema(Schema):
    team_id = fields.Str(dump_only=True)
    teamname = fields.Str(required=True)
    driver_id = fields.Str(required=True)

class DriverSchemaNested(Schema):
    driver = fields.List(fields.Nested(DriverSchema), dump_only = True)
    team = fields.List(fields.Nested(TeamSchema), dump_only = True)

class EditDriverSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(required=True, load_only=True)
    newpassword = fields.Str()
    firstname = fields.Str()
    lastname = fields.Str()
    teamname = fields.Str()
    country = fields.Str()

class AuthDriverSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(required=True, load_only=True)

class OwnerSchema(Schema):
    owner_id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    firstname = fields.Str()
    lastname = fields.Str()
    country = fields.Str()

class EditOwnerSchema(Schema):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str(required=True, load_only=True)
    newpassword = fields.Str()
    firstname = fields.Str()
    lastname = fields.Str()
    country = fields.Str()