from flask import Flask
# from app.config import *
from app.api.v1.views import AllProducts, SpecificProduct, SaleOrders, AttendantSale, Blue_v1
# from flask_restful import Api, Resource
from instance.config import app_config




def create_app(config_name):

	app = Flask(__name__, instance_relative_config=True)
	app.register_blueprint(Blue_v1)
	app.config.from_object(app_config['development'])
	app.config.from_pyfile('config.py')
	
	
	return app
