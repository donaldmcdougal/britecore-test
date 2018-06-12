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
            client=self.client, client_priority=self.client_priority, \
            target_date=self.target_date, product_area=self.product_area)

_engine = create_engine('sqlite:///britecore.db')
Base.metadata.create_all(_engine)
Base.metadata.bind = _engine
DBSession = sessionmaker(bind=_engine)
