from flask import Flask, Blueprint
from app.config import *
from app.api.v1.views import *
# from app.api.v1.views import blue_v1
from flask_restful import Api,Resource


blue_v1 = Blueprint('blue_v1', __name__)

api = Api(blue_v1, prefix = '/store-manager/api/v1')

def create_app(default_config=Config):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Development)

    api.add_resource(AllProducts, '/products', endpoint = 'products')
    app.register_blueprint(blue_v1)

    return app