from flask_restful import Api
from controller import Test
from flask import Blueprint

routes_blueprint = Blueprint(name='routes', import_name=__name__)

api = Api(routes_blueprint, default_mediatype="application/json")
api.add_resource(Test, f'/api/v1/test')
