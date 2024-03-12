from flask_restx import Namespace, Resource
from flask_restx.reqparse import RequestParser
from api.models.user import User

change_ns = Namespace(name='change')

updateNameParser = RequestParser()
updateNameParser.add_argument(
    'Usertoken',
    location='headers',
    required=True,
    help='Авторизационный токен пользователя',
)
updateNameParser.add_argument('name', required=True, help='Новое имя пользователя')


@change_ns.route(
    '/name',
    doc={
        "description": "Метод для изменения имени пользователя",
        "security": "Usertoken",
    },
)
@change_ns.doc(
    responses={
        200: 'Успешно изменено',
        401: 'Некорректный токен',
        402: 'Не найден пользователь',
    }
)
class UpdateName(Resource):
    @change_ns.expect(updateNameParser)
    def post(self):
        args = updateNameParser.parse_args()
        user = User.getByToken(args['Usertoken'])
        print(user)
        user.name = args['name']
        user.save()
        return 'Name changet to {}'.format(user.name), 200
