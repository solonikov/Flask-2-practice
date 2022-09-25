# import logging
# from config import Config
# from flask import Flask, g
# from flask_restful import Api, Resource, abort, reqparse
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
# from flask_httpauth import HTTPBasicAuth
#
# app = Flask(__name__)
# app.config.from_object(Config)
#
# api = Api(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# ma = Marshmallow(app)
# auth = HTTPBasicAuth()
#
#
# # @auth.verify_password
# # def verify_password(username_or_token, password):
# #     from api.models.user import UserModel
# #     # сначала проверяем authentication token
# #     # print("username_or_token = ", username_or_token)
# #     # print("password = ", password)
# #     user = UserModel.verify_auth_token(username_or_token)
# #     if not user:
# #         # потом авторизация
# #         user = UserModel.query.filter_by(username=username_or_token).first()
# #         if not user or not user.verify_password(password):
# #             return False
# #     g.user = user
# #     return True
# ## UPDATE: откатили метод авторизации к старой версии (ниже), так как авторизация
# ## через токены была переписана во время курса:
# @auth.verify_password
# def verify_password(username, password):
#     from api.models.user import UserModel
#     user = UserModel.query.filter_by(username=username).first()
#     if not user or not user.verify_password(password):
#         return False
#     g.user = user
#     return user
#
#
# @auth.get_user_roles
# def get_user_roles(user):
#     return g.user.get_roles()

#################################
## Всё, что ниже, я скопировал у преподавателя
import logging
from config import Config
from flask import Flask, g
from flask_restful import Api, Resource, abort, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
# from flasgger import Swagger
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec

app = Flask(__name__)
app.config.from_object(Config)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Notes Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger',  # URI API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui'  # URI UI of API Doc
})

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth('Bearer')
auth = MultiAuth(basic_auth, token_auth)
docs = FlaskApiSpec(app)
# swagger = Swagger(app)


@basic_auth.verify_password
def verify_password(username, password):
    from api.models.user import UserModel
    user = UserModel.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return user


@token_auth.verify_token
def verify_token(token):
    from api.models.user import UserModel
    user = UserModel.verify_auth_token(token)
    # print(f"{user=}")
    return user


@basic_auth.get_user_roles
def get_user_roles(user):
    return user.get_roles()
