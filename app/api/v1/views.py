from flask import request
from flask_restful import Api,Resource
from datetime import datetime

products_list = []
sale_orders_list = []

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

		if type(item_id, int) == False:
			return { 'Error message': 'Please supply an integer value'}

		item_list = []
		for product in products_list:
			if item_id == product['item_id']:
				item.list.append(product)
				return { 'product': item_list[0] }, 200

		return { 'message': 'no such product found'}, 404

class sale_orders(Resource):
	def post(self):
		data = request.get_json()

		sale_id = len(sale_orders_list)  + 1
		date = datetime.datetime.now()
		product_id = data['product_id']
		products_tally = data['products_tally']
		total_cost =data['total_cost']
		attendant_id = data['attendant_id']

		payload = {
				'sale_id': sale_id,
				'date': date
				'product_id': product_nid,
				'products_tally' : products_tally,
				'total_cost' : total_cost,
				'attendant_id' : attendant_id
				}

		sale_item = [item for item in products_list if item['item_id'] == product_id]

		if len(sale_item) > 0:
			available = sale_item[0]['quantity']
			if products_tally <= available:
				rem = available - products_tally
				sale_item[0].update('quantity' = rem)
				return { 'success':'Order succesfuly placed'}

		
		

		

