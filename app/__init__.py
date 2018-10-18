from flask import Flask
# from instance import app_config
from app.config import *
from app.api.v1.views import blue_v1



def create_app(test_config=Config):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Development)
    app.register_blueprint(blue_v1, url_prefix='/api/v1')

    app.add_resource(AllProducts, '/products')
    app.add_resource(AllProducts, '/sales')

    return app