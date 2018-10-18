from flask import blueprint
from flask_restful import Api,Resource

api_v1_blueprint = Bueprint('api-v1', __name__)

product_items = []

class AllProducts(Resource):

	def post(self):
		data = request.get_json()
		item_id = product_items[-1]['item_id'] + 1
		name = data['name']
		category = data['category']
		price = data['price']
		quantity = data['quantity']

		payload = {
				'item_id': item_id,
				'name': name,
				'category': category,
				'price': price
				'quantity': quantity
				}

		product_items.append(payload)

		return { 'product' : product_items }, 201
