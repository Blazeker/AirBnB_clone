#!/usr/bin/python3
from datetime import datetime
import uuid
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Class Base """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.strptime(value, time)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ Returns the string representation """
        return "[{}] ({}) {} ".format(self.__class__.__name__,
                                      self.id,
                                      self.__dict__)

    def save(self):
        """ Update the updatet_at attribute """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return the dictionary representation of the attributes """
        my_dict = self.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = self.created_at.strftime(time)
        if "updated_at" in my_dict:
            my_dict["updated_at"] = self.updated_at.strftime(time)
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
