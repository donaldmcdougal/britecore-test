import unittest
import requests
import json
import sys

class IndexTest(unittest.TestCase):

    base_url = 'http://localhost:5000'

    def test_server_should_get_home_page(self):
        page = requests.get(self.base_url)
        self.assertEquals(200, page.status_code)

    def test_server_should_get_three_clients(self):
        clients = requests.get(self.base_url + '/client')
        clientObjs = clients.content
        self.assertEquals(3, len(json.loads(clientObjs)))
        self.assertEquals(200, clients.status_code)

    def test_server_should_get_four_product_areas(self):
        pas = requests.get(self.base_url + '/product_area')
        pasObjs = pas.content
        self.assertEquals(4, len(json.loads(pasObjs)))
        self.assertEquals(200, pas.status_code)
