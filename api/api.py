from flask import Blueprint
from flask_restx import Api
from api.resources.user.user_resources import CreateUser, TestPage, GetUser

from api.resources.user.change import change_ns


authorizations = {'Usertoken': {'type': 'apiKey', 'in': 'header', 'name': 'Usertoken'}}


api_blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(
    api_blueprint,
    version='1.0',
    title='REST API / WICE PROJECT',
    doc='/doc',
    authorizations=authorizations,
)
api.add_namespace(change_ns, path='/user/change')

api.add_resource(CreateUser, '/user/create')
api.add_resource(GetUser, '/user/get')
# api.add_resource(UpdateName, '/user/change/name')
api.add_resource(TestPage, '/test')
