import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def to_json(self):
        return dict(id=self.id, name=self.name)

class ProductArea(Base):
    __tablename__ = 'product_area'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def to_json(self):
        return dict(id=self.id, name=self.name)

class FeatureRequest(Base):
    __tablename__ = 'feature_request'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=True)
    description = Column(String, nullable=True)
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship(Client)
    client_priority = Column(Integer, nullable=False)
    target_date = Column(Date, nullable=False)
    product_area_id = Column(Integer, ForeignKey('product_area.id'))
    product_area = relationship(ProductArea)

    def to_json(self):
        return dict(id=self.id, title=self.title, description=self.description, \
            client_id=self.client_id, client_priority=self.client_priority, \
            target_date=self.target_date, product_area_id=self.product_area_id)

_engine = create_engine('sqlite:///britecore.db')
Base.metadata.create_all(_engine)
Base.metadata.bind = _engine
DBSession = sessionmaker(bind=_engine)
_session = DBSession()

if len(_session.query(Client).all()) == 0:
    clientA = Client(name='Client A')
    clientB = Client(name='Client B')
    clientC = Client(name='Client C')
    _session.add_all([clientA, clientB, clientC])
    _session.flush()
    _session.commit()

if len(_session.query(ProductArea).all()) == 0:
    policies1 = ProductArea(name='Policies')
    policies2 = ProductArea(name='Billing')
    policies3 = ProductArea(name='Claims')
    policies4 = ProductArea(name='Reports')
    _session.add_all([policies1, policies2, policies3, policies4])
    _session.flush()
    _session.commit()
