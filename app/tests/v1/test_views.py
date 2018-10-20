import unittest
import json
from app import create_app



class TestEndpoints(unittest.TestCase):

	def setUp(self):
		self.app = create_app("testing").test_client()


	def test_post_product(self):
		test_data = { "name":"iphone 8", "category":"phones", "price":300, "quantity": 50 }
		url = self.app.post('/store-manager/api/v1/products', data = json.dumps(test_data), content_type = 'application/json')
		self.assertEqual(url.status_code, 201)

	def test_get_all_products(self):
		url = self.app.get('/store-manager/api/v1/products')
		self.assertEqual(url.status_code, 200)

	def test_get_specific_product(self):
		url = self.app.get('/store-manager/api/v1/products/1')
		self.assertEqual(url.status_code, 200)

	def test_post_sale(self):
		test_data = {"product_id":1, "products_tally":2, "total_cost":300, "attendant_id": 6432 }
		url = self.app.post('/store-manager/api/v1/sales', data = json.dumps(test_data), content_type = 'application/json')
		self.assertEqual(url.status_code, 201)

	def test_get_all_sale_orders(self):
		url = self.app.get('/store-manager/api/v1/sales')
		self.assertEqual(url.status_code, 200)

	def test_get_specific_sale(self):
		url = self.app.get('/store-manager/api/v1/sales/tie')
		self.assertEqual(url.status_code, 404)
		rl2 = self.app.get('/store-manager/api/v1/sales/5')
		self.assertEqual(url.status_code, 404)


if __name__ =='__main__':
	unittest.main(exit=false)