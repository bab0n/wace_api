from flask_restx import Resource, reqparse, fields
from api.models.user import User, UserTemplates
from flask import request
import jwt


class TestPage(Resource):
    def get(self):
        return 'Hello from wace api, age is ' + request.cookies.get('age'), 200


createUserParser = reqparse.RequestParser()
createUserParser.add_argument('phone', type=str, required=True)


class CreateUser(Resource):
    def post(self):
        args = createUserParser.parse_args()
        if User.query.filter(User.phone == args.get('phone')).first() is not None:
            return 'User already exitsts', 400
        else:
            new_user = User(phone=args.get('phone'))
            new_user.add_new()
            return 'User created', 200


class GetUser(Resource):
    def get(self):
        login = jwt.decode(
            request.headers.get('Usertoken'), 'secret', algorithms=['HS256']
        ).get('login')
        user = User.query.filter(User.phone == login).first()
        if user is None:
            return 'User not found', 401
        else:
            return user.getInfo(), 200
