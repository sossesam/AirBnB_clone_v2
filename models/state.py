#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Integer, Column, VARCHAR
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """ State class """
    name = ''
   


