from flask import Flask
from flask_testing import TestCase
from src import app as ginsu
from config import config
import json

class TestProcess(TestCase):
	"""Testing plain processing, no blades"""

	def create_app(self):
		app = ginsu.create_app()
		app.config['TESTING'] = True
		return app

	def test_not_supported(self):
		response = self.client.post('/process/', data=json.dumps({"url":"","type":"exe"}).encode('utf-8'))
		assert response.json['status'] == 400
		assert response.json['message'] == 'file type not supported'

	def test_csv(self):
		data= [dict(foo=1,bar='a'),dict(foo=2,bar='b')]
		response = self.client.post('/process/', data=json.dumps({"url":"https://raw.githubusercontent.com/exversion/ginsu/master/tests/files/test.csv","type":"csv"}).encode('utf-8'))
		for r in response.data.decode("utf-8").splitlines():
			assert json.loads(r) in data