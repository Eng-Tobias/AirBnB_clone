#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage

class BaseModel:
    """BaseModel defines all common attributes and methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Updates the public instance attribute updated_at and saves to storage."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Returns the string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
