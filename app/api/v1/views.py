from flask import Blueprint
from flask_restful import Api,Resource

api = Api(__name__)

blue_v1 = Blueprint('api-v1', __name__)

product_items = []

class AllProducts(Resource):

	def post(self):
		data = request.get_json()

		# if len(data) > 5:
		# 	return { 'Error': 'can only take item_id, name, category, price, quantity'}

		item_id = product_items[-1]['item_id'] + 1
		name = data['name']
		category = data['category']
		price = data['price']
		quantity = data['quantity']

		payload = {
				'item_id': item_id,
				'name': name,
				'category': category,
				'price': price,
				'quantity': quantity
				}

		product_items.append(payload)

		return { 'product' : product_items }, 201
