#!/usr/bin/python3
"""
This module instantiates an object of class
FileStorage or DBStorage according the HBNB_TYPE_STORAGE
"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
elif getenv('HBNB_TYPE_STORAGE') == 'file':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
