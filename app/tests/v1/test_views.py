import unittest
import json
from flask import current_app

class TestEndpoints(unittest.TestCase):

	def setup(self):
		self.current_app.test_client()


	def test_post_product(self):
		test_data = {'item_id':1, 'name':'iphone 7', 'category':'phones', 'price':300, 'quantity': 4 }
		url = self.current_app.post('/store-manager/api/v1/products', data = json.dumps(test_data), content_type = 'application/json')
		self.assertEquals(url.status_code, 201)

	def test_get_all_products(self):
		url = self.current_app.get('/store-manager/api/v1/products')
		self.assertEquals(url.status_code, 200)

	def test_get_specific_product(self):
		url = self.current_app.get('/store-manager/api/v1/products/tie')
		self.assertEquals(url.status_code, 404)
		url2 = self.current_app.get('/store-manager/api/v1/products/1')
		self.assertEquals(url.status_code, 200)

	def test_post_sale(self):
		test_data = {'sale_id':1, 'products_tally':20, 'total_cost':300, 'attendant_id': 6432 }
		url = self.current_app.post('/store-manager/api/v1/sales', data = json.dumps(test_data), content_type = 'application/json')
		self.assertEquals(url.status_code, 201)

	def test_get_all_sale_orders(self):
		url = self.current_app.get('/store-manager/api/v1/sales')
		self.assertEquals(url.status_code, 200)

	def test_get_specific_sale(self):
		url = self.current_app.get('/store-manager/api/v1/sales/tie')
		self.assertEquals(url.status_code, 404)
		rl2 = self.current_app.get('/store-manager/api/v1/products/1')
		self.assertEquals(url.status_code, 200)


if __name__ =='__main__':
	current_app.run(exit=false)