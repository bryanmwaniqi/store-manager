import unittest
import json
# from app.api.v1.views import *
from app import current_app

class TestEndpoints(unittest.TestCase):
	def setup(self):
		self.app.test_client()


	def test_post_product(self):
		test_data = {'item_id':1, 'name':'iphone 7', 'category':'phones', 'price':300, 'quantity': 4 }
		url = self.app.post('/store-manager/api/v1/products', data = json.dumps(test_data), content_type = 'application/json')
		self.assertEquals(url.status_code, 201)

	def test_get_all_products(self):
		url = self.app.get('/store-manager/api/v1/products')
		self.assertEquals(url.status_code, 200)

if __name__ =='__main__':
	app.run(exit=false)