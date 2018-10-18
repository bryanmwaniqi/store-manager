from flask import request
from flask_restful import Api,Resource

products_list = []

class AllProducts(Resource):

	""" Products class for getting all products and adding a product to product list """

	def get(self):
		return { 'products':products_list }, 200

	def post(self):

		data = request.get_json()

		if len(data) > 4:
			return { 'Error':'can only take item_id, name, category, price, quantity' }

		item_id = len(products_list) + 1
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

		products_list.append(payload)

		return { 'products' : products_list }, 201

class SpecificProduct(Resource):
	def get(self,item_id):
		item_list = []
		for product in products_list:
			if item_id == product['item_id']:
				item.list.append(product)
				return { 'product': item_list[0] }, 200

		return { 'message': 'no such product found'}, 404