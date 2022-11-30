#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
import models
import os
STRG = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    if STRG == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """ Getter method """
            from models import storage
            my_list = []
            for i in list(storage.all(City).values()):
                if self.id == i.state_id:
                    my_list.append(i)
            return my_list
