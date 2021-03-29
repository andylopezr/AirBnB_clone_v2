#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all,delete')

    else:
        name = ""
        @property
        def cities(self):
            """Getter the cities for FileStorage
            """
            city_list = []
            for key, val in storage.all(City).items():
                if val.state_id == self.id:
                    city_list = city_list.append[val]
            return city_list
