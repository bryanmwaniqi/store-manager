import unittest
import json
from api.v1.views import products

class TestEndpoints(unittest.TestCase):
	def setup(self):
		self.app.test_client()


	def test_post_product(self):
		test_data = {'item_id':1, 'name':'iphone 7', 'category':'phones', 'price':300, 'quantity': 4 }
		url = self.app.post('/store-manager/api/v1/products', data = json.dumps(test_data), content_type = 'application/json')
		self.assertEquals(url.status_code, 201)

	

if __name__ =='main':
	app.run(exit=false)