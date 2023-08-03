"""A base class for all other Classes."""

import uuid
from datetime import datetime

class BaseModel:
    """Basemodel class
    
    Initialises id attribute with uuid
    Initialises Created at and Updated at with current time
    """
    def __init__(self):
        """Intialiases Attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """updates the public instance attribute updated_at with the current datetime"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves Data with the corrected time it wass Updated"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Copies The Data In Dictionary form to attributes."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
