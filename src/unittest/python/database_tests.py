from mockito import mock, verify, unstub, when
from datetime import date
import json
import unittest

from database import Client, ProductArea, FeatureRequest, DBSession

class DatabaseTest(unittest.TestCase):
    def test_client_should_create_dict(self):
        client = Client(id=1, name='Client A')
        clientObj = client.to_json()
        client2 = Client(id=clientObj['id'], name=clientObj['name'])
        self.assertEquals(client.id, client2.id)
        self.assertEquals(client.name, client2.name)

    def test_product_area_should_create_dict(self):
        pa = ProductArea(id=1, name='Billing')
        paObj = pa.to_json()
        pa2 = ProductArea(id=paObj['id'], name=paObj['name'])
        self.assertEquals(pa.id, pa2.id)
        self.assertEquals(pa.name, pa2.name)

    def test_feature_request_should_create_dict(self):
        fr = FeatureRequest(id=1, title='Doom', description='Doom Request', client_id=1, client_priority=2, target_date=date.today(), product_area_id=3)
        frObj = fr.to_json()
        fr2 = FeatureRequest(id=frObj['id'], title=frObj['title'], description=frObj['description'], client_id=frObj['client_id'], client_priority=frObj['client_priority'], target_date=frObj['target_date'], product_area_id=frObj['product_area_id'])
        self.assertEquals(fr.id, fr2.id)
        self.assertEquals(fr.title, fr2.title)
        self.assertEquals(fr.description, fr2.description)
        self.assertEquals(fr.client_id, fr2.client_id)
        self.assertEquals(fr.client_priority, fr2.client_priority)
        self.assertEquals(fr.target_date, fr2.target_date)
        self.assertEquals(fr.product_area_id, fr2.product_area_id)
