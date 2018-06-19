import unittest
import requests
import json
import sys
from database import FeatureRequest
from datetime import date
from index import app

class IndexTest(unittest.TestCase):

    base_url = 'http://localhost:5000'

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_METHODS'] = []  # This is the magic
        self.app = app.test_client()

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

    def test_server_should_get_no_frs(self):
        frs = requests.get(self.base_url + '/feature_request')
        frObjs = frs.content
        self.assertEquals(0, len(json.loads(frObjs)))
        self.assertEquals(200, frs.status_code)

    def test_server_should_create_fr(self):
        fr = FeatureRequest(title='FR', description='Test FR',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr.to_json()
        headers = {'Content-Type': 'application/json'}
        frSaved = requests.post(self.base_url + '/feature_request', data=json.dumps(frJson), headers=headers)
        self.assertEquals(200, frSaved.status_code)
        frSavedJson = json.loads(frSaved.content)
        self.assertEquals(1, frSavedJson['id'])
        # now delete the feature request
        deleted = requests.delete(self.base_url + '/feature_request/1')
        self.assertEquals(200, deleted.status_code)

    def test_server_should_get_all_frs(self):
        fr = FeatureRequest(title='FR', description='Test FR',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr.to_json()
        headers = {'Content-Type': 'application/json'}
        frSaved = requests.post(self.base_url + '/feature_request', data=json.dumps(frJson), headers=headers)
        frs = requests.get(self.base_url + '/feature_request')
        frObjs = frs.content
        self.assertEquals(1, len(json.loads(frObjs)))
        self.assertEquals(200, frs.status_code)
        # now delete the feature request
        deleted = requests.delete(self.base_url + '/feature_request/1')
        self.assertEquals(200, deleted.status_code)

    def test_server_should_get_one_fr(self):
        fr = FeatureRequest(title='FR', description='Test FR',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr.to_json()
        headers = {'Content-Type': 'application/json'}
        frSaved = requests.post(self.base_url + '/feature_request', data=json.dumps(frJson), headers=headers)
        frReturned = requests.get(self.base_url + '/feature_request/1')
        frObj = json.loads(frReturned.content)
        self.assertEquals(1, frObj['id'])
        self.assertEquals(200, frReturned.status_code)
        # now delete the feature request
        deleted = requests.delete(self.base_url + '/feature_request/1')
        self.assertEquals(200, deleted.status_code)

    def test_server_should_not_update_non_existent_fr(self):
        fr = FeatureRequest(title='FR', description='Test FR',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr.to_json()
        headers = {'Content-Type': 'application/json'}
        frSaved = requests.put(self.base_url + '/feature_request/1', data=json.dumps(frJson), headers=headers)
        self.assertEquals(404, frSaved.status_code)

    def test_server_should_update_fr(self):
        fr = FeatureRequest(title='FR', description='Test FR',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr.to_json()
        headers = {'Content-Type': 'application/json'}
        frSaved = requests.post(self.base_url + '/feature_request', data=json.dumps(frJson), headers=headers)
        frReturned = requests.get(self.base_url + '/feature_request/1')
        frObj = json.loads(frReturned.content)
        self.assertEquals(1, frObj['id'])
        self.assertEquals(200, frReturned.status_code)
        fr.description = 'Test FR 2'
        frJson = fr.to_json()
        frSaved = requests.put(self.base_url + '/feature_request/1', data=json.dumps(frJson), headers=headers)
        self.assertEquals(200, frSaved.status_code)
        # now delete the feature request
        deleted = requests.delete(self.base_url + '/feature_request/1')
        self.assertEquals(200, deleted.status_code)

    def test_server_should_not_delete_non_existent_fr(self):
        deleted = requests.delete(self.base_url + '/feature_request/1')
        self.assertEquals(404, deleted.status_code)

    def test_server_should_not_allow_delete_without_id(self):
        deleted = requests.delete(self.base_url + '/feature_request')
        self.assertEquals(405, deleted.status_code)

    def test_server_should_reassign_priorities(self):
        fr1 = FeatureRequest(title='FR', description='Test FR',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr1.to_json()
        headers = {'Content-Type': 'application/json'}
        frSaved = requests.post(self.base_url + '/feature_request', data=json.dumps(frJson), headers=headers)
        frReturned = requests.get(self.base_url + '/feature_request/1')
        frObj = json.loads(frReturned.content)
        self.assertEquals(1, frObj['id'])
        self.assertEquals(200, frReturned.status_code)

        fr2 = FeatureRequest(title='FR', description='Test FR 2',
            client_id=1, client_priority=1,
            target_date='2018-06-30', product_area_id=1)
        frJson = fr2.to_json()
        frSaved = requests.post(self.base_url + '/feature_request', data=json.dumps(frJson), headers=headers)
        self.assertEquals(200, frSaved.status_code)
        frReturned = requests.get(self.base_url + '/feature_request/1')
        frObj = json.loads(frReturned.content)
        self.assertEquals(2, frObj['client_priority'])
        self.assertEquals(200, frReturned.status_code)

        frJson = fr1.to_json()
        frSaved = requests.put(self.base_url + '/feature_request/1', data=json.dumps(frJson), headers=headers)
        self.assertEquals(200, frSaved.status_code)
        frReturned = requests.get(self.base_url + '/feature_request/1')
        frObj = json.loads(frReturned.content)
        self.assertEquals(1, frObj['client_priority'])
        self.assertEquals(200, frReturned.status_code)

        # now delete the feature requests
        deleted = requests.delete(self.base_url + '/feature_request/1')
        self.assertEquals(200, deleted.status_code)
        deleted = requests.delete(self.base_url + '/feature_request/2')
        self.assertEquals(200, deleted.status_code)
