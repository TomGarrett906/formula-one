from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
# from flask_jwt_extended import get_jwt_identity, jwt_required

from .OwnerModel import OwnerModel
from schemas import EditOwnerSchema, OwnerSchema
from . import bp





@bp.route('/')
class Owners(MethodView):

#SHOW OWNERS
    @bp.response(200, OwnerSchema(many=True))
    def get(self):
        owners = OwnerModel.query.all()
        return owners

#ADD OWNER
    @bp.arguments(OwnerSchema)
    @bp.response(201, OwnerSchema)
    def post(self, owner_data):
        owner = OwnerModel(**owner_data)
        try:
            owner.save()
            return owner_data, 201
        except IntegrityError:
            abort(400, message="Owner already exists")





@bp.route('/<owner_id>')
class Owner(MethodView):

#SHOW OWNER
    @bp.response(200, OwnerSchema)
    def get(self, owner_id):
        owner = OwnerModel.query.get(owner_id)
        if owner:
            return owner
        abort(404, message="Owner not found")

#EDIT OWNER
    # @jwt_required()
    @bp.arguments(EditOwnerSchema)
    @bp.response(200, OwnerSchema)
    def put(self, owner_data, owner_id):
        # current_owner_id = get_jwt_identity()
        owner = OwnerModel.query.get(owner_id)
        if owner and owner.owner_id == owner_id:
            try:
                owner.from_dict(owner_data)
                owner.save()
                return owner
            except KeyError:
                abort(400, message="Invalid owner data")
        abort(401, message="Unauthorized")

#DELETE OWNER
    # @jwt_required()
    def delete(self, owner_id):
        # owner_id = get_jwt_identity()
        owner = OwnerModel.query.get(owner_id)
        if owner and owner.owner_id == owner_id:
            owner.delete()
            return {"message": "Owner deleted"}, 202
        abort(401, message="Unauthorized") 