#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, DateTime, String


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
       
        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    format = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.strptime(value, format) 

                elif key == "updated_at":
                    format = '%Y-%m-%dT%H:%M:%S.%f'
                    value = datetime.strptime(value, format)

                setattr(self, key, value)
            

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        new_dict = {}

        for key, value in self.__dict__.items():
            if key == "updated_at":
                new_dict[key] = self.created_at.isoformat()
            elif key == "created_at":
                new_dict[key] = self.updated_at.isoformat()
            else:
                new_dict[key] = value
        if "__class__" not in self.__dict__.keys():
            new_dict["__class__"] = self.__class__.__name__

        return new_dict

    def to_update(self, args):
        for para in args:
            key, value = para.split("=")
            value = value.replace('"', '/"')
            setattr(self, key, value)
