#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Integer, Column, VARCHAR, ForeignKey


class City(BaseModel, Base):
    from state import State
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(VARCHAR(60), ForeignKey(State.id),  nullable=False,)
    name = Column(VARCHAR(128), nullable=False)
