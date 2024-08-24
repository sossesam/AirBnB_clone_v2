#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Integer, Column, VARCHAR, ForeignKey


class City(BaseModel):
    """ The city class, contains state ID and name """
    
    state_id = ''
    name = ''
